import base64
import json
from boto3.session import Session
import gzip

aws_access_key_id = base64.b64decode("_______________________=".encode()).decode() #fill your access key here
aws_secret_access_key = base64.b64decode("_________________________==".encode()).decode() #fill your secret key here

bucket_name = "___________" #fil the bucket name on AWS
key = "__________" #fill the name of file you want to download


# Your code here
session = Session(aws_access_key_id,
              aws_secret_access_key)
file = session.resource('s3').Bucket(bucket_name).download_file(key, key)




json_strings = []
with open(key, 'rb') as f:
    serial = gzip.decompress(f.read())
    jdata = serial.decode('utf-8')


stack = []
index_of_first_char = 0
index_of_last_char = 0
for i in range (len(jdata)):
    if jdata[i] == '{': 
        if not stack:
            index_of_first_char = i
        stack.append(jdata[i])
    if jdata[i] == '}':
        stack.pop()
        if not stack:
            index_of_last_char = i + 1
            object = json.loads(jdata[index_of_first_char : index_of_last_char])
            json_strings.append(object)