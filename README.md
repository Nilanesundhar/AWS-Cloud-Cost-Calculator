### AWS Cloud Cost Calculator

Cloud cost calculator is a simple and interactive web-based cost estimation tool built using HTML, CSS and JavaScript hosted on Amazon S3 as a static website. It allows users to select AWS services like EC2, S3 and Data Transfer, input usage and calculate an estimated monthly cost instantly.


### Features

* User-friendly interface built with HTML, CSS, and JavaScript.
* Dropdown-based service selection (EC2, S3, Lambda, DynamoDB).
* Allows users to enter custom usage values.
* Instantly calculates estimated monthly costs.
* Deployed on Amazon S3 static website hosting for global access.


### Technologies used

* Amazon S3 → Hosts the static website (index.html)
* IAM Policy → Grants public read-only access for website visitors
* API Gateway + AWS Lambda → Used for dynamic pricing retrieval
* CloudWatch → Monitor access logs and performance
* Dynamo DB → used for database

### Architecture Diagram


User Browser  →  Amazon S3 (Static Website)
                        ↓
                 IAM Policy for Access
                        ↓
                 API Gateway → AWS Lambda


### Tech Stack

* Frontend: HTML, CSS, JavaScript
* Hosting : AWS S3 Static Website
* Security: AWS IAM Policy
* Backend : Lambda, API Gateway

### Work Flow

* User accesses the S3-hosted website via a public endpoint.
* User selects AWS service and usage type.
* JavaScript performs the cost calculation on the client side.
* The result displays instantly — showing individual service costs and total monthly estimate. 

### Future Enhancements

* Fetch real-time AWS pricing using AWS Pricing API
* Add RDS, DynamoDB, CloudFront service options
* Include data visualization charts for cost breakdown
* Store user inputs using AWS DynamoDB

### Developer

Nilani S
