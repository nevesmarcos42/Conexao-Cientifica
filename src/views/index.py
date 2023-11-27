'''Module Docstring'''
import os
import time
from datetime import date


# Importing files from sibling directories
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# pylint: disable=E0401
# pylint: disable=C0413
from controllers.conexao_cientifica_controllers import ConexaoCientificaControllers
from models.conexao_cientifica_models_articles import ConexaoCientificaModelsArticles
from models.conexao_cientifica_models_students import ConexaoCientificaModelsStudents
# pylint: enable=E0401
# pylint: enable=C0413


class ConexaoCientificaViews:
    """Class representing a views"""

    # Cadastra o Monitor inicialmente
    monitor = ConexaoCientificaModelsStudents(
                                        full_name= 'Monitor',
                                        email= 'monitor@gmail.com',
                                        ra= 1352113065
                                        )
    ConexaoCientificaControllers.register_students(monitor)
    #os.system('cls') # Limpa o terminal

    # Application menu
    while True:
        decision = int(input('Digite a opção escolhida: \n'
                               '-------------------------\n'
                               '- 1 cadastrar um aluno\n'
                               '- 2 Acesso\n'
                               '- 3 monitoria\n'
                               '- 4 cadastrar um artigo\n'
                               '- 5 pesquisar artigos\n'
                               '- 6 logout\n'
                               ))
        if decision == 1:
            os.system('cls') # Limpa o terminal

            print('---------------Cadastro----------------')
            full_name_informed = input("Informe seu nome completo: ")
            email_informed = input("Informe seu email: ")
            # Trata se for informado outro valor ao invés de um numero
            try:
                ra_informed = int(input("Informe seu RA: "))
            except ValueError as error:
                ra_informed = 0
                os.system('cls') # Limpa o terminal
                print('É preciso informar um valor do tipo numerico, se não o '
                      'valor 0 sera atituido ao seu RA!')
                time.sleep(3) # Guarda 3 segundos para continuar o fluxo

            os.system('cls') # Limpa o terminal

            # Cadastra o aluno
            student = ConexaoCientificaModelsStudents(
                                                full_name= full_name_informed,
                                                email= email_informed,
                                                ra= ra_informed
                                                )
            ConexaoCientificaControllers.register_students(student)

            time.sleep(3) # Guarda 3 segundos para continuar o fluxo
            os.system('cls') # Limpa o terminal

        elif decision == 2:
            os.system('cls') # Limpa o terminal

            print('--------------Login----------------')
            user_informed = input('Informe o usuario: ')
            password_informed = int(input('Informe a senha: '))

            os.system('cls') # Limpa o terminal

            ConexaoCientificaControllers.login_students(
                user=user_informed, password=password_informed
                )

            time.sleep(3) # Guarda 3 segundos para continuar o fluxo
            os.system('cls') # Limpa o terminal

        elif decision == 3:
            os.system('cls')
            # Abre o navegador e carrega a pagina que vai ser realizada
            # a monitoria
            ConexaoCientificaControllers.monitoring(
                link='https://meet.google.com/'
                )

            time.sleep(3) # Guarda 3 segundos para continuar o fluxo
            os.system('cls') # Limpa o terminal

        elif decision == 4:
            # Data atual do registro
            current_date = str(date.today())

            print('---------------Cadastro----------------')
            author_register = input("Informe seu nome do autor: ")
            data_register = current_date
            title_register = input("Informe o titulo: ")
            subject_register = input("Informe o assunto: ")

            os.system('cls') # Limpa o terminal

            article = ConexaoCientificaModelsArticles(
                                                    author= author_register,
                                                    data= data_register,
                                                    title= title_register,
                                                    subject= subject_register
                                                         )

            ConexaoCientificaControllers.register_articles(article)

            time.sleep(3) # Guarda 3 segundos para continuar o fluxo
            os.system('cls') # Limpa o terminal

        elif decision == 5:
            os.system('cls') # Limpa o terminal

            ConexaoCientificaControllers.search_articles('IA')

            time.sleep(2) # Guarda 3 segundos para continuar o fluxo
            os.system('cls') # Limpa o terminal
        
        elif decision == 6:
            os.system('cls') # Limpa o terminal

            ConexaoCientificaControllers.logout()

            time.sleep(2) # Guarda 3 segundos para continuar o fluxo
            os.system('cls') # Limpa o terminal

        else:
            os.system('cls') # Limpa o terminal

            print(f'{decision} é uma opção invalida!')

            time.sleep(2) # Guarda 3 segundos para continuar o fluxo
            os.system('cls') # Limpa o terminal
