from fastapi import APIRouter
from fastapi import Query
from fastapi import Depends
from fastapi import Body
from src.models import get_db
from sqlalchemy.orm import Session
from ..schemas.userSchema import UserBase as UserSchema
from ..services import userService
router = APIRouter()

@router.get("/all",name="Get All Users")
async def get_all_user(db:Session = Depends(get_db)) :
  return userService.get_all_users(db)

@router.get("/{user_id}",name="Get User By ID")
async def get_user(user_id:int, db:Session = Depends(get_db)) :
  return userService.get_user_by_id(user_id, db)

@router.post('/',name='Create New User')
async def add_user(user:UserSchema, db:Session = Depends(get_db)):
  return userService.create_user(db=db, user=user)

@router.put("/{user_id}",name="Get User By ID")
async def update_user(user_id:int, user:UserSchema, db:Session = Depends(get_db)) :
  return userService.update_user_by_id(user_id, user, db)

@router.delete("/{user_id}", name="Delet User By ID")
async def delete_user(user_id:int, db:Session = Depends(get_db)) :
  return userService.delete_user_by_id(user_id, db)
