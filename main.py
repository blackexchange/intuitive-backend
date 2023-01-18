from typing import Union


from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse

import schema
from  model import Operadoras

from database import SessionLocal, engine


app = FastAPI()

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Success": "Intuitve Test. By Neville"}


@app.get("/operadoras/{name}")
def read_movie(name: schema.Operadoras.Nome_Fantasia, db: Session = Depends(get_database_session)):
    search = "%{}%".format(name)
    item = db.query(Operadoras).filter(Operadoras.Nome_Fantasia.like(search)).all()
    return {"operadoras": item}
    