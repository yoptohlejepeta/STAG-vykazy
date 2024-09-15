from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routes import router

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Projects management",
    redoc_url=None,
    docs_url="/",
    summary="API for managing projects",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router.router)
