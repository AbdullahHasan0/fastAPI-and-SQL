# FastAPI SQLAlchemy Learning Project

This repository contains the work I did while learning how to connect a database with FastAPI using SQLAlchemy and how to handle database migrations using Alembic. It includes CRUD operations, database models, Pydantic schemas, product management, and a simple project structure to understand how backend systems work.

## What This Project Covers

- Setting up SQLAlchemy with FastAPI
- Configuring the database engine and session
- Creating SQLAlchemy models (User, Product)
- Adding a quantity field to the Product model
- Creating Pydantic request and response models
- Implementing CRUD APIs for Users and Products
- Using Alembic to manage database migrations
- Understanding upgrade and downgrade migrations
- Maintaining a clean backend project structure

## Folder Structure (Simple Overview)

app/
  database/
    databaseconnector.py
    databaseschema.py
  features/
    UserManagment/
      Userschema.py
      UserRoutes.py
    ProductManagment/
      Productschema.py
      ProductRoutes.py
  alembic/
    versions/
main.py

## How to Run the Project

1. Install dependencies:
  ```bash
  pip install -r requirements.txt
```
2. Initialize Alembic (only for first-time setup):
   ```bash
   alembic init alembic
```
3. Apply migrations:
```bash
   alembic upgrade head
```
4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
```

5. Open API documentation:
```bash
   http://127.0.0.1:8000/docs
```

## CRUD Endpoints Included

User Management:
- Create a user
- Get user by ID
- Get all users
- Update user
- Delete user

Product Management:
- Create a product
- Get product by ID
- Get all products
- Includes quantity field in the Product table

## Purpose of This Repository

This project helped me understand how FastAPI interacts with SQLAlchemy, how database sessions work, how to structure backend modules, and how to manage schema changes using Alembic migrations. It also serves as a reference for building clean and scalable backend APIs.
