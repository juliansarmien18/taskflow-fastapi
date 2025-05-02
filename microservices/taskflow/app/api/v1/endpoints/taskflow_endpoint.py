from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app import schemas
from app.crud.taskflow import *
from app.schemas.taskflow import *
from app.db.session import get_db
from app.models import User
from app.core.security import Portador


router = APIRouter()


security = Portador()


@router.get("/list-all", response_model=List[schemas.TaskflowResponse])
def list_all(db: Session = Depends(get_db),  usuario: dict = Depends(security)):
    taskflows = list_taskflows(db=db)
    return taskflows


@router.post("/", response_model=schemas.TaskflowResponse)
def create_taskflow(
    item: TaskflowCreate,
    db: Session = Depends(get_db),
    usuario: dict = Depends(security)  # Aquí recibes el payload del token
):
    db_item = create_task_in_db(db=db, item=item)
    return schemas.TaskflowResponse.from_attributes(db_item)

@router.get("/{item_id}", response_model=schemas.TaskflowResponse)
def read_taskflow(item_id: int, db: Session = Depends(get_db), usuario: dict = Depends(security)):
    taskflow = get_taskflow(db, item_id=item_id)
    if taskflow is None:
        raise HTTPException(status_code=404, detail="Taskflow no encontrado")
    return taskflow

@router.put("/{item_id}", response_model=schemas.TaskflowResponse)
def update_taskflow_endpoint(
    item_id: int, 
    item: schemas.TaskflowCreate, 
    db: Session = Depends(get_db),
    usuario: dict = Depends(security)
):
    # 1. Llamar a la función de servicio
    updated_taskflow = update_taskflow(db=db, item_id=item_id, item=item)
    
    # 2. Manejar errores
    if not updated_taskflow:
        raise HTTPException(
            status_code=404,
            detail="Taskflow no encontrado"
        )
    
    # 3. Convertir a TaskflowResponse y retornar
    return schemas.TaskflowResponse.from_orm(updated_taskflow)

@router.delete("/{item_id}")
def delete_taskflow_endpoint(
    item_id: int, 
    db: Session = Depends(get_db)
):
    # 1. Verificar y eliminar
    deleted = delete_taskflow(db=db, item_id=item_id)
    
    # 2. Manejar errores
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail=f"Taskflow con ID {item_id} no encontrado"
        )
    
    # 3. Retornar confirmación en JSON
    return JSONResponse(
        status_code=200,
        content={
            "message": f"Taskflow con ID {item_id} fue eliminado correctamente",
            "deleted_id": item_id
        }
    )


    
