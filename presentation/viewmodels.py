from typing import Union, List
from pydantic import BaseModel

class Tarefas(BaseModel):
    id: Union[int, None]
    responsavel: str
    descricao: str
    nivel: str          # 1,2,3,4,5
    situacao: str       # em amndamento, resolvida, pendente, cancelado
    prioridade: str 