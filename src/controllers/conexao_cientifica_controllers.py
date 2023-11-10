import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from models.conexao_cientifica_models import Conexao_Cientifica_models
from typing import List

class Conexao_Cientifica_Controllers:

    List_students = []

    @classmethod
    def register_students(cls, aluno: Conexao_Cientifica_models) -> None:
        ...
        # cls.aluno.append(aluno)
    
    @classmethod
    def login_students(cls) -> None:
        ...
    
    @classmethod
    def monitoria(cls) -> None:
        ...
    
    @classmethod
    def register_articles(cls) -> None:
        ...
    
    @classmethod
    def search_articles(cls) -> None:
        ...