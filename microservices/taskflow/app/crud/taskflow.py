from sqlalchemy.orm import Session
from app.models.taskflow import Taskflow as TaskFlowModel
from app.schemas.taskflow import *

def get_taskflow(db: Session, item_id: int) -> Optional[TaskflowResponse]:
    db_taskflow = db.query(TaskFlowModel).filter(TaskFlowModel.id == item_id).first()
    if db_taskflow is None:
        return None
    return TaskflowResponse.from_orm(db_taskflow)

def list_taskflows(db: Session):
    # Consulta todos los taskflows desde la base de datos
    db_taskflows = db.query(TaskFlowModel).all()
    # Convierte cada objeto de la base de datos a un modelo TaskflowResponse
    return [TaskflowResponse.from_orm(taskflow) for taskflow in db_taskflows]

def create_task_in_db(db: Session, item: TaskflowCreate):
    item.tags = ','.join(item.tags)
    db_item = TaskFlowModel(**item.dict())  # Crear el objeto de Taskflow usando el diccionario
    db.add(db_item)
    db.commit()
    db.refresh(db_item)  # Asegúrate de que se haya refrescado el objeto con los valores actualizados
    return db_item
    

def update_taskflow(
    db: Session, 
    item_id: int, 
    item: TaskflowCreate):
    # 1. Obtener el taskflow existente
    db_item = db.query(TaskFlowModel).filter(TaskFlowModel.id == item_id).first()
    if not db_item:
        return None

    # 2. Actualizar campos (manejando tags como string)
    update_data = item.model_dump()
    if "tags" in update_data and isinstance(update_data["tags"], list):
        update_data["tags"] = ",".join(update_data["tags"])

    for field, value in update_data.items():
        setattr(db_item, field, value)

    # 3. Persistir cambios
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_taskflow(db: Session, item_id: int) -> bool:
    db_item = db.query(TaskFlowModel).filter(TaskFlowModel.id == item_id).first()
    if not db_item:
        return False
    db.delete(db_item)
    db.commit()
    return True
