from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas import User as UserSchema
from ..models.userModel import UserModel

def create_user(db: Session, user:UserSchema):
  db_user = UserModel(**user.dict())
  db.add(db_user)
  db.commit()
  return {
    "success" : True,
    "message" : f"Success create new user {user.name}",
    "data" : user
  }
  
def update_user_by_id(user_id:int, user:UserSchema, db: Session):
  db_user = db.query(UserModel).get(user_id)
  try:
    user = user.dict()
    db_user.name = user["name"]
    db_user.email = user["email"]
    db_user.password = user["password"]
    db.commit()
    db.refresh(db_user)
    return {
      "success" : True,
      "message" : f"Success update user with id {user_id}",
      "data" : user
    }
  except Exception as e:
    raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
  
def get_user_by_id(user_id:int, db: Session):
  db_user = db.query(UserModel).get(user_id)
  if (db_user) :
    return {
      "success": True,
      "message": f"Success get user with id {user_id}",
      "data" : db_user
    }
  else:
    raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

def delete_user_by_id(user_id: int, db:Session):
  db_user = db.query(UserModel).get(user_id)
  try:
    db.delete(db_user)
    db.commit()
    return {
      "success": True,
      "message": f"Success delete user with id {user_id}",
      "data" : db_user
    }
  except Exception as e:
    raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    
def get_all_users(db: Session):
  return db.query(UserModel).all()