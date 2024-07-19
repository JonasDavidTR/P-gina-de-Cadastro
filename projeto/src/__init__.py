from flask import Flask
from dotenv import load_dotenv
import sys, os

load_dotenv()

# Subistitua os.environ.get('seu_caminho') pelo seu caminho
url = os.environ.get('seu_caminho')

# caminho para a pasta raiz do projeto ex: C:/seu-caminho/projeto
sys.path.append(url)
print()

app = Flask(__name__)
