# Automated Backup System Using AWS S3 and Lambda

This repository contains an automated backup system that uses **AWS S3** and **AWS Lambda** to automatically copy files uploaded to one S3 bucket (source bucket) to another S3 bucket (backup bucket). This ensures that your data is automatically backed up every time a new file is added to the source bucket.

---

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

---

## Overview

This system automates the process of backing up files using AWS services. The Lambda function is triggered automatically whenever a new file is uploaded to the source S3 bucket. It then copies the file to a backup S3 bucket.

### Features:
- Automatically backs up any file uploaded to the source bucket.
- Uses AWS Lambda to handle the automation.
- Simple to set up and cost-effective.

---

## Architecture
![Untitled Diagram drawio(2)](https://github.com/user-attachments/assets/9cfb5c1f-9297-40ee-8062-e59b7d2e660c)
---

## Prerequisites

Before you begin, ensure you have the following:
- **AWS Account**: Set up with access to **AWS Lambda** and **S3**.
- **IAM Role with Permissions**: Create an IAM role that grants Lambda access to the S3 buckets.

---

## Setup Instructions

Follow these steps to set up the automated backup system:

### Step 1: Create AWS S3 Buckets

1. Go to the **S3 Console** in AWS.
2. **Create a Source Bucket**:
   - Click **Create Bucket** and give it a unique name (e.g., `my-source-bucket`).
   - Leave the default settings or adjust based on your requirements.
   - Click **Create**.
3. **Create a Backup Bucket**:
   - Repeat the above steps to create the backup bucket (e.g., `my-backup-bucket`).

### Step 2: Create Lambda Function

1. Go to the **Lambda Console** and click **Create Function**.
2. Choose **Author from Scratch**.
3. Give the function a name (e.g., `FileBackupLambda`).
4. Choose **Python 3.x** as the runtime (or another language if preferred).
5. Click **Create Function**.

### Step 3: Write Lambda Function Code
[Lambda function](lambda_function.py)

### Step 4: Set IAM Role Permissions

Your Lambda function needs permissions to interact with both the source and backup S3 buckets. Set up an **IAM Role** with the following policies:
- **AmazonS3ReadOnlyAccess**: Grants Lambda permission to read from the source bucket.
- **AmazonS3FullAccess**: Grants Lambda permission to write to the backup bucket.

To create an IAM role:
1. Go to the **IAM Console**.
2. Create a new role with the **Lambda** service as the trusted entity.
3. Attach the above policies to the role.
4. Assign the role to your Lambda function under the **Configuration** tab.

### Step 5: Configure S3 Event Notification

Set up an event notification to trigger the Lambda function when a new file is uploaded to the source bucket:
1. Go to the **S3 Console** and select your source bucket.
2. In the **Properties** tab, scroll down to **Event notifications**.
3. Click **Create event notification**.
4. Select **Lambda function** as the destination and choose your Lambda function (`FileBackupLambda`).
5. Set the event type to **All object create events**.

### Step 6: Test the System

To test the system:
1. Upload a file to your source S3 bucket.
2. Check your backup S3 bucket to confirm that the file was automatically copied.
3. View **AWS Lambda Logs** in **CloudWatch** to ensure the function executed correctly.

---

## Usage

Once the system is set up, any new file uploaded to the source bucket will automatically be copied to the backup bucket. You can monitor the Lambda function’s execution via **CloudWatch Logs** to track backups and any errors.

---

## Monitoring and Logs

1. Go to **CloudWatch Console**.
2. Select **Logs** and find the log group for your Lambda function.
3. Review the logs to check for successful backups or errors in execution.

---

### Notes:

- **Versioning**: You can enable versioning in the backup bucket to store multiple versions of the same file.
- **Notifications**: Configure additional notifications to alert you when backups are completed or if errors occur.
- **Encryption**: You can enable encryption on the backup bucket for enhanced security.

