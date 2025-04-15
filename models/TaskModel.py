from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    intern_email:str
    title:str
    description:Optional[str]=None
    assigned_at:Optional[datetime]=None
    completed:bool=False

    