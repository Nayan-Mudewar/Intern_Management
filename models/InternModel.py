from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import time

class InternModel(BaseModel):
    name: str
    email: EmailStr
    role:str
    in_time:Optional[time]=None
    out_time:Optional[time]=None


