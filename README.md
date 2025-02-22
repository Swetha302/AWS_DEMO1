## AWS S3,IAM,RDS,ATHENA,GLUE AND ECS

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
	
    * CREATING A BUCKET *
  	
	![image](https://github.com/user-attachments/assets/0e58bfac-e0b8-4b68-aa34-c49a7ef76954)

    * FILE UPLOAD *

  	![image](https://github.com/user-attachments/assets/3f3bc915-4ec7-4063-8fbe-cb6910cb930a)

   * CREATING IAM USER *
   
	![image](https://github.com/user-attachments/assets/9839ed67-077b-4984-9ff4-14eacf911b8e)
 

    * USER ACCESS KEY *
 
	![image](https://github.com/user-attachments/assets/c575f910-5304-451a-bf87-4ae6179842f3)
 


## Use Cases of AWS S3

1.Backup and Restore

2.	Data Lakes.

3.	Media Hosting
   
4.	Static Website Hosting
	
5.	Big Data Analytics

•	AWS S3 is a versatile and cost-effective storage service that integrates with many AWS tools for automation, security, and analytics. By leveraging features like versioning, lifecycle policies, and event notifications, users can efficiently manage their data while ensuring security and availability.

## Introduction to IAM

AWS Identity and Access Management (IAM) is a service that helps you securely control access to AWS resources. It allows you to manage who (users, groups, roles) can access what (AWS services and resources) under specific conditions.

## Why Use IAM

1.Security & Access Control

2.Granular Permissions 

3.Multi-Factor Authentication (MFA) 

4.Identity Federation

5.AWS Service Integration 

6.Fine-Grained Policies 

7.Temporary Credentials 

8.Compliance & Auditing 

9.Secure Cross-Account Access 


## Uses of IAM

**User Authentication & Authorization** 

Create and manage users, assign permissions, and enforce least privilege access.


**Secure Access to AWS Services** 

Use IAM roles to grant permissions to AWS services like EC2, Lambda, and S3 without storing credentials.

**Multi-Factor Authentication (MFA)**

Add an extra layer of security for user logins.

**Granular Permission Control** 

Use IAM policies to define fine-grained access control for users and services.

**Federated Access & SSO**

Enable access via external identity providers like Google, Microsoft Active Directory, or Okta.

**Temporary Security Credentials** 

Use AWS STS (Security Token Service) to provide short-term credentials for applications.

**Audit & Compliance**

Monitor access logs using AWS CloudTrail for security and compliance tracking.

**Resource-Level Access** 

Restrict access to specific AWS resources (e.g., certain S3 buckets or RDS instances).

* CREATING THE USER *


![image](https://github.com/user-attachments/assets/324661b8-c172-4fcc-ae02-c050047431a1)


* SECURITY CREDENTIALS *

![image](https://github.com/user-attachments/assets/953e7c14-94cf-45c6-b43b-ac7bd82f8c20)

* CREATING USER GROUP AND PERMISSIONS NOT DEFINED *

![image](https://github.com/user-attachments/assets/6be6f9f3-cfe0-4169-b60a-a532a86fa823)

* AFTER THE ACCESS PERMISSIONS DEFINED *

![image](https://github.com/user-attachments/assets/8dd785b3-f0f9-46f0-8f9c-10faebba3ce0)


# Introduction to RDS

Amazon RDS (Relational Database Service) is a managed database solution by AWS that simplifies setting up, operating, and scaling relational databases in the cloud. It supports multiple database engines like MySQL, PostgreSQL, MariaDB, SQL Server, Oracle, and Amazon Aurora, offering high availability, automatic backups, security, and performance monitoring. With features like Multi-AZ deployments, read replicas, and automated maintenance, RDS ensures reliability and scalability without requiring manual database administration. It is cost-effective, allowing businesses to pay on demand or reserve instances for better pricing while focusing on application development instead of infrastructure management.

### Uses of Amazon RDS (Key Points) 

**Automated Database Management** – Handles backups, patching, and maintenance automatically.  

**Scalability** – Easily scales up or down based on workload demands.  

**High Availability** – Supports Multi-AZ deployments for failover and disaster recovery.  

**Security & Compliance** – Provides encryption, IAM integration, and compliance with industry standards.  

**Performance Optimization** – Supports read replicas, caching, and tuning for high-speed queries.  

**Cost-Effective** – Pay-as-you-go pricing with reserved instance options for savings.  

**Multi-Database Support** – Works with MySQL, PostgreSQL, SQL Server, Oracle, and MariaDB.  

**Seamless AWS Integration** – Connects with AWS services like Lambda, S3, CloudWatch, and more.  

**Developer-Friendly** – Simplifies database setup and management for faster application deployment.  

**Disaster Recovery & Backups** – Ensures data safety with automated snapshots and point-in-time recovery.  


* CREATING DATABASE *
  
![Screenshot 2025-02-19 172957](https://github.com/user-attachments/assets/4ab7ac54-ae10-4d22-9bc4-1792dc744a39)


* THIS IS THE DATABASE *

![Screenshot 2025-02-19 173146](https://github.com/user-attachments/assets/08443109-0fd7-4799-bd23-957c082fafa2)


## INTRODUCTION TO ECS ##

# What is AWS  ECS #

Amazon Elastic Container Service (ECS) is a highly scalable, fully managed container orchestration service that allows users to run, stop, and manage Docker containers on a cluster of virtual machines. It eliminates the need to install, operate, and scale container orchestration software, making it easier to deploy and manage containerized applications.

# Core Components of AWS ECS #

Clusters – Logical group of EC2 instances or Fargate tasks.

Task Definitions – Defines how containers should run (CPU, memory, networking).

Tasks – A running instance of a task definition (single or multiple containers).

Services – Ensures that a specified number of tasks are running and manages scaling.

Container Agent – Runs on EC2 instances to manage container lifecycle.

Container Registry (ECR) – AWS-managed Docker container registry.


# Use Cases of AWS ECS #

Microservices and API hosting.

Batch processing workloads.

Machine learning model deployment.

Event-driven architecture with AWS Lambda and SQS.

Continuous integration and deployment (CI/CD) pipelines.

# Getting Started with AWS ECS #

Create an ECS Cluster – Choose Fargate or EC2 as the launch type. 

Define a Task Definition – Configure container settings, including image, CPU, memory, and networking.

Create a Service – Deploy tasks and manage scaling.

Set Up Load Balancing – Use ALB or NLB for traffic routing.

Monitor & Scale – Use CloudWatch for logging and auto-scaling.

 **THIS IS MY EC2**

![Screenshot 2025-02-22 010314](https://github.com/user-attachments/assets/2b4f7b9d-0213-45b2-b3d9-2fff7a12e7d4)

![image](https://github.com/user-attachments/assets/a0613c58-ce92-4321-8e42-5027ebf89fe8)


![image](https://github.com/user-attachments/assets/4583ad0b-2da3-4e4e-aec4-2c0d456eac04)

**THIS IS MY ECS CLUSTER**

![Screenshot 2025-02-21 204835](https://github.com/user-attachments/assets/9da47fba-2342-4be5-8e1a-6823048ebc1c)

![Screenshot 2025-02-21 211527](https://github.com/user-attachments/assets/0e918fcd-f912-4b04-96ae-bd0c376e09c5)

![Screenshot 2025-02-21 211611](https://github.com/user-attachments/assets/73d0574b-60e8-48cf-a4f7-afec55b66a19)

![Screenshot 2025-02-21 211720](https://github.com/user-attachments/assets/f33c4710-2013-458a-aaff-fda6dd25e76f)

![Screenshot 2025-02-21 211905](https://github.com/user-attachments/assets/7d86c15b-2bcc-4616-953a-f366bd3d9087)

![Screenshot 2025-02-21 211905](https://github.com/user-attachments/assets/6f0a9b8d-fe07-4ff9-89a6-ec652488445e)



## INTRODUCTION TO ATHENA ##

# What is Amazon Athena #

Amazon Athena is a serverless, interactive query service that enables users to analyze data stored in Amazon S3 using standard SQL. It eliminates the need for setting up or managing databases and infrastructure, making it a cost-effective and easy-to-use solution for running queries on large datasets.

# Key Features of Amazon Athena #

**Serverless** – No infrastructure to manage; pay only for queries run.

**SQL Querying** – Uses standard SQL via Presto and Trino engines.

**Scalability** – Automatically scales to handle queries of any size.

**Secure** – Integrated with AWS IAM, AWS Lake Formation, and AWS Glue for fine-grained access control.

**Supports Multiple Data Formats** – Works with CSV, JSON, ORC, Avro, Parquet, and more.

**Integration with AWS Services** – Connects with AWS Glue for schema management, Quicksight for visualization, and CloudTrail for auditing.


# How Amazon Athena Works #

1. Store Data in Amazon S3 – Upload structured or semi-structured data to an S3 bucket.
   
2. Define Schema using AWS Glue – Use AWS Glue Data Catalog to create a schema for your data.

3. Run Queries using SQL – Write SQL queries to analyze the data directly from S3.

4. Pay for What You Use – Charges are based on the amount of data scanned per query.


# Use Cases of Amazon Athena #

1. Log Analysis – Query AWS service logs (e.g., CloudTrail, VPC Flow Logs).

2. Business Intelligence – Analyze large datasets without complex ETL processes.

3. Data Lake Querying – Query structured and unstructured data in Amazon S3.

4. Security & Compliance – Monitor and audit AWS activity logs efficiently.


![Screenshot 2025-02-21 224119](https://github.com/user-attachments/assets/a00d90e8-7715-42a2-a166-4fe30037f18c)

![Screenshot 2025-02-21 225719](https://github.com/user-attachments/assets/4068853e-e1e0-4f1e-a726-060f637e0dec)

![Screenshot 2025-02-21 230321](https://github.com/user-attachments/assets/afd491ce-b1ed-4083-aa09-3434f896db92)

![Screenshot 2025-02-21 230333](https://github.com/user-attachments/assets/54a91147-b797-46c1-a621-68b58742a754)







## INTRODUCTION TO GLUE ##

# What is AWS Glue #

AWS Glue is a serverless data integration service that automates ETL (Extract, Transform, Load) processes, making it easier to prepare and manage data for analytics, machine learning, and reporting.

# Key Features of AWS Glue

1. Serverless – No infrastructure management; scales automatically.

2. Automated Data Discovery – Uses Crawlers to scan and classify data sources.

3. AWS Glue Data Catalog – Centralized metadata repository for schema management.

4. ETL (Extract, Transform, Load) Processing – Supports PySpark, Python, and Spark SQL for data transformation.

5. Multiple Data Format Support – Works with CSV, JSON, Parquet, Avro, ORC, etc.

6. Integration with AWS Services – Works with S3, Redshift, Athena, DynamoDB, Lake Formation, etc.

7. Secure & Compliant – Integrated with IAM, VPC, and KMS for encryption and access control.

# How AWS Glue Works

1. Data Discovery & Crawling – Crawlers scan and infer schemas from S3, RDS, Redshift, DynamoDB, and other sources.

2. Metadata Management – Stores schema details in the Glue Data Catalog for easy access.

3. ETL Job Creation – AWS Glue generates PySpark-based ETL scripts to clean, transform, and enrich data.

4. Data Loading & Querying – Transformed data is loaded into S3, Redshift, RDS, DynamoDB, and queried via Athena, QuickSight, or Redshift Spectrum.

# Use Cases of AWS Glue

1. Data Lake Management – Process and organize data for analytics.

2. ETL Pipelines – Automate data extraction, transformation, and loading.

3. Big Data Processing – Handle large-scale data transformations.

4. Machine Learning Data Preparation – Clean and structure data for ML models.

5. Log & Security Analytics – Process and analyze logs from CloudTrail, VPC, and other sources.
   

![Screenshot 2025-02-21 225719](https://github.com/user-attachments/assets/97f04574-22b4-43b3-abed-bc59885bc527)

![Screenshot 2025-02-21 230604](https://github.com/user-attachments/assets/a88dbf2d-6c5a-425d-b607-298d267db514)

![Screenshot 2025-02-21 230626](https://github.com/user-attachments/assets/98f7674f-f5e8-4283-8fe5-3ad26988b37e)

![Screenshot 2025-02-21 230650](https://github.com/user-attachments/assets/d8ddc783-f5db-4b41-bd8b-f568654b6d67)

![Screenshot 2025-02-21 232103](https://github.com/user-attachments/assets/fd4180f1-9eeb-4340-9e3c-bf59dd56ee3c)







   
































