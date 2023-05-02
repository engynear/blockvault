import os

from botocore.utils import fix_s3_host
import boto3

os.environ['AWS_ACCESS_KEY_ID'] = "accessKey1"
os.environ['AWS_SECRET_ACCESS_KEY'] = "verySecretKey1"

s3 = boto3.resource(service_name='s3', endpoint_url='http://localhost:8000')
s3.meta.client.meta.events.unregister('before-sign.s3', fix_s3_host)

for bucket in s3.buckets.all():
    print(bucket.name)

client = s3.meta.client
client.create_bucket(Bucket='modelpreview')
#удаление бакета modelPreview
# client.delete_bucket(Bucket='model1')

s3.meta.client.upload_file('preview.png', 'modelpreview', '1.png')
s3.meta.client.upload_file('buran.png', 'modelpreview', '2.png')

#s3 write file by key models/1/preview.png to variable and return it
# obj = s3.Object('bucket1', 'models/1/preview.png')
# body = obj.get()['Body'].read()
# print(body)




# s3.meta.client.upload_file('test2.txt', 'bucket1', 'test2.txt')
# s3.meta.client.upload_file('test3.txt', 'bucket1', 'test3.txt')
# s3.meta.client.upload_file('test4.txt', 'bucket1', 'test4.txt')
# s3.meta.client.upload_file('test5.txt', 'bucket1', 'test5.txt')
# s3.meta.client.upload_file('test6.txt', 'bucket1', 'test6.txt')
# s3.meta.client.upload_file('test7.txt', 'bucket1', 'test7.txt')
