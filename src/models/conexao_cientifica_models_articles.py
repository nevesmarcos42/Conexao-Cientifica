"""Module providing a function to work with article data."""

class ConexaoCientificaModelsArticles:
    """Class representing a article data"""

    def __init__(self, author:str, data:str, title:str, subject:str) -> None:
        self.author = author
        self.data = data
        self.title = title
        self.subject = subject
