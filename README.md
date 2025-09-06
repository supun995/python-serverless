# python-serverless

A serverless application built with **AWS SAM (Serverless Application Model)** and Python.  

---

## 🚀 Build and Deploy

To build the application:

```bash
sam build
```bash
To deploy:
```bash
sam deploy
```bash
For the first-time deployment (guided mode):
```bash
sam deploy --guided
```bash
```bash
<!-- Example of packaging before deployment: ```bash sam package \ --template-file template.yml \ --output-template-file package.yml \ --s3-bucket amzn-s3-demo-bucket ``` -->
```bash

## 🧪 Local Testing

Start the local API:
```bash
sam local start-api
```bash

Start a local Lambda function:

```bash
sam local start-lambda```bash
