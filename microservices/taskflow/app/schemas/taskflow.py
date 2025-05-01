from pydantic import BaseModel

class TaskflowBase(BaseModel):
    name: str
    description: str

class TaskflowCreate(TaskflowBase):
    pass

class Taskflow(TaskflowBase):
    id: int

    class Config:
        from_attributes = True
