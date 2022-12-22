# aws-ml-exercise
 AWS exercise that makes use of Rekognition and Polly.

app.py -> main python flask web application  
model.py -> makes use of AWS services to process the image  

# HOW TO USE
Create an AWS CLI IAM with __AmazonPollyFullAccess__ and __AmazonRekognitionFullAccess__.  
Pip install boto3 and flask for Python.  
Go in a console to the main file and enter __$ flask run__  
Go to the link that Flask is running on, example: "http://127.0.0.1:5000/"  
Upload a picture (.jpg or .jpeg) with text like a quote, upload on the web application and submit!
