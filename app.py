from flask import Flask, render_template, request, send_from_directory
import os
from style_transfer_model import run_style_transfer, image_loader, tensor_to_image, device, cnn, cnn_normalization_mean, cnn_normalization_std
from PIL import Image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    content_image = request.files['content_image']
    style_image = request.files['style_image']
    
    content_path = os.path.join(app.config['UPLOAD_FOLDER'], 'content.jpg')
    style_path = os.path.join(app.config['UPLOAD_FOLDER'], 'style.jpg')
    
    content_image.save(content_path)
    style_image.save(style_path)
    
    content_img = image_loader(content_path)
    style_img = image_loader(style_path)
    
    input_img = content_img.clone()
    
    output_img = run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std,
                                    content_img, style_img, input_img, num_steps=300)
    
    output_image = tensor_to_image(output_img)
    output_path = os.path.join('static', 'output_image.jpg')
    output_image.save(output_path)
    
    return render_template('result.html', output_image='static/output_image.jpg')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
