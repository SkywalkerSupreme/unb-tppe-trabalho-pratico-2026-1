import os
import json
import pytest

@pytest.fixture(scope="session")
def dados_reais():
    caminho_base = os.path.dirname(os.path.abspath(__file__))
    caminho_dados = os.path.join(caminho_base, "data", "dados_curadoria_800.json")
    
    if not os.path.exists(caminho_dados):
        raise FileNotFoundError(f"Arquivo de dados massivos nao encontrado em: {caminho_dados}")
        
    with open(caminho_dados, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

@pytest.fixture(scope="session")
def dados_corrompidos_dinamicos():
    return {
        "dataset_vazio": [],
        "registro_sem_id": [
            {"nome": "Cassius de Souza", "idade": 40, "email": "autor@pesquisa.br"}
        ],
        "registro_sem_nome": [
            {"id": 46048, "idade": 40, "email": "autor@pesquisa.br"}
        ],
        "id_tipo_invalido": [
            {"id": "46048_texto", "nome": "Cassius de Souza", "idade": 40}
        ],
        "idade_negativa": [
            {"id": 46048, "nome": "Cassius de Souza", "idade": -10, "email": "autor@pesquisa.br"}
        ],
        "idade_extrema": [
            {"id": 46048, "nome": "Cassius de Souza", "idade": 150, "email": "autor@pesquisa.br"}
        ],
        "email_invalido": [
            {"id": 46048, "nome": "Cassius de Souza", "idade": 35, "email": "autor_sem_arroba.br"}
        ],
        "orcid_curto": [
            {"id": 46048, "nome": "Cassius de Souza", "orcid": "0000-0002-9935"}
        ],
        "orcid_longo": [
            {"id": 46048, "nome": "Cassius de Souza", "orcid": "0000-0002-9935-123456"}
        ]
    }

@pytest.fixture(scope="function")
def lote_mutavel_teste(dados_reais):
    return [registro.copy() for registro in dados_reais]