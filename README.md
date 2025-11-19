# FastAPI SQLAlchemy Learning Project

This repository contains the work I did while learning how to connect a database with FastAPI using SQLAlchemy and how to handle database migrations using Alembic. It includes basic CRUD operations, database models, Pydantic schemas, and a simple project structure to understand how backend systems work.

## What This Project Covers

- Setting up SQLAlchemy with FastAPI
- Configuring the database engine and session
- Creating SQLAlchemy models (User, Product)
- Creating Pydantic request and response models
- Implementing CRUD APIs using FastAPI
- Learning how Alembic handles database migrations
- Understanding schema versioning and upgrade/downgrade flow
- Practicing real backend development workflow

## Folder Structure (Simple Overview)

app/
  database/
    databaseconnector.py
    databaseschema.py
  features/
    UserManagment/
      Userschema.py
      UserRoutes.py
  alembic/
    versions/
main.py

## How to Run the Project

1. Install dependencies:
   pip install -r requirements.txt

2. Initialize Alembic (only if running for the first time):
   alembic init alembic

3. Apply migrations:
   alembic upgrade head

4. Start the FastAPI server:
   uvicorn main:app --reload

5. Open API documentation in the browser:
   http://127.0.0.1:8000/docs

## CRUD Endpoints Included

- Create a user
- Get a user by ID
- Get all users
- Update a user
- Delete a user

Each endpoint uses SQLAlchemy for database operations and Pydantic for request/response validation.

## Purpose of This Repository

This repository is mainly for learning purposes. It helped me understand:

- How FastAPI handles incoming requests
- How SQLAlchemy interacts with the database
- How Alembic tracks and applies schema changes
- How to maintain a clean backend project structure

It also helps me present my learning progress clearly to my team lead.

