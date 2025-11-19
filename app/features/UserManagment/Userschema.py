from pydantic import BaseModel, Field,EmailStr, constr

class UserCreate(BaseModel):
    name: str = Field(...,min_length=3, max_length=50, description="Name of the user")
    phno: str = Field(...,min_length=11, max_length=15, description="Phone number of the user")
    email: EmailStr = Field(..., description="Email address of the user")
    role: str = Field(..., description="Role of the user")
    age: int = Field(..., ge=0, le=120, description="Age of the user",)
    password: str = Field(..., min_length=8,min_digits=1,description="Password for the user account")

class UserResponse(BaseModel):
    id: int = Field(..., description="Unique ID of the user")
    name: str = Field(..., description="Name of the user")
    phno: str = Field(..., description="Phone number of the user")
    email: str = Field(..., description="Email address of the user")
    role: str = Field(..., description="Role of the user")
    age: int = Field(..., description="Age of the user")
    
    class ConfigDict:
        from_attributes = True
