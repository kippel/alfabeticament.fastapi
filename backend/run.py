import os
from fastapi import FastAPI, HTTPException   
from fastapi.middleware.cors import CORSMiddleware


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

origins = [
    "http://localhost:3000"
]


from routers import llengues, seeding

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(llengues.router)
app.include_router(seeding.router)