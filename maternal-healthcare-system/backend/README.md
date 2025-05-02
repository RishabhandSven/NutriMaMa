# Maternal Healthcare System Backend

This document provides an overview of the backend component of the Maternal Healthcare System project, which is designed to improve maternal healthcare in rural India.

## Overview

The backend is built using FastAPI, a modern web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed to handle emergency alerts and user logs from ASHA workers in rural areas.

## Features

- **Emergency Alert API**: Allows ASHA workers to submit emergency alerts for patients.
- **User Log API**: Enables logging of patient vitals such as blood pressure and weight.
- **FHIR Compliance**: All data is validated against FHIR standards to ensure interoperability.

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd maternal-healthcare-system/backend
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.7+ installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   You can start the FastAPI application using:
   ```
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Access the API Documentation**:
   Once the server is running, you can access the interactive API documentation at `http://localhost:8000/docs`.

## API Endpoints

- **POST /alert**: Submit an emergency alert.
- **POST /log**: Log user vitals.

## Deployment

The backend can be containerized using Docker. Refer to the `Dockerfile` for instructions on building the Docker image.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.