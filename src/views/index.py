import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controllers.conexao_cientifica_controllers import Conexao_Cientifica_Controllers
from models.conexao_cientifica_models import Conexao_Cientifica_models

class Conexao_Cientifica_Views:
    ...
    # Cria os codigos da aplicaçao