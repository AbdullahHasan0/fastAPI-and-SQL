from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    
    name: str = Field(..., description="The name of the product")
    description: str = Field(..., description="A detailed description of the product")
    price: float = Field(..., description="The price of the product")
    quantity: int = Field(..., description="The available quantity of the product")

class ProductResponse(BaseModel):
    id: int = Field(..., description="The unique identifier of the product")
    name: str = Field(..., description="The name of the product")
    description: str = Field(..., description="A detailed description of the product")
    price: float = Field(..., description="The price of the product")
    # quantity: int = Field(..., description="The available quantity of the product")

    class Config:
        from_attributes = True
