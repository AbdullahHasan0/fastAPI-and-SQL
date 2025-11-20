# app/__init__.py
from fastapi import FastAPI
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
    from app.features.Home.homeAPI import router as Home
    app.include_router(
        Home, 
        prefix=currentVersion,
        tags=["Home Route"]
    )

    from app.features.UserManagment.userAPI import router as User
    app.include_router(
        User, 
        prefix=currentVersion,
        tags=["User Management Route"]
    )
    
    from app.features.ProductManagment.productAPI import router as Product
    app.include_router(
        Product, 
        prefix=currentVersion,
        tags=["Product Management Route"]
    )
    return app