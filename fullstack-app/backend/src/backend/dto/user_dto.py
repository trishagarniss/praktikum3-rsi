from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 1. Skema Dasar (Biar nggak ngetik berulang)
class UserBase(BaseModel):
    first_name: str
    last_name: str
    whatsapp: str

# 2. Skema untuk Request Create (POST)
class UserInput(UserBase):
    pass

# 3. Skema untuk Request Update (PUT)
class UserUpdate(UserBase):
    pass

# 4. Skema untuk Response yang dikirim ke Swagger/Klien
class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True