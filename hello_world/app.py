import json,requests,boto3

from aws_xray_sdk.core import xray_recorder,patch_all
patch_all()


def lambda_handler(event, context):
	s3 = boto3.client('s3')

	ip = requests.get("http://ipinfo.io/ip")
	response = s3.list_buckets()
	return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "location": ip.text.replace("\n", ""),
            "buckets": [x["Name"] for x in response["Buckets"]]
        }),
	}
