from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src import api

app = FastAPI(title="FastAPI Steam Application",
              description="Proyecto individual 1 - MLOps - Steam",
              version="1.0.0", )

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

@app.get("/")
async def root():
    return {"message": "APP OK"}

@app.get("/playtimegenre/{genre}")
def read_user(genre):
    year = api.PlayTimeGenre(genre)
    if year == 0:
        raise HTTPException(status_code=400, detail="Error, Genero no encontrado!")
    return str(year)

@app.get("/userforgenre/{genre}")
def read_user(genre):
    data = api.UserForGenre(genre)
    if data == 0:
        raise HTTPException(status_code=400, detail="Error, Genero no encontrado!")
    return str(data)

@app.get("/usersrecommend/{year}")
def read_user(year:int):
    data = api.UsersRecommend(year)
    if data == 0:
        raise HTTPException(status_code=400, detail="Error, Año no encontrado!")
    return str(data)

@app.get("/usersnotrecommend/{year}")
def read_user(year:int):
    data = api.UsersNotRecommend(year)
    if data == 0:
        raise HTTPException(status_code=400, detail="Error, Año no encontrado!")
    return str(data)

@app.get("/sentiment_analysis/{year}")
def read_user(year:int):
    data = api.sentiment_analysis(year)
    if data == 0:
        raise HTTPException(status_code=400, detail="Error, Año no encontrado!")
    return str(data)

@app.get("/recomendacion_juego/{id}")
def read_user(id:int):
    data = api.recomendacion_juego(id)
    if data == 0:
        raise HTTPException(status_code=400, detail="Error, Id no encontrado!")
    return str(data)