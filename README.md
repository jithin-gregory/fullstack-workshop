# Fullstack Workshop Backend

## Overview

This is the Demo app developed during the Full Stack Workshop using Python FastAPI. It has a predefined folder structure and features various components like routers, services, models, and more.

## Folder Structure

- **src**: The source directory containing all project code.
  - **main.py**: Entry point of the application.
  - **document**: Database documents or schemas.
  - **middlewares**: Middleware components for the application.
  - **model**: Request and response models.
  - **repositories**: Data access layer or repositories.
  - **routers**: API routers.
  - **services**: Business logic layer or services.
  - **utils**: Utility functions or helpers.
- **requirements.txt**: List of Python dependencies required for the project.

## Setup

1. Clone the repository: `git clone https://github.com/jithin-gregory/fullstack-workshop.git`
2. Navigate to the project directory: `cd fullstack-workshop`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

## Running the Application

To run the FastAPI application, execute the following command:

```bash
python ./src/main.py
```

This command starts the server and enables automatic reloading on code changes.

## Swagger Documentation

After starting the server, you can access the Swagger documentation at http://localhost:8000/docs. Swagger provides a user-friendly interface to interact with and test the API endpoints.

## Contributors
- Jithin Gregory
- Jemshith T K
- Mohammed Hafiz
- Prince Martin

## Have Fun Learning!

We hope you enjoy the Full Stack Workshop and find this project helpful in your journey to becoming a full-stack developer!