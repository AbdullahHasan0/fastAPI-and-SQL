from fastapi import APIRouter
from app.database.databaseconnector import DatabaseConector
from app.database.databaseschema import Order
from app.database.databaseschema import OrderItem
from app.database.databaseschema import Product
from app.features.OrderItemManagment.orderitemschema import OrderItemCreate as OICreate, OrderItemResponse as OIResp
from fastapi import HTTPException, Depends
from typing import List
from sqlalchemy.exc import IntegrityError

DB_URL = "sqlite:///users.db"

connector = DatabaseConector(DB_URL= DB_URL)
get_db = connector.get_db
router = APIRouter()

@router.post("/orderitems/", response_model=OIResp)
def create_order_item(order_item: OICreate, db=Depends(get_db)):
    if not db.query(Order).filter(Order.id == order_item.order_id).first():
        raise HTTPException(status_code=400, detail="Order does not exist")
    if not db.query(OrderItem).filter(Product.id == order_item.product_id).first():
        raise HTTPException(status_code=400, detail="Product does not exist")
    db_order_item = OrderItem(**order_item.model_dump())
    db.add(db_order_item)
    try:
        db.commit()
        db.refresh(db_order_item)
    except IntegrityError as ie:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error: " + str(ie))
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error creating order item: " + str(e))
    return db_order_item

@router.get("/orderitems/{order_item_id}", response_model=OIResp)
def get_order_item(order_item_id: int, db=Depends(get_db)):
    db_order_item = db.query(OrderItem).filter(OrderItem.id == order_item_id).first()
    if db_order_item is None:
        raise HTTPException(status_code=404, detail="Order item not found")
    return db_order_item

@router.get("/orderitems/orders/{order_id}", response_model=List[OIResp])
def get_order_items_by_order(order_id: int, db=Depends(get_db)):
    db_order_items = db.query(OrderItem).filter(OrderItem.order_id == order_id).all()
    if not db_order_items:
        raise HTTPException(status_code=404, detail="No order items found for this order")
    return db_order_items

@router.get("/orderitems/", response_model=List[OIResp])
def get_all_order_items(db=Depends(get_db)):
    db_order_items = db.query(OrderItem).all()
    return db_order_items

@router.get("/orderitems/products/{product_id}", response_model=List[OIResp])
def get_order_items_by_product(product_id: int, db=Depends(get_db)):
    db_order_items = db.query(OrderItem).filter(OrderItem.product_id == product_id).all()
    if not db_order_items:
        raise HTTPException(status_code=404, detail="No order items found for this product")
    return db_order_items

@router.get("/orderitems/orders/{order_id}/products/{product_id}", response_model=OIResp)
def get_order_item_by_order_and_product(order_id: int, product_id: int, db=Depends(get_db)):
    db_order_item = db.query(OrderItem).filter(
        OrderItem.order_id == order_id,
        OrderItem.product_id == product_id
    ).first()
    if db_order_item is None:
        raise HTTPException(status_code=404, detail="Order item not found for this order and product")
    return db_order_item

@router.get("/orderitems/user/{user_id}", response_model=int)
def get_total_order_items_by_user(user_id: int, db=Depends(get_db)):
    total_count = db.query(OrderItem).join(OrderItem.order).filter(Order.user_id == user_id).count()
    return total_count