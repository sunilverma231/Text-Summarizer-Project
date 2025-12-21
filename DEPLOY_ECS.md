# Deploy to AWS ECS (Fargate)

This guide shows how to build, push, and run the FastAPI service on ECS Fargate using Amazon ECR.

## Prerequisites
- AWS CLI configured (`aws configure`)
- An AWS account with permissions for ECR/ECS/IAM
- Docker installed locally

## 1) Create an ECR Repository
```bash
aws ecr create-repository --repository-name text-summarizer --region us-east-1
URI: 474369734726.dkr.ecr.eu-north-1.amazonaws.com/text-s
```
Capture the repository URI (e.g., `ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/text-summarizer`).

## 2) Authenticate Docker to ECR
```bash
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com
```

## 3) Build and Push Image
```bash
# From project root
docker build -t text-summarizer:latest .

docker tag text-summarizer:latest ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/text-summarizer:latest

docker push ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/text-summarizer:latest
```

## 4) Create ECS Task Definition (Fargate)
Use the following container settings:
- Image: `ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/text-summarizer:latest`
- CPU/Memory: e.g., `0.5 vCPU / 1 GB`
- Port mappings: `8000/tcp`
- Command (optional): leave default (Dockerfile CMD uses Gunicorn)
- Environment:
  - `PORT=8000`
- Health check: `CMD-SHELL curl -f http://localhost:8000/ || exit 1`

Enable `awslogs` for container logs:
- Log driver: `awslogs`
- Options: `awslogs-group`, `awslogs-region`, `awslogs-stream-prefix`

## 5) Create ECS Service
- Launch type: `Fargate`
- Desired tasks: `1` (scale later as needed)
- Networking: place in a public or private subnet with an ALB
- If using an Application Load Balancer:
  - Target group: HTTP, port 8000, health check `/`
  - Listener: `:80` → forward to target group

## 6) Test
Once the service is running behind the ALB, test the endpoint:
```
GET http://<ALB-DNS-Name>/
POST http://<ALB-DNS-Name>/predict
```

## Notes
- The image uses Gunicorn with Uvicorn workers for production.
- If your app needs local model artifacts, bake them into the image (remove from `.dockerignore`) or mount via EFS.
- For better performance, increase Gunicorn workers based on task CPU.
- To restrict outbound internet, ensure models/tokenizers are bundled in the image or available via EFS/S3.
