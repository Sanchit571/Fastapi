from sqlalchemy import Column , String , Boolean , Integer
from src.utils.db import Base

class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer , primary_key = True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean , default = False)
    
