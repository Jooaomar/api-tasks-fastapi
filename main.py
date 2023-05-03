from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import Union, List
import pymongo
from fastapi.responses import JSONResponse
from bson import json_util
from dotenv import load_dotenv, find_dotenv
import os
from os.path import join, dirname

from persistence.tarefas_mongo import TasksMongoDBRepository

load_dotenv(find_dotenv())

# use = os.getenv('USER')
# password = os.getenv('PASSWORD')

USER = os.environ.get("USER_DB")
PASSWORD = os.environ.get("PASSWORD_DB")
CLUSTER = os.environ.get("CLUSTER_DB")

app = FastAPI()

origins = [
    "http://localhost:5173/",
    "http://0.0.0.0:5173/",
    "http://localhost:5173",
    "http://0.0.0.0:5173",
    "https://tasks-todo-egs9gz7xp-jooaomar.vercel.app/",
    "https://tasks-todo-egs9gz7xp-jooaomar.vercel.app"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


client = pymongo.MongoClient(f"mongodb+srv://AppListFilme:NXxVLs4Xi6HsU8cv@cluster0.ms2ogne.mongodb.net/?retryWrites=true&w=majority")
# client = pymongo.MongoClient(f"mongodb+srv://{USER}:{PASSWORD}@{CLUSTER}")

db = client["listaFilmes"]
collection = db["filme"]

tarefas_repository = TasksMongoDBRepository()


class Tarefas(BaseModel):
    id: Union[int, None]
    responsavel: str
    descricao: str
    nivel: str          # 1,2,3,4,5
    situacao: str       # em amndamento, resolvida, pendente, cancelado
    prioridade: str     # 1,2,3


tarefas: List[Tarefas] = []


@app.post('/adicionar/')
def adicionar(item: Tarefas):
    # item.id = len(tarefas) + 100
    # # tarefas.append(item)
    # col = dict(item)
    # collection.insert_one(col)
    # return item
    tarefas_repository.salvar(item)


@app.delete('/deletar/{tarefa_id}')
def remover(tarefa_id: str):
    tarefas_repository.remover(tarefa_id)


@app.get('/tarefas')
def todas_tarefas():
    tarefas = tarefas_repository.todos()
    # filmes_usuario = list(
    #     filter(lambda filme: filme.usuario_id == usuario.id, filmes))
    return tarefas



@app.get('/tarefas/')
def listar_situacao(situacao: str):
    selects = []
    for task in tarefas:
        if task.situacao == situacao:
            selects.append(task)
    if len(selects) > 0:
        return selects
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get('/tarefas-nivel/')
def listar_nivel(nivel: int):
    selects = []
    for task in tarefas:
        if task.nivel == nivel:
            selects.append(task)
    if len(selects) > 0:
        return selects
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get('/tarefas-prioridade/')
def listar_prioridade(prioridade: int):
    selects = []
    for task in tarefas:
        if task.prioridade == prioridade:
            selects.append(task)
    if len(selects) > 0:
        return selects
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get('/detalhes/{tarefa_id}')
def detalhes(tarefa_id: int):

    for task in tarefas:
        if task.id == tarefa_id:
            return task


@app.put('/situacao/{tarefa_id}')
def situacao(tarefa_id: int, mudanca: str):

    for task in tarefas:
        if task.id == tarefa_id:
            task.situacao = mudanca
            return task




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)