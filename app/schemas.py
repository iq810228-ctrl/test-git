from pydantic import BaseModel, ConfigDict
from typing import Optional

class TaskBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # Pydantic V2

    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    completed: Optional[bool] = None

class TaskOut(TaskBase):
    id: int
    completed: bool