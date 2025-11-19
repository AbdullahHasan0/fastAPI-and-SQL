from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str = Field(..., description="Name of the user")
    phno: str = Field(..., description="Phone number of the user")
    email: str = Field(..., description="Email address of the user")
    role: str = Field(..., description="Role of the user")

class UserResponse(BaseModel):
    id: int = Field(..., description="Unique ID of the user")
    name: str = Field(..., description="Name of the user")
    phno: str = Field(..., description="Phone number of the user")
    email: str = Field(..., description="Email address of the user")
    role: str = Field(..., description="Role of the user")
    
    class ConfigDict:
        from_attributes = True
