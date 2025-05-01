from fastapi import FastAPI

from app.db.utils import run_migrations
from .api.v1.endpoints.taskflow_endpoint import router as taskflow_router
from .api.v1.endpoints.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
