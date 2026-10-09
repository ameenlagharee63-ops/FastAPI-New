
from database import Base, engine, get_db
import models
from fastapi import Depends, FastAPI, HTTPException
import schemas
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="My FastAPI Project")


@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
  db_user = (
      db.query(models.User).filter(models.User.email == user.email).first()
  )
  if db_user:
    raise HTTPException(status_code=400, detail="Email already registered")

  new_user = models.User(name=user.name, email=user.email)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user


@app.get("/users/", response_model=list[schemas.UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
  users = db.query(models.User).offset(skip).limit(limit).all()
  return users