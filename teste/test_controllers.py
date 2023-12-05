'''Module Docstring'''
import sys
import pytest

sys.path.append(".")

# pylint: disable=E0401
# pylint: disable=C0413
from src.models import conexao_cientifica_models_articles
from src.models import conexao_cientifica_models_students
from src.controllers import conexao_cientifica_controllers
# pylint: enable=E0401
# pylint: enable=C0413


class TestStudents:
    """Class performs the tests"""
    @pytest.fixture
    def co_cie_con(self):
        """Function."""
        return conexao_cientifica_controllers.ConexaoCientificaControllers

    # def test_valid_register_student(self, co_cie_con):
    #     """Function valid login."""
    #     c_c_m_student = conexao_cientifica_models_students.ConexaoCientificaModelsStudents(
    #         full_name='João Silva',
    #         email='gmail@gmail.com',
    #         ra=1352113070
    #     )
    #     result = co_cie_con.register_students(c_c_m_student)

    #     assert result == 'Aluno cadastrado com sucesso!'

    # def test_invalid_register_student(self, co_cie_con):
    #     """Function valid login."""
    #     c_c_m_student = conexao_cientifica_models_students.ConexaoCientificaModelsStudents(
    #         full_name='João Silva',
    #         email='gmailgmail.com',
    #         ra=1352113070
    #     )

    #     result = co_cie_con.register_students(c_c_m_student)

    #     assert result == 'Aluno cadastrado com sucesso!'

    # def test_valid_login(self, co_cie_con):
    #     """Function valid login."""
    #     c_c_m_student = conexao_cientifica_models_students.ConexaoCientificaModelsStudents(
    #         full_name='João Silva',
    #         email='gmail@gmail.com',
    #         ra=1352113070
    #     )
    #     co_cie_con.register_students(c_c_m_student)
    #     c_c_c_s = co_cie_con.login_students(
    #         user='gmail@gmail.com',
    #         password=1352113070
    #     )
    #     assert c_c_c_s == c_c_m_student.email

    # def test_invalid_login(self, co_cie_con):
    #     """Function invalid login."""
    #     c_c_m_student = conexao_cientifica_models_students.ConexaoCientificaModelsStudents(
    #         full_name='João Silva',
    #         email='gmail@gmail.com',
    #         ra=1352113070
    #     )

    #     co_cie_con.register_students(c_c_m_student)

    #     c_c_c_s = co_cie_con.login_students(
    #         user='carlos@gmail.com',
    #         password=1352113070
    #     )
    #     assert c_c_c_s == c_c_m_student.email
    
    # def test_valid_register_article(self, co_cie_con):
    #     """Function valid article."""
    #     c_c_m_student = conexao_cientifica_models_students.ConexaoCientificaModelsStudents(
    #         full_name='Monitor',
    #         email='monitor@gmail.com',
    #         ra=1352113070
    #     )

    #     co_cie_con.register_students(c_c_m_student)

    #     c_c_c_s = co_cie_con.login_students(
    #         user='monitor@gmail.com',
    #         password=1352113070
    #     )
    #     c_c_m_article = conexao_cientifica_models_articles.ConexaoCientificaModelsArticles(
    #         author= 'João Silva',
    #         data= '2023-15-11',
    #         title= 'IA',
    #         subject= "IA"
    #     )

    #     result = co_cie_con.register_articles(c_c_m_article)

    #     assert 'Artigo cadastrado com sucesso!' == result
    
    # def test_invalid_register_article(self, co_cie_con):
    #     """Function valid article."""
    #     c_c_m_student = conexao_cientifica_models_students.ConexaoCientificaModelsStudents(
    #         full_name='Monitor',
    #         email='monitor@gmail.com',
    #         ra=1352113070
    #     )
    #     co_cie_con.register_students(c_c_m_student)

    #     c_c_c_s = co_cie_con.login_students(
    #         user='marcos@gmail.com',
    #         password=1352113070
    #     )
    #     c_c_m_article = conexao_cientifica_models_articles.ConexaoCientificaModelsArticles(
    #         author= 'João Silva',
    #         data= '2023-15-11',
    #         title= 'IA',
    #         subject= "IA"
    #     )

    #     result = co_cie_con.register_articles(c_c_m_article)

    #     assert 'Artigo cadastrado com sucesso!' == result
    



   
