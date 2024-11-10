# Automated Backup System Using AWS S3 and Lambda 🚀

This repository contains an automated backup system that uses **AWS S3** and **AWS Lambda** to automatically copy files uploaded to one S3 bucket (source bucket) to another S3 bucket (backup bucket). This ensures your data is safely backed up every time a new file is added! 🔄

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Step 1: Create AWS S3 Buckets](#step-1-create-aws-s3-buckets)
  - [Step 2: Create Lambda Function](#step-2-create-lambda-function)
  - [Step 3: Write Lambda Function Code](#step-3-write-lambda-function-code)
  - [Step 4: Set IAM Role Permissions](#step-4-set-iam-role-permissions)
  - [Step 5: Configure S3 Event Notification](#step-5-configure-s3-event-notification)
  - [Step 6: Test the System](#step-6-test-the-system)
- [Usage](#usage)
- [Monitoring and Logs](#monitoring-and-logs)

## Overview 🌟

This system automates file backups using AWS services. The **Lambda** function is triggered automatically whenever a new file is uploaded to the source S3 bucket, and it copies the file to the backup bucket.

### Features:
- 🚀 Automatically backs up files uploaded to the source bucket.
- 🧑‍💻 Uses AWS Lambda for automation.
- 💸 Cost-effective and easy to set up.

## Architecture 🏗️
![System Architecture](https://github.com/user-attachments/assets/9cfb5c1f-9297-40ee-8062-e59b7d2e660c)

## Prerequisites 🛠️

Before you begin, ensure you have:
- **AWS Account** with access to **AWS Lambda** and **S3**.
- **IAM Role** with permissions for Lambda to access S3.

## Setup Instructions 📝

Follow these steps to set up the automated backup system:

### Step 1: Create AWS S3 Buckets 🪣

1. Go to the **S3 Console** in AWS.
2. Create a **Source Bucket** (e.g., `my-source-bucket`).
3. Create a **Backup Bucket** (e.g., `my-backup-bucket`).

### Step 2: Create Lambda Function 🖥️

1. Go to the **Lambda Console** and click **Create Function**.
2. Choose **Author from Scratch**.
3. Name your function (e.g., `FileBackupLambda`).
4. Select **Python 3.x** as the runtime.
5. Click **Create Function**.

### Step 3: Write Lambda Function Code ✍️
[Lambda function](lambda_function.py)

### Step 4: Set IAM Role Permissions 🔑

Create an **IAM Role** with these permissions:
- **AmazonS3ReadOnlyAccess**: Access to the source bucket.
- **AmazonS3FullAccess**: Write permissions for the backup bucket.

Assign the role to your Lambda function.

### Step 5: Configure S3 Event Notification 🔔

Set up an event to trigger Lambda when a new file is uploaded:
1. Go to the **S3 Console** and select your source bucket.
2. Under **Properties**, find **Event notifications**.
3. Create a new event notification and select **Lambda function** as the destination.
4. Choose your Lambda function (`FileBackupLambda`).
5. Set the event type to **All object create events**.

### Step 6: Test the System ✅

1. Upload a file to your source bucket.
2. Check the backup bucket for the file.
3. View **AWS Lambda Logs** in **CloudWatch** to verify everything is working!

## Usage ⚙️

Once set up, any new file uploaded to the source bucket is automatically copied to the backup bucket. Monitor the Lambda function's execution via **CloudWatch Logs**.

## Monitoring and Logs 📊

1. Go to **CloudWatch Console**.
2. Find the **Logs** section and locate your Lambda function’s log group.
3. Review logs to track successful backups or any errors.

### Notes:
- **Versioning**: Enable versioning in the backup bucket for multiple file versions.
- **Notifications**: Set up notifications to alert you about backup success or errors.
- **Encryption**: Consider enabling encryption on your backup bucket for extra security.
