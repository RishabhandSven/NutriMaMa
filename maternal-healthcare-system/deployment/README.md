# Maternal Healthcare System Deployment Documentation

This document provides instructions for deploying the Maternal Healthcare System using Docker and Terraform. 

## Prerequisites

Before you begin, ensure you have the following installed:

- Docker
- Docker Compose
- Terraform
- Git

## Deployment Steps

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone <repository-url>
cd maternal-healthcare-system
```

### 2. Docker Deployment

#### Build and Run the Docker Containers

Navigate to the `deployment` directory and run the following command to build and start the Docker containers:

```bash
docker-compose up --build
```

This command will start the FastAPI backend and any other services defined in the `docker-compose.yml` file.

#### Accessing the Application

Once the containers are running, you can access the FastAPI application at `http://localhost:8000`.

### 3. Terraform Deployment

#### Configure Terraform

Navigate to the `deployment/terraform` directory and modify the `variables.tf` file to set your desired configuration values.

#### Initialize Terraform

Run the following command to initialize Terraform:

```bash
terraform init
```

#### Apply the Terraform Configuration

Deploy the infrastructure by running:

```bash
terraform apply
```

Follow the prompts to confirm the deployment. Terraform will provision the necessary resources based on the configuration defined in `main.tf`.

### 4. Stopping the Deployment

To stop the Docker containers, run:

```bash
docker-compose down
```

### 5. Cleanup

To destroy the resources created by Terraform, run:

```bash
terraform destroy
```

## Conclusion

This document outlines the steps to deploy the Maternal Healthcare System using Docker and Terraform. For further details on the backend API and mobile application, refer to their respective documentation files.