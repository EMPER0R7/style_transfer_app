# Neural Style Transfer Flask App

This repository contains a Flask web application that performs neural style transfer . The app allows users to upload a content image and a style image, and it generates a new image that combines the content of the first image with the style of the second image.

## Features
- Upload content and style images through a web interface.
- Generate a stylized image using neural style transfer.
- Save and display the generated image.

## Requirements
- Git
- Python 3.7+
- Flask
- Torch
- Torchvision
- Pillow

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/EMPER0R7/style_transfer_app.git
    cd style_transfer_app
    ```

2. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Flask application**:
    ```sh
    python app.py
    ```

4. **Open your browser and go to** `http://127.0.0.1:5000/` **to access the app**.

## Usage

1. Open the application in your web browser.
2. Upload a content image and a style image using the provided form.
3. Click on the "Submit" button to start the style transfer process.
4. Wait for the process to complete. The generated image will be displayed on the result page.

## Project Structure

- `app.py`: The main Flask application file.
- `style_transfer_model.py`: Contains the neural style transfer implementation.
- `templates/`: Directory containing HTML templates.
  - `index.html`: The main page for uploading images.
  - `result.html`: The page for displaying the generated image.
- `static/`: Directory for static files (e.g., the generated image).
- `uploads/`: Directory for temporarily storing uploaded images.

## Dependencies

- Flask
- Torch
- Torchvision
- Pillow

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.


