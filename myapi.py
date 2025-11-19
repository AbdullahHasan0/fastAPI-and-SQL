
from pydantic import BaseModel, Field

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from pydantic import BaseModel, Field
from typing import Optional, List

from databaseschema import Base

from User import DatabaseConector

database_url = "sqlite:///users.db"
db_connector = DatabaseConector(database_url)





## API Endpoints
@app.get("/")
def root():
    return {"message": "Welcome to the User Management API"}

@app.get("/users/{user_id}", response_model=UserResponse)
def get_users(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db : Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(User).filter(User.phno == user.phno).first():
        raise HTTPException(status_code=400, detail="Phone number already registered")
    
    ## Create User
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.put('/users/{user_id}', response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for key, value in user.model_dump().items():
        setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete('/users/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    name = db_user.name
    user = db_user.id
    print(name,user, "<--- HELLLO")
    db.delete(db_user)
    db.commit()
    # db.refresh(db_user)
    return {"message": f"User '{name}' with id '{user}' has been deleted."}
    # return {"message": f"User has been deleted."}

@app.get('/users/', response_model=List[UserResponse])
def get_all_users(db:Session = Depends(get_db)):
    users = db.query(User).all()
    return users