import pytest
from src.curador import Curador

@pytest.mark.caso5
@pytest.mark.deduplicacao
class TestCaso5Deduplicacao:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.curador = Curador()

    @pytest.mark.parametrize("dicionario_in, dicionario_out", [
        (
            {"31298": "Raphael Goncalves Viana", "433094": "Raphael Gonçalves Viana", "549243": "Raphael Gonçalves Viana"},
            {"31298": "Raphael Gonçalves Viana", "433094": "Raphael Gonçalves Viana", "549243": "Raphael Gonçalves Viana"}
        ),
        (
            {"243349": "Ana de Mattos Seabra", "28372": "Ana de Mattos Seabra", "582585": "A. M. Seabra"},
            {"28372": "Ana de Mattos Seabra", "243349": "Ana de Mattos Seabra", "582585": "Ana de Mattos Seabra"}
        ),
        (
            {"746936": "Souza C.", "28371": "Cassius de Souza", "746937": "Cassius Souza"},
            {"28371": "Cassius de Souza", "746936": "Cassius de Souza", "746937": "Cassius de Souza"}
        ),
        (
            {"608303": "Moreira V O", "31303": "Veronica de Oliveira Moreira", "243352": "Verônica de Oliveira Moreira"},
            {"31303": "Verônica de Oliveira Moreira", "243352": "Verônica de Oliveira Moreira", "608303": "Verônica de Oliveira Moreira"}
        ),
        (
            {"608296": "Luiz Oliveira Souza", "549242": "Souza, Luiz de Oliveira", "31297": "Luiz de Oliveira de Souza"},
            {"31297": "Luiz de Oliveira de Souza", "549242": "Luiz de Oliveira de Souza", "608296": "Luiz de Oliveira de Souza"}
        ),
        (
            {"433095": "Mônica Hirata Sant'anna", "31299": "Monica Hirata Sant`anna", "549244": "Sant'anna M. H."},
            {"31299": "Mônica Hirata Sant'anna", "433095": "Mônica Hirata Sant'anna", "549244": "Mônica Hirata Sant'anna"}
        ),
        (
            {"763027": "Vanilda Cristina Junior", "335284": "Vanilda Cristina Júnior"},
            {"335284": "Vanilda Cristina Júnior", "763027": "Vanilda Cristina Júnior"}
        ),
        (
            {"554799": "Sergio Henrique Guaraldi", "243350": "Sérgio Henrique Guaraldi", "954057": "SH Guaraldi"},
            {"243350": "Sérgio Henrique Guaraldi", "554799": "Sérgio Henrique Guaraldi", "954057": "Sérgio Henrique Guaraldi"}
        ),
        (
            {"713897": "Yuri Vieira Faria", "51104": "Y. V. Faria"},
            {"51104": "Yuri Vieira Faria", "713897": "Yuri Vieira Faria"}
        ),
        (
            {"16175": "Raphael Gonçalves Viana", "11071": "Raphael Gonçalves Viana"},
            {"11071": "Raphael Gonçalves Viana", "16175": "Raphael Gonçalves Viana"}
        )
    ])
    def test_eleicao_menor_id_com_unificacao(self, dicionario_in, dicionario_out):
        assert self.curador.consolidar_ids(dicionario_in) == dicionario_out

    @pytest.mark.parametrize("lista_autores, id_esperado", [
        ([{"id": 433094, "nome": "Raphael Goncalves Viana"}, {"id": 31298, "nome": "Raphael Gonçalves Viana"}], 31298),
        ([{"id": 243349, "nome": "Ana de Mattos Seabra"}, {"id": 28372, "nome": "Ana de Mattos Seabra"}], 28372),
        ([{"id": 746936, "nome": "Souza C."}, {"id": 28371, "nome": "Cassius de Souza"}], 28371),
        ([{"id": 608303, "nome": "Moreira V O"}, {"id": 31303, "nome": "Veronica de Oliveira Moreira"}], 31303),
        ([{"id": 608296, "nome": "Luiz Oliveira Souza"}, {"id": 31297, "nome": "Luiz de Oliveira de Souza"}], 31297),
        ([{"id": 433095, "nome": "Mônica Hirata Sant'anna"}, {"id": 31299, "nome": "Monica Hirata Sant`anna"}], 31299),
        ([{"id": 763027, "nome": "Vanilda Cristina Junior"}, {"id": 335284, "nome": "Vanilda Cristina Júnior"}], 335284),
        ([{"id": 554799, "nome": "Sergio Henrique Guaraldi"}, {"id": 243350, "nome": "Sérgio Henrique Guaraldi"}], 243350),  # Corrigido aqui
        ([{"id": 713897, "nome": "Yuri Vieira Faria"}, {"id": 54942, "nome": "Yuri Vieira Faria"}], 54942),
        ([{"id": 14207, "nome": "Ana de Mattos Seabra"}, {"id": 84364, "nome": "Ana de Mattos Seabra"}], 14207),
        ([{"id": 746938, "nome": "Raphael Goncalves Viana"}, {"id": 16175, "nome": "Raphael Gonçalves Viana"}], 16175),
        ([{"id": 92397, "nome": "Lílian Luíza Viana Vieira"}, {"id": 82512, "nome": "Lílian Luíza Viana Vieira"}], 82512),
        ([{"id": 77391, "nome": "A. M. Seabra"}, {"id": 17944, "nome": "A. M. Seabra"}], 17944),
        ([{"id": 70637, "nome": "V. de O. Moreira"}, {"id": 86350, "nome": "V. de O. Moreira"}], 70637),
        ([{"id": 31798, "nome": "Seabra A. M."}, {"id": 99399, "nome": "Seabra A. M."}], 31798),
        ([{"id": 46434, "nome": "Souza, Luiz de Oliveira"}, {"id": 19099, "nome": "Souza, Luiz de Oliveira"}], 19099),
        ([{"id": 80010, "nome": "Souza C."}, {"id": 33053, "nome": "Souza C."}], 33053),
        ([{"id": 11220, "nome": "Vanilda Cristina Junior"}, {"id": 58434, "nome": "Vanilda Cristina Junior"}], 11220),
        ([{"id": 53719, "nome": "Mônica Hirata Sant'anna"}, {"id": 17146, "nome": "Mônica Hirata Sant'anna"}], 17146),
        ([{"id": 69638, "nome": "AM Seabra"}, {"id": 56090, "nome": "AM Seabra"}], 56090),
        ([{"id": 44179, "nome": "SH Guaraldi"}, {"id": 70946, "nome": "SH Guaraldi"}], 44179),
        ([{"id": 22240, "nome": "Lilian Luíza Viana Vieira"}, {"id": 35443, "nome": "Lilian Luíza Viana Vieira"}], 22240),
        ([{"id": 73517, "nome": "M. H. Sant'anna"}, {"id": 69510, "nome": "M. H. Sant'anna"}], 69510),
        ([{"id": 80798, "nome": "Vanilda Cristina Júnior"}, {"id": 61116, "nome": "Vanilda Cristina Júnior"}], 61116),
        ([{"id": 64496, "nome": "SH Guaraldi"}, {"id": 64568, "nome": "SH Guaraldi"}], 64496),
        ([{"id": 99016, "nome": "Sérgio Henrique Guaraldi"}, {"id": 56961, "nome": "Sérgio Henrique Guaraldi"}], 56961),
        ([{"id": 94246, "nome": "Y. V. Faria"}, {"id": 21813, "nome": "Y. V. Faria"}], 21813),
        ([{"id": 18993, "nome": "Vanilda Cristina Júnior"}, {"id": 34920, "nome": "Vanilda Cristina Júnior"}], 18993),
        ([{"id": 19961, "nome": "Sergio Henrique Guaraldi"}, {"id": 76317, "nome": "Sergio Henrique Guaraldi"}], 19961),
        ([{"id": 69087, "nome": "Cassius de Souza"}, {"id": 59372, "nome": "Cassius de Souza"}], 59372)
    ])
    def test_resolucao_id_menor_objeto(self, lista_autores, id_esperado):
        assert self.curador.obter_id_ouro(lista_autores) == id_esperado