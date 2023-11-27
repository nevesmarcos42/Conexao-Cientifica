"""Module providing a function to work with student data."""

class ConexaoCientificaModelsStudents:
    '''Class representing a student'''
    # Dados que a classe Conexao_Cientifica_models possui
    def __init__(self, full_name:str, email:str, ra:int) -> None:
        self.full_name = full_name
        self.email = email
        self.ra = ra
