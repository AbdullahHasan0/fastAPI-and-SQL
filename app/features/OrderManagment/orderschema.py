
from pydantic import BaseModel, Field
from datetime import datetime

class OrderCreate(BaseModel):

    user_id: int = Field(..., description="ID of the user placing the order")
    status: bool = Field(..., description="Status of the order")
    total_amount: float = Field(..., description="Total amount of the order")


class OrderResponse(BaseModel):
    id: int = Field(..., description="ID of the order")
    user_id: int = Field(..., description="ID of the user placing the order")
    status: bool = Field(..., description="Status of the order")
    total_amount: float = Field(..., description="Total amount of the order")
    created_at: datetime = Field(..., description="Order creation timestamp")
    updated_at: datetime = Field(..., description="Order last update timestamp")


    class Config:
        from_attributes = True