import uuid
from typing import TypedDict

from bson.objectid import ObjectId
# from decouple import config
from pymongo import MongoClient
from typing import Union, List
# from ..presentation.viewmodels import Filme
from presentation.viewmodels import Tarefas
import pymongo
from bson import json_util
import json


class TasksMongoDBRepository():

    tarefas: List[Tarefas] = []


    def __init__(self):
        # Connect to MongoDB
        # uri = 'mongodb://localhost:27017'
        # uri = config('MONGODB_URL')
        

        client = pymongo.MongoClient(f"mongodb+srv://AppListFilme:NXxVLs4Xi6HsU8cv@cluster0.ms2ogne.mongodb.net/?retryWrites=true&w=majority")


        db = client["listaFilmes"]

        self.colecao = db["filme"]


        try:
            # print('Info MongoDB Server: ', client.server_info())
            print('MongoDB Tarefas 💖')
        except Exception:
            print('Deu erro!')

    def todos(self):
        filmes = []
        for filme in self.colecao.find():
            filme_json = json.loads(json_util.dumps(filme))
            filmes.append(filme_json)
        return filmes

    def salvar(self, item: Tarefas):
        # _id = self.colecao.insert_one(filme.toDict()).inserted_id
        # filme.id = str(_id)
        # return filme

        item.id = str(uuid.uuid4())
        # tarefas.append(item)
        col = dict(item)
        self.colecao.insert_one(col)
        return item
        

    def obter_um(self, filme_id):
        filtro = {"_id": ObjectId(filme_id)}
        filme_encontrado = self.colecao.find_one(filtro)
        return Tarefas.fromDict(filme_encontrado) if filme_encontrado else None

    def remover(self, filme_id):
        filtro = {"id": filme_id}
        self.colecao.delete_one(filtro)

    def atualizar(self, filme_id, filme):
        filtro = {"_id": ObjectId(filme_id)}
        self.colecao.update_one(filtro, {'$set': filme.toDict()})
        filme.id = filme_id
        return filme