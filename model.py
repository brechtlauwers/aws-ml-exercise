import boto3
from botocore.exceptions import ClientError

class ProcessImage:
    def __init__(self, image, image_name):
        self.image = image
        self.image_name = image_name

    def detect_text(self):
        texts = list()

        session = boto3.Session()
        client = session.client('rekognition', "eu-west-1")

        try:
            response = client.detect_text(Image={'Bytes': self.image.read()})
            detection = response['TextDetections']

            for text in detection:
                if text["Type"] == "WORD":
                    texts.append(text["DetectedText"])

            print(f"Found {len(texts)} texts in {self.image_name}")

        except ClientError:
            print(f"Couldn't detect text in {self.image_name}")
            texts = "No text found in this image"
        else:
            return texts


    def text_to_speech(self, image_text):
        session = boto3.Session()
        client = session.client('polly', "eu-west-1")
        
        try:            
            response = client.synthesize_speech(Text=image_text, 
            OutputFormat="mp3", VoiceId="Matthew")
            
        except ClientError as error:
            print(error)

        if "AudioStream" in response:
            audio = response['AudioStream'].read()

            file_name ='static/converted_text.mp3'

            with open(file_name, 'wb') as file:
                file.write(audio)
            
            return
