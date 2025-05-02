from fastapi import FastAPI, Request

from app.db.session import SessionLocal

from app.db.utils import run_migrations
from .api.v1.endpoints.taskflow_endpoint import router as taskflow_router
from .api.v1.endpoints.auth import router as auth_router
from .api.v1.endpoints.user_endpoint import router as user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    """
    Middleware para inyectar la sesión de base de datos en request.state.db
    """
    response = None
    try:
        request.state.db = SessionLocal()  # Crea la sesión
        response = await call_next(request)  # Pasa la solicitud al siguiente paso (rutas)
    finally:
        request.state.db.close()  # Cierra la sesión cuando termine la solicitud
    return response

run_migrations()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(taskflow_router, prefix="/taskflow", tags=["taskflow"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/user", tags=["user"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
