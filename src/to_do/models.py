from typing import Optional,List,TYPE_CHECKING
from sqlmodel import Field, SQLModel,Relationship
from datetime import datetime

class TodoBase(SQLModel):
    task_title : str = Field(nullable=False)
    task_datetime: datetime= Field(nullable=False)
    task_status :bool =Field(nullable=True,default=False)
    
class Todo(TodoBase,table = True):
    __tablename__="to_do_list"
    task_id :int= Field(nullable=False,primary_key=True,default=None)
    
class TodoCreate(TodoBase):
    pass 
 
class TodoRead(TodoBase):
    task_id : int
    

