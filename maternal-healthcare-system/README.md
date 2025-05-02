# Maternal Healthcare System

This project aims to improve maternal healthcare in rural India by providing a comprehensive system for ASHA workers to log patient data and submit emergency alerts. The system consists of a FastAPI backend and a Flutter mobile application.

## Goals

- Enable ASHA workers to log vital patient information.
- Provide a mechanism for submitting emergency alerts.
- Ensure data compliance with FHIR standards.
- Utilize modern technologies for efficient data handling and user experience.

## Tech Stack

- **Backend**: FastAPI, Pydantic, Firebase Admin SDK, Redis
- **Mobile App**: Flutter
- **Deployment**: Docker, Terraform

## Project Structure

- **backend/**: Contains the FastAPI application.
  - **app/**: Main application code including routers, models, services, and utilities.
  - **Dockerfile**: Instructions for building the backend Docker image.
  - **requirements.txt**: Python dependencies for the backend.
  - **README.md**: Documentation for the backend.

- **mobile-app/**: Contains the Flutter application for ASHA workers.
  - **lib/**: Main application code including screens and services.
  - **pubspec.yaml**: Flutter project configuration.

- **deployment/**: Contains configuration files for deploying the application.
  - **docker-compose.yml**: Docker service definitions.
  - **terraform/**: Terraform configuration files for cloud deployment.
  - **README.md**: Documentation for the deployment process.

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Build the Docker image:
   ```
   docker build -t maternal-healthcare-backend .
   ```
3. Run the Docker container:
   ```
   docker run -d -p 8000:8000 maternal-healthcare-backend
   ```

### Mobile App

1. Navigate to the `mobile-app` directory.
2. Install dependencies:
   ```
   flutter pub get
   ```
3. Run the application:
   ```
   flutter run
   ```

### Deployment

1. Navigate to the `deployment` directory.
2. Use Docker Compose to start services:
   ```
   docker-compose up
   ```
3. Deploy using Terraform:
   ```
   terraform init
   terraform apply
   ```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or suggestions.