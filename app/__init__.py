# app/__init__.py
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app():
    app = FastAPI(title="Integration With SQLAlchemy")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allow all origins for development purposes
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    currentVersion = "/api/v1"

    # Register Routes
    from app.features.UserManagment.UserAPI import router as User
    app.include_router(
        User, 
        prefix=currentVersion,
        tags=["User Management Route"]
    )
    
    return app