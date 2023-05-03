# A fazerfrom pydantic import BaseModel, EmailStr
# from sqlalchemy.orm import registry
# from sqlmodel import Field, SQLModel
from typing import Union, List
from pydantic import BaseModel



# mapper_registry = registry()


class Tarefas(BaseModel):
    id: str
    responsavel: str
    descricao: str
    nivel: int          # 1,2,3,4,5
    situacao: str       # em amndamento, resolvida, pendente, cancelado
    prioridade: int  