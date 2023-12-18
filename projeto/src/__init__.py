from flask import Flask
from dotenv import load_dotenv
import sys, os

load_dotenv()


seu_caminho_completo = os.environ.get('url')

print("Iniciando o pacote src")

# caminho para a pasta raiz do projeto ex: C:/seu-caminho/projeto
sys.path.append(seu_caminho_completo)

app = Flask(__name__)
