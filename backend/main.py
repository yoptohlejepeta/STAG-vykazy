from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import router

app = FastAPI(
    title="UJEP uchazeči PŘF",
    redoc_url=None,
    docs_url="/",
    summary="API pro frontend aplikace Uchazeči PŘF",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/books")
def get_books():
    return [
        {"name": "In the Mountains of Madness", "author": "H.P. Lovecraft"},
        {"name": "One Hundred Years of Solitude", "author": "Gabriel García Márquez"},
    ]


app.include_router(router.router)
