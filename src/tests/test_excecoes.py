import pytest
from src.curador import Curador, FormatoInvalidoError, IdInvalidoError

@pytest.mark.excecoes
@pytest.mark.erros
class TestExcecoesCurador:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.curador = Curador()

    @pytest.mark.parametrize("dados_invalidos", [
        ([{"nome": "Raphael Viana"}]),
        ([{"id": "texto", "nome": "Ana Seabra"}]),
        ([{"id": None, "nome": "Luiz Souza"}]),
        ([{"id": 123}]),
        ([])
    ])
    def test_excecao_formato_registro_invalido(self, dados_invalidos):
        with pytest.raises(FormatoInvalidoError):
            self.curador.processar_base_dados(dados_invalidos)

    @pytest.mark.parametrize("registro_id_invalido", [
        ([{"id": -5, "nome": "Sérgio Guaraldi"}]),
        ([{"id": 0, "nome": "Vanilda Junior"}]),
        ([{"id": -746938, "nome": "Raphael Viana"}]),
        ([{"id": -1, "nome": "Cassius de Souza"}]),
        ([{"id": -10074, "nome": "Moreira V O"}])
    ])
    def test_excecao_id_negativo_ou_zero(self, registro_id_invalido):
        with pytest.raises(IdInvalidoError):
            self.curador.processar_base_dados(registro_id_invalido)