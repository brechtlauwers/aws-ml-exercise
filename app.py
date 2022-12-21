from flask import Flask, render_template, request
import boto3
import model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['GET', 'POST'])
def process_image():
    if request.method == 'POST':
        image = request.files['uploadedImage']

        if image.filename == "":
            return
        
        image_name = image.filename

        processor = model.ProcessImage(image, image_name)
        extracted_words = processor.detect_text()
        extracted_text = ' '.join(extracted_words)

        audio = processor.text_to_speech(extracted_text)

        return render_template('processed.html',extracted_text=extracted_text)
