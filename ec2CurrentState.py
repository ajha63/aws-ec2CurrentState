# ec2CurrentState.py
import boto3
import os

ARNTOPIC = os.getenv("ARNTopic")
SUBJECT = os.getenv("MessageSubject")
MESSAGE = os.getenv("Message")
EC2INSTACES = os.getenv("EC2Instances")

def lambda_handler(event, context):
	# Get instance id
	instances = EC2INSTACES.split(",")
	for instance in instances:
		ec2State = checkEC2status(instance)
		ec2Name = getTagName(instance)
		subjectmsg = "{0} {1} State: {2}".format(SUBJECT, ec2Name['Name'], ec2State['Name'])
		messagebody = "{0} {1} ({2}) is on {3} State".format(MESSAGE, instance, ec2Name['Name'], ec2State['Name'])
		result = send_message(messagebody, subjectmsg, ARNTOPIC)
		print(messagebody)
	print(result)
	
def checkEC2status(instanceid):
	ec2 = boto3.resource('ec2')
	instance = ec2.Instance(instanceid)
	return(instance.state)

def getTagName(instanceid):
	ec2 = boto3.resource('ec2')
	instance = ec2.Instance(instanceid)
	ec2tags = {}
	for tag in instance.tags:
		ec2tags.update({tag['Key']:tag['Value']})
	if 'Name' in ec2tags:
		return({'Name': ec2tags['Name']})
	else:
		return({'Name': 'Not Name'})

def send_message(message, subject, arntopic):
	# create a sns client
	sns = boto3.client('sns')
	# Publish a simple message to the specified SNS topic
	response = sns.publish(
		TopicArn=arntopic,
		Subject=subject,
		Message="{0}".format(message),
	)
	return(response)
