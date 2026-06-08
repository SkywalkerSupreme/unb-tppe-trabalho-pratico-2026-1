import pytest
from src.curador import Curador

@pytest.mark.caso3
@pytest.mark.particulas
class TestCaso3Particulas:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.curador = Curador()

    @pytest.mark.parametrize("lista_in, lista_out", [
        (["Luiz Oliveira Souza", "Luiz de Oliveira de Souza"], ["Luiz de Oliveira de Souza", "Luiz de Oliveira de Souza"]),
        (["Ana Mattos Seabra", "Ana de Mattos Seabra"], ["Ana de Mattos Seabra", "Ana de Mattos Seabra"]),
        (["Cassius Souza", "Cassius de Souza"], ["Cassius de Souza", "Cassius de Souza"]),
        (["Veronica Oliveira Moreira", "Veronica de Oliveira Moreira"], ["Veronica de Oliveira Moreira", "Veronica de Oliveira Moreira"]),
        (["Monica Hirata Sant'anna", "Monica Hirata de Sant'anna"], ["Monica Hirata de Sant'anna", "Monica Hirata de Sant'anna"]),
        (["Yuri Vieira Faria", "Yuri de Vieira Faria"], ["Yuri Vieira Faria", "Yuri Vieira Faria"]),
        (["Raphael Gonçalves Viana", "Raphael Gonçalves de Viana"], ["Raphael Gonçalves Viana", "Raphael Gonçalves Viana"]),
        (["Luiz de O de Souza", "Luiz de Oliveira de Souza"], ["Luiz de Oliveira de Souza", "Luiz de Oliveira de Souza"]),
        (["Ana de M Seabra", "Ana de Mattos Seabra"], ["Ana de Mattos Seabra", "Ana de Mattos Seabra"]),
        (["Moreira V O", "Verônica de Oliveira Moreira"], ["Verônica de Oliveira Moreira", "Verônica de Oliveira Moreira"])
    ])
    def test_reintegracao_particulas_obrigatorias(self, lista_in, lista_out):
        assert self.curador.curar_particulas(lista_in) == lista_out

    @pytest.mark.parametrize("lista_in, lista_out", [
        (["Luiz de O. de Souza", "Luiz de Oliveira de Souza"], ["Luiz de Oliveira de Souza", "Luiz de Oliveira de Souza"]),
        (["Ana de M. Seabra", "Ana de Mattos Seabra"], ["Ana de Mattos Seabra", "Ana de Mattos Seabra"]),
        (["Moreira V. de O.", "Veronica de Oliveira Moreira"], ["Veronica de Oliveira Moreira", "Veronica de Oliveira Moreira"]),
        (["V. de O. Moreira", "Verônica de Oliveira Moreira"], ["Verônica de Oliveira Moreira", "Verônica de Oliveira Moreira"]),
        (["Luiz de O. Souza", "Luiz de Oliveira de Souza"], ["Luiz de Oliveira de Souza", "Luiz de Oliveira de Souza"]),
        (["Ana M. de Seabra", "Ana de Mattos Seabra"], ["Ana de Mattos Seabra", "Ana de Mattos Seabra"]),
        (["Souza, L. de O.", "Luiz de Oliveira de Souza"], ["Luiz de Oliveira de Souza", "Luiz de Oliveira de Souza"]),
        (["Moreira, V. de O.", "Veronica de Oliveira Moreira"], ["Veronica de Oliveira Moreira", "Veronica de Oliveira Moreira"]),
        (["Seabra, A. de M.", "Ana de Mattos Seabra"], ["Ana de Mattos Seabra", "Ana de Mattos Seabra"]),
        (["Cassius de S.", "Cassius de Souza"], ["Cassius de Souza", "Cassius de Souza"])
    ])
    def test_particulas_com_pontuacao_opcional(self, lista_in, lista_out):
        assert self.curador.curar_particulas(lista_in) == lista_out

    @pytest.mark.parametrize("lista_in, lista_out", [
        (["Luiz DE Oliveira DE Souza"], ["Luiz de Oliveira de Souza"]),
        (["Ana DE Mattos Seabra"], ["Ana de Mattos Seabra"]),
        (["Cassius DE Souza"], ["Cassius de Souza"]),
        (["Veronica DE Oliveira Moreira"], ["Veronica de Oliveira Moreira"]),
        (["Monica Hirata DE Sant'anna"], ["Monica Hirata de Sant'anna"]),
        (["Luiz de Oliveira de Souza", "Luiz Oliveira Souza", "Luiz DE O. DE Souza"], ["Luiz de Oliveira de Souza", "Luiz de Oliveira de Souza", "Luiz de Oliveira de Souza"]),
        (["Ana de Mattos Seabra", "Ana Mattos Seabra", "Ana DE M. Seabra"], ["Ana de Mattos Seabra", "Ana de Mattos Seabra", "Ana de Mattos Seabra"]),
        (["Cassius de Souza", "Cassius Souza", "Cassius DE S. Souza"], ["Cassius de Souza", "Cassius de Souza", "Cassius de Souza"]),
        (["Yuri Vieira Faria", "Yuri DE Vieira Faria"], ["Yuri Vieira Faria", "Yuri Vieira Faria"]),
        (["Moreira V DE O", "Verônica de Oliveira Moreira"], ["Verônica de Oliveira Moreira", "Verônica de Oliveira Moreira"])
    ])
    def test_normalizacao_caso_particulas(self, lista_in, lista_out):
        assert self.curador.curar_particulas(lista_in) == lista_out