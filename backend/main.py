from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(
    
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

@app.get("/data")
def get_graph_data():
    return {
        "labels": ["January", "February", "March", "April", "May", "June", "July"],
        "datasets": [{
        "data": [random.randint(1, 100) for _ in range(7)]
    }]
    }
