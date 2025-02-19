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

# User Authentication & Authorization 
Create and manage users, assign permissions, and enforce least privilege access.

# Secure Access to AWS Services 
Use IAM roles to grant permissions to AWS services like EC2, Lambda, and S3 without storing credentials.

# Multi-Factor Authentication (MFA) 
Add an extra layer of security for user logins.

# Granular Permission Control 
Use IAM policies to define fine-grained access control for users and services.

# Federated Access & SSO 
Enable access via external identity providers like Google, Microsoft Active Directory, or Okta.

# Temporary Security Credentials 
Use AWS STS (Security Token Service) to provide short-term credentials for applications.

# Audit & Compliance –
Monitor access logs using AWS CloudTrail for security and compliance tracking.

# Resource-Level Access 
Restrict access to specific AWS resources (e.g., certain S3 buckets or RDS instances).

![image](https://github.com/user-attachments/assets/324661b8-c172-4fcc-ae02-c050047431a1)









