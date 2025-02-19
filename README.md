## AWS S3 AND IAM ##

## Introduction to Amazon S3

Amazon Simple Storage Service (Amazon S3) is an object storage service that offers scalability, security, performance, and data availability. It is designed to store and retrieve any amount of data from anywhere on the web. S3 is widely used for backup, data archiving, big data analytics, disaster recovery, and cloud-native application storage.

## Create an S3 Bucket

1.	Log in to the AWS Management Console.
2.	Navigate to S3 from the AWS services list.
3.	Click "Create Bucket".
4.	Enter a unique Bucket Name (e.g., demo-s3-bucket-123).
5.	Choose an AWS Region (e.g., us-west-2).
6.	Configure public access settings as required.
7.	Click "Create Bucket".
8.
9.	![image](https://github.com/user-attachments/assets/0e58bfac-e0b8-4b68-aa34-c49a7ef76954)

10.	![image](https://github.com/user-attachments/assets/3f3bc915-4ec7-4063-8fbe-cb6910cb930a)
11.	![image](https://github.com/user-attachments/assets/9839ed67-077b-4984-9ff4-14eacf911b8e)
12.
13.	![image](https://github.com/user-attachments/assets/c575f910-5304-451a-bf87-4ae6179842f3)
14.	
## Use Cases of AWS S3

•	Backup and Restore
•	Data Lakes.
•	Media Hosting
•	Static Website Hosting
•	Big Data Analytics

•	AWS S3 is a versatile and cost-effective storage service that integrates with many AWS tools for automation, security, and analytics. By leveraging features like versioning, lifecycle policies, and event notifications, users can efficiently manage their data while ensuring security and availability.

## Introduction to IAM

AWS Identity and Access Management (IAM) is a service that helps you securely control access to AWS resources. It allows you to manage who (users, groups, roles) can access what (AWS services and resources) under specific conditions.


## Uses of IAM

User Authentication & Authorization 
Create and manage users, assign permissions, and enforce least privilege access.

Secure Access to AWS Services 
Use IAM roles to grant permissions to AWS services like EC2, Lambda, and S3 without storing credentials.

Multi-Factor Authentication (MFA) 
Add an extra layer of security for user logins.

Granular Permission Control 
Use IAM policies to define fine-grained access control for users and services.

Federated Access & SSO 
Enable access via external identity providers like Google, Microsoft Active Directory, or Okta.

Temporary Security Credentials 
Use AWS STS (Security Token Service) to provide short-term credentials for applications.

Audit & Compliance –
Monitor access logs using AWS CloudTrail for security and compliance tracking.

Resource-Level Access 
Restrict access to specific AWS resources (e.g., certain S3 buckets or RDS instances).

![image](https://github.com/user-attachments/assets/324661b8-c172-4fcc-ae02-c050047431a1)
![image](https://github.com/user-attachments/assets/953e7c14-94cf-45c6-b43b-ac7bd82f8c20)

![image](https://github.com/user-attachments/assets/6be6f9f3-cfe0-4169-b60a-a532a86fa823)

![image](https://github.com/user-attachments/assets/8dd785b3-f0f9-46f0-8f9c-10faebba3ce0)


## Introduction to Lambda

AWS Lambda is a serverless computing service that allows you to run code without provisioning or managing servers. It automatically scales, runs code in response to events, and only charges for the compute time used.

# Key Features:

Event-driven execution – Triggers from AWS services like S3, DynamoDB, API Gateway, and CloudWatch.
Fully managed infrastructure – No need to manage servers or scaling.
Pay-per-use pricing – Billed only for execution time, down to milliseconds.
Supports multiple languages – Python, Node.js, Java, Go, C#, Ruby, etc.
Integrates with AWS services – Works with S3, DynamoDB, RDS, SNS, SQS, etc.
Secure and scalable – Handles thousands of concurrent executions.

# Use Cases

🔹 Automated backups & data processing (S3 file processing, ETL workflows)
🔹 API backends (via API Gateway + Lambda)
🔹 IoT & real-time processing (sensor data, logs, and analytics)
🔹 Chatbots & voice assistants
🔹 Security automation & compliance monitoring












