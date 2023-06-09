import json
import boto3

s3_client = boto3.client("s3")
sns_client = boto3.client("sns")
sns_topic_arn = "arn:aws:sns:us-west-2:689503057656:prime-numbers"


def lambda_handler(event, context):
    # bucket_name = 'prime-numbers-buck123'
    # file_key = 'prime_numbers.txt'
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    file_key = event["Records"][0]["s3"]["object"]["key"]

    s3_object = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    file_content = s3_object["Body"].read().decode("utf-8")
    # print(file_content)
    num_words = count_words(file_content)

    sns_client.publish(
        TopicArn=sns_topic_arn,
        Message="Success - The word count is: " + str(num_words),
        Subject="Lambda Function",
    )
    # return f'Number of primes is {num_words} in file {file_key} in the bucket {bucket_name}.'


def count_words(text):
    """returns the number of words in a file"""
    # with open(filename, "r") as file:
    #    contents = file.read()
    words = text.split()
    num_words = len(words)
    # print(f"Number of primes in the file: {num_words}")
    return num_words


