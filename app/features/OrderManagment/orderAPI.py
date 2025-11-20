from app.database.databaseschema import Order
from app.features.OrderManagment.orderschema import OrderCreate as OCreate, OrderResponse as OResp
from app.database.databaseconnector import DatabaseConector
from fastapi import HTTPException, APIRouter, Depends
from typing import List

DB_URL = "sqlite:///users.db"
connector = DatabaseConector(DB_URL= DB_URL)

get_db = connector.get_db
router = APIRouter()

@router.post("/orders/", response_model=OResp)
def create_order(order: OCreate, db=Depends(get_db)):
    db_order = Order(**order.model_dump())
    db.add(db_order)
    try:
        db.commit()
        db.refresh(db_order)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error creating order: " + str(e))
    return db_order

@router.get("/orders/{order_id}", response_model=OResp)
def get_order(order_id: int, db=Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.get("/orders/users/{user_id}", response_model=List[OResp])
def get_orders_by_user(user_id: int, db = Depends(get_db)):
    db_orders = db.query(Order).filter(Order.user_id == user_id).all()
    if not db_orders:
        raise HTTPException(status_code=404, detail="No orders found for this user")
    return db_orders

@router.get("/orders/", response_model=List[OResp])
def get_all_orders(db=Depends(get_db)):
    db_orders = db.query(Order).all()
    return db_orders