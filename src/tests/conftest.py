import os
import json
import pytest

@pytest.fixture(scope="session")
def datasets():
    """Carrega os arquivos JSON de dados e gabarito usando caminhos absolutos."""
    caminho_base = os.path.dirname(__file__)
    
    caminho_dados = os.path.join(caminho_base, "data", "dados_curadoria_800.json")
    caminho_gabarito = os.path.join(caminho_base, "data", "gabarito_curadoria_800.json")
    
    with open(caminho_dados, "r", encoding="utf-8") as f:
        dados_ruins = json.load(f)
        
    with open(caminho_gabarito, "r", encoding="utf-8") as f:
        gabarito = json.load(f)
        
    return dados_ruins, gabarito


@pytest.fixture
def dados_corrompidos_dinamicos():
    """Gera lote de dados inválidos em memória para testes de estresse de exceções."""
    return {
        "dataset_vazio": [],
        "registro_sem_id": [{"nome": "Cassius de Souza", "idade": 40}],
        "registro_sem_nome": [{"id": 46048, "idade": 40}],
        "id_tipo_invalido": [{"id": "46048_texto", "nome": "Cassius de Souza"}],
        "idade_negativa": [{"id": 46048, "nome": "Cassius de Souza", "idade": -5}],
        "idade_extrema": [{"id": 46048, "nome": "Cassius de Souza", "idade": 150}],
        "email_invalido": [{"id": 46048, "nome": "Cassius de Souza", "email": "autor_sem_arroba.br"}],
        "orcid_curto": [{"id": 46048, "nome": "Cassius de Souza", "orcid": "0000-0002-9935"}]
    }