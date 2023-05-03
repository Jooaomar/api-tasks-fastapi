from fastapi import HTTPException, APIRouter
from typing import List
from dotenv import load_dotenv, find_dotenv
from presentation.viewmodels import Tarefas

from persistence.tarefas_mongo import TasksMongoDBRepository

load_dotenv(find_dotenv())

print('Tasks Controller ✅')
routes = APIRouter()


tarefas_repository = TasksMongoDBRepository()

tarefas: List[Tarefas] = []


@routes.post('/adicionar/')
def adicionar(item: Tarefas):
    tarefas_repository.salvar(item)


@routes.delete('/deletar/{tarefa_id}')
def remover(tarefa_id: str):
    tarefas_repository.remover(tarefa_id)


@routes.get('/tarefas')
def todas_tarefas():
    tarefas = tarefas_repository.todos()
    return tarefas



@routes.get('/tarefas/')
def listar_situacao(situacao: str):
    selects = []
    for task in tarefas:
        if task.situacao == situacao:
            selects.routesend(task)
    if len(selects) > 0:
        return selects
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@routes.get('/tarefas-nivel/')
def listar_nivel(nivel: int):
    selects = []
    for task in tarefas:
        if task.nivel == nivel:
            selects.routesend(task)
    if len(selects) > 0:
        return selects
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@routes.get('/tarefas-prioridade/')
def listar_prioridade(prioridade: int):
    selects = []
    for task in tarefas:
        if task.prioridade == prioridade:
            selects.routesend(task)
    if len(selects) > 0:
        return selects
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@routes.get('/detalhes/{tarefa_id}')
def detalhes(tarefa_id: int):

    for task in tarefas:
        if task.id == tarefa_id:
            return task


@routes.put('/situacao/{tarefa_id}')
def situacao(tarefa_id: int, mudanca: str):

    for task in tarefas:
        if task.id == tarefa_id:
            task.situacao = mudanca
            return task
