import json
import boto3
from botocore.exceptions import ClientError

#from rekognition_image import RekognitionImage
#from rekognition_label import RekognitionLabel

rekognition_client = boto3.client('rekognition')
s3_client = boto3.client('s3')
sns_client = boto3.client('sns')
sns_topic_arn = 'arn:aws:sns:us-west-2:689503057656:prime-numbers'

def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="eu-west-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_labels(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		MaxLabels=max_labels,
		MinConfidence=min_confidence,
	)
	return response['Labels']

def lambda_handler(event, context):
    # bucket_name = 'prime-numbers-buck123'
    # file_key = '3683.webp'
    # for label in detect_labels(bucket_name, file_key):
	#     print("{Name} - {Confidence}%".format(**label))
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    # Create a RekognitionImage object using the S3 object
    image_data = {"S3Object": {"Bucket": bucket_name, "Name": file_key}}
    rekognition_image = RekognitionImage(image_data, file_key, rekognition_client)

    # Detect labels in the image
    max_labels = 10  # Set the maximum number of labels you want to return
    labels = rekognition_image.detect_labels(max_labels)
    
    

    # Convert the labels to a string representation
    #labels_str = json.dumps([label.to_dict() for label in labels])
    
    #print("Labels detected in image: " + labels_str)
    # Publish the labels to the SNS topic
    #sns_client.publish(
    #    TopicArn=sns_topic_arn,
    #    Message="Labels detected in image: " + labels_str,
    #    Subject='Lambda Function'
    #)
    return labels






import json
import boto3
from botocore.exceptions import ClientError

#from rekognition_image import RekognitionImage
#from rekognition_label import RekognitionLabel

rekognition_client = boto3.client('rekognition')
s3_client = boto3.client('s3')
sns_client = boto3.client('sns')
sns_topic_arn = 'arn:aws:sns:us-west-2:689503057656:prime-numbers'

def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="us-west-2"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_labels(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		MaxLabels=max_labels,
		MinConfidence=min_confidence,
	)
	return response['Labels']

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    #bucket_name = 'prime-numbers-buck1234'
    #file_key = 'cat.jpg'
    labellist = detect_labels(bucket_name, file_key)
    #for label in labellist:
     #   string = "{Name} - {Confidence}%".format(**label)
    print(labellist)
    return labellist