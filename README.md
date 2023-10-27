# lambdatuning

This repository contains Python code to create a Lambda function to generate prime numbers up to a specified limit. Once the Lambda function is created, you can use it with the Lambda Power Tuning tool.

Directions:
1. Install the [Lambda Power Tuning tool](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:451282441545:applications~aws-lambda-power-tuning) in an AWS account in a region of your choice. The tool is well documented [here.](https://github.com/alexcasalboni/aws-lambda-power-tuning/blob/master/README.md) This will create a state machine using Step Functions.
2. Clone this repository to your local machine. This should download the Zip file that contains the deployment package.
3. Log into your AWS management console, make sure you are in the same region where the Lambda Power Tuning Tool state machine is deployed.
4. Navigate to the Lambda service console.
5. Create a new Lambda function by clicking the `Create function` button.
6. Select `Author from scratch`
7. Give your function a name.
8. Choose Python 3.11 as the runtime.
9. Click `Create function`
10. Once the function is created, click on the `Code` tab and click the `Upload from` button on the right.
11. Select `.zip file`, then select `Upload`.
12. In the pop-up file menu, select the `lambda_function.zip` Zip file you cloned in step 2.
13. Click `Save`. This will create your Lambda function.
14. To avoid timeouts during testing, set the function's timeout to 15 minutes.
15. Copy the Lambda function ARN and use that as an input to the state machine created in step 1 to run the Lambda Power Tuning tool.
16. You can optionally use `state_machine_input.json` file as the input too. Just make sure you edit it and add your Lambda function's ARN from step 14.
