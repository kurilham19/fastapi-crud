from pydantic import BaseModel

class UserBase(BaseModel):
  name: str
  email : str
  password: str
  
class User(UserBase):
  id: int
  
  class Config:
    orm_mode = True