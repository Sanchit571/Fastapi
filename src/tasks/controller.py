from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import  TaskModel
from fastapi import HTTPException , Request , status  
from src.utils.settings import settings 
import jwt 
from datetime import datetime 


def create_task(body : TaskSchema , db: Session):
    data = body.model_dump()
    new_task = TaskModel(Title = data["title"],
                         description = data["description"],
                         is_completed = data["is_completed"]
                        )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"status" : "Task Created Successfully..."}


def get_task(db : Session):
    tasks = db.query(TaskModel).all()
    return tasks


def get_one_task(task_id : int , db : Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task :
        raise HTTPException(404 , detail = "Task Id is Incorrect")
    
    
    return one_task 


def update_task(body: TaskSchema , task_id : int , db : Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task :
        raise HTTPException(404 , detail = "Task Id is Incorrect" )

    for field , value  in setattr.items():
        db.get(field) = value 


    db.add(one_task)
    db.commit() 
    db.refresh()

    return one_task

def delete_task(task_id : int , db : Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404 , detail = "Task Id is Incorrect")

    db.delete(one_task)
    db.commit()
    db.referesh()

    return None



 


     