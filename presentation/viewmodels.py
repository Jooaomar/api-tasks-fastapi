from typing import Union, List
from pydantic import BaseModel

class Tarefas(BaseModel):
    id: str
    responsavel: str
    descricao: str
    nivel: str          # 1,2,3,4,5
    situacao: str       # em amndamento, resolvida, pendente, cancelado
    prioridade: str  