Your task is to analyze a log file, and extract all the json strings it contains to array.
The file is in s3.
Assume that the log file timestamps can be from any date and time.

----------
import base64

aws_access_key_id = base64.b64decode("_______________________=".encode()).decode() #fill your access key here
aws_secret_access_key = base64.b64decode("_________________________==".encode()).decode() #fill your secret key here

bucket_name = "___________" #fil the bucket name on AWS
key = "__________" #fill the name of file you want to download

# Your code here



