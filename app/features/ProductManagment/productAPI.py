from fastapi import APIRouter
from app.features.ProductManagment.productschema import ProductCreate as PCreate, ProductResponse as PResp
from typing import List
from app.database.databaseconnector import DatabaseConector
from fastapi import Depends, HTTPException
from app.database.databaseschema import Product
db_url = "sqlite:///users.db"

router = APIRouter()
db_connector = DatabaseConector(DB_URL=db_url)
get_db = db_connector.get_db

@router.get("/products/{prod_id}", response_model=PResp)
async def get_product(prod_id: int, db=Depends(get_db)):
    product = db.query(Product).filter(Product.id == prod_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products/", response_model=PResp)
async def create_product(product: PCreate, db=Depends(get_db)):
    if db.query(Product).filter(Product.id == product.id).first():
        raise HTTPException(status_code=400, detail="Product with this ID already exists")
    
    new_product = Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.delete("/products/{prod_id}")
async def delete_product(prod_id: int, db=Depends(get_db)):
    product = db.query(Product).filter(Product.id == prod_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted successfully"}

@router.get("/products/", response_model=List[PResp])
async def list_products(db=Depends(get_db)):
    products = db.query(Product).all()
    return products