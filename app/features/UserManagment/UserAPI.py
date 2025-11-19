
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from typing import List

from app.database.databaseconnector import DatabaseConector

from app.features.UserManagment.userschema import UserCreate as UCreate , UserResponse as UResp
from app.database.databaseschema import User


database_url = "sqlite:///users.db"
db_connector = DatabaseConector(database_url)



router = APIRouter()




## API Endpoints
@router.get("/")
def root():
    return {"message": "Welcome to the User Management API"}

@router.get("/users/{user_id}", response_model=UResp)
def get_users(user_id: int, db: Session = Depends(db_connector.get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users/", response_model=UResp)
def create_user(user: UCreate, db : Session = Depends(db_connector.get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(User).filter(User.phno == user.phno).first():
        raise HTTPException(status_code=400, detail="Phone number already registered")
    
    ## Create User
    new_user = User(**user.model_dump())
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Unique constraint violated") from e
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="failed to create user") from e
    
    return new_user

@router.put('/users/{user_id}', response_model=UResp)
def update_user(user_id: int, user: UCreate, db: Session = Depends(db_connector.get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for key, value in user.model_dump().items():
        setattr(db_user, key, value)
    
    try:
        db.commit()
        db.refresh(db_user)

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Unique constraint violated") from e
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to update user") from e
    
    return db_user

@router.delete('/users/{user_id}')
def delete_user(user_id: int, db: Session = Depends(db_connector.get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    name = db_user.name
    user = db_user.id

    db.delete(db_user)
    try:
        db.commit()

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to delete user") from e
    
    return {"message": f"User '{name}' with id '{user}' has been deleted."}

@router.get('/users/', response_model=List[UResp])
def get_all_users(db:Session = Depends(db_connector.get_db)):
    users = db.query(User).all()
    return users

