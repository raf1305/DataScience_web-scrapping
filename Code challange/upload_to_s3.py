import boto3
import pandas as pd

s3=boto3.client('s3')
s3.create_bucket(bucket='corona')

with open('testfile.txt','r') as f:
    content=f.read()
s3.upload_file('testfile.txt','corona','test_1_s3.txt')

with open('final.csv','r') as f:
    content = f.read()
s3.putobject(Body=content,Bucket='corona',key='s3_given_access_key.csv')
