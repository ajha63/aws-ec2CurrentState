# aws-ec2CurrentState
A AWS Lambda function to send a SNS notification with EC2 current State  of a list of ec2 instance ID

To implement this lambda function do you need:

   1. Use python 3.6 or pyhton 3.7 to create lambda function
   2. Define an IAM lambda role with SNS, EC2, and CloudWatch. You can see an example on ec2CurrentState-policies.json
   3. Define a SNS topic and subscription
   4. Define environment variables:
      4.1 Key:: ARNTopic, Value: arn:topic
      4.2 Key:: EC2Instances, Value: list of instance ID separated by commas without spaces
      4.3 Key:: Message, Value: Message body to sns message
      4.4 Key:: MessageSubject, Value: Subject to sns message

>Author: Alvaro Hernandez <alvaro@escala24x7.com>

[![@ajha63](https://upload.wikimedia.org/wikipedia/commons/6/61/DevelopByAjha63.png)](https://github.com/ajha63/aws-ec2CurrentState)

[Alvaro Hernandez]: <by.ajha.work>
[@ajha63]: <https://twitter.com/ajha63>
