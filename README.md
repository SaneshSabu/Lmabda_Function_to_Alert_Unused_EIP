
# Lmabda_Function_to_Alert_on_Unused_EIP
Lambda Function that finds and sends alert via SNS, Helps to have a check on billing.



## Usage

- Set SNS topic to alert unused EIP and create subscription.
- Upload the lambda function and attach role to the lambda function with sufficient permission to access the details of elastic IP and publish SNS alert.
