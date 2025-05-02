from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class TaskflowBase(BaseModel):
    title: str
    description: str
    end_date: Optional[datetime] 
    tags: List[str]
    completed: Optional[bool] = False

class TaskflowCreate(TaskflowBase):
    pass

class Taskflow(TaskflowBase):
    id: int

    class Config:
        from_attributes = True

class TaskflowResponse(BaseModel):
    id: int
    title: str
    description: str
    end_date: Optional[datetime] = None
    tags: List[str]  # Esta es la lista que FastAPI espera para la respuesta
    completed: Optional[bool] = False

    @classmethod
    def from_attributes(cls, obj):
        obj_dict = obj.__dict__
        # Convierte la cadena de tags a lista si es un string
        if 'tags' in obj_dict and isinstance(obj_dict['tags'], str):
            obj_dict['tags'] = obj_dict['tags'].split(',')
        return cls(**obj_dict)

    @classmethod
    def from_orm(cls, obj):
        # Convierte el objeto ORM a un modelo Pydantic
        obj_dict = obj.__dict__
        if 'tags' in obj_dict and isinstance(obj_dict['tags'], str):
            obj_dict['tags'] = obj_dict['tags'].split(',')
        return cls(**obj_dict)