from fastapi.routing import APIRouter
from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_404_NOT_FOUND,HTTP_200_OK
from typing import List
from sqlmodel import Session
from src.database import get_db
from src.to_do.models import TodoBase,TodoRead,TodoCreate,Todo

router = APIRouter()

@router.get("/get_all_task",response_model=List[TodoRead])
def get_all_tasks(db:Session=Depends(get_db)):
    list=  db.query(Todo).all()
    if list:
        return list
    else:
        return HTTPException(status_code=HTTP_404_NOT_FOUND,detail="Task does not exist.")

@router.post("/create_task",response_model=TodoRead)
def create(task:TodoCreate,db:Session =Depends(get_db)):
    db_task = Todo(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return HTTPException(status_code=HTTP_200_OK,detail=db_task)

@router.get("/get_task_by_id",response_model=TodoRead)
def get_by_id(task_id:int,db:Session=Depends(get_db)):
    task =  db.query(Todo).filter(Todo.task_id==task_id).first()
    if task:
        return task
    else:
        return HTTPException(status_code=HTTP_404_NOT_FOUND,detail="Task does not exist.")

@router.put("/update_task")
def update_task(task_id:int,task :TodoCreate,db:Session=Depends(get_db)):
    task_update = task.dict(exclude_unset=True)
    db_obj = db.query(Todo).filter(Todo.task_id == task_id).update(task_update)
    db.commit()
    return db_obj

@router.delete("/delete task")
def delete_task(task_id:int,db:Session=Depends(get_db)):
    task =  db.query(Todo).filter(Todo.task_id==task_id).first()
    if task:
        db.query(Todo).filter(Todo.task_id==task_id).delete()
        db.commit()
        return HTTPException(status_code=HTTP_200_OK,detail="Task Deleted")
    else:
        return HTTPException(status_code=HTTP_404_NOT_FOUND,detail="Task Not found")
