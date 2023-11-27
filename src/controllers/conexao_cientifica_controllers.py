'''Module Docstring'''
import webbrowser

import re

# Importing files from sibling directories
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# pylint: disable=E0401
# pylint: disable=C0413
from models.conexao_cientifica_models_students import ConexaoCientificaModelsStudents
from models.conexao_cientifica_models_articles import ConexaoCientificaModelsArticles
# pylint: enable=E0401
# pylint: enable=C0413

class ConexaoCientificaControllers:
    """Class representing a controllers"""

    list_students = []
    list_articles = []
    is_logged = False
    registered = True
    monitor = False

    @classmethod
    def register_students(cls, student: ConexaoCientificaModelsStudents) -> str|None:
        """Function student registration."""
        email = student.email

        regex_email = '^[a-z0-9]+[._]?[a-z0-9]+[@][a-zA-Z0]+[.][a-zA-Z0]{2,3}$'
        
        if(re.search(regex_email, email)):
            cls.list_students.append(student)
            print('Aluno cadastrado com sucesso!')
            return 'Aluno cadastrado com sucesso!'
        else:
            print("Dados Invalido")

        return None

    @classmethod
    def login_students(cls, user:str, password:int) -> str|None:
        """Function student login."""
        for student in cls.list_students:

            if(user == student.email and password == student.ra):
                print(f'{student.full_name} você está logado!')
                cls.is_logged = True
                if student.email == 'monitor@gmail.com':
                    cls.monitor = True
                return student.email

            print('Senha ou email invalido')
            return None

    @classmethod
    def monitoring(cls, link:str) -> str|None:
        """Function carries out monitoring."""
        print('Não foi criada!')

    @classmethod
    def register_articles(cls, articles: ConexaoCientificaModelsArticles) -> str|None:
        """Function register article."""

        if cls.is_logged and cls.monitor:
            cls.list_articles.append(articles)
            print('Artigo cadastrado com sucesso!')
            return 'Artigo cadastrado com sucesso!'
        else:
            print('Cadastro não autorizado!')
        
        return None

    @classmethod
    def search_articles(cls, subject:str) -> str|None:
        """Function search article."""
        print('Não foi criada!')

    @classmethod
    def logout(cls) -> None:
        """Function logout."""
        
        print('logout concluido!')
        cls.is_logged = False
        cls.monitor = False
        