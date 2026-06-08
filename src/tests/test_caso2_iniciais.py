import pytest
from src.curador import Curador

@pytest.mark.caso2
@pytest.mark.iniciais
class TestCaso2Iniciais:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.curador = Curador()

    @pytest.mark.parametrize("lista_in, lista_out", [
        (["Seabra A. M.", "Ana de Mattos Seabra"], ["Ana de Mattos Seabra", "Ana de Mattos Seabra"]),
        (["Souza C.", "Cassius de Souza"], ["Cassius de Souza", "Cassius de Souza"]),
        (["Moreira V. de O.", "Verônica de Oliveira Moreira"], ["Verônica de Oliveira Moreira", "Verônica de Oliveira Moreira"]),
        (["Souza, L. O.", "Luiz de Oliveira de Souza"], ["Luiz de Oliveira de Souza", "Luiz de Oliveira de Souza"]),
        (["Guaraldi S. H.", "Sérgio Henrique Guaraldi"], ["Sérgio Henrique Guaraldi", "Sérgio Henrique Guaraldi"]),
        (["Vieira L. L. V.", "Lílian Luíza Viana Vieira"], ["Lílian Luíza Viana Vieira", "Lílian Luíza Viana Vieira"]),
        (["Faria Y. V.", "Yuri Vieira Faria"], ["Yuri Vieira Faria", "Yuri Vieira Faria"]),
        (["Sant'anna M. H.", "Mônica Hirata Sant'anna"], ["Mônica Hirata Sant'anna", "Mônica Hirata Sant'anna"]),
        (["Viana R. G.", "Raphael Gonçalves Viana"], ["Raphael Gonçalves Viana", "Raphael Gonçalves Viana"]),
        (["Moreira V. O.", "Veronica de Oliveira Moreira"], ["Veronica de Oliveira Moreira", "Veronica de Oliveira Moreira"])
    ])
    def test_iniciais_com_pontos(self, lista_in, lista_out):
        assert self.curador.curar_iniciais(lista_in) == lista_out

    @pytest.mark.parametrize("lista_in, lista_out", [
        (["Seabra A M", "Ana de Mattos Seabra"], ["Ana de Mattos Seabra", "Ana de Mattos Seabra"]),
        (["Souza C", "Cassius de Souza"], ["Cassius de Souza", "Cassius de Souza"]),
        (["Moreira V de O", "Verônica de Oliveira Moreira"], ["Verônica de Oliveira Moreira", "Verônica de Oliveira Moreira"]),
        (["Souza L O", "Luiz de Oliveira de Souza"], ["Luiz de Oliveira de Souza", "Luiz de Oliveira de Souza"]),
        (["Guaraldi S H", "Sérgio Henrique Guaraldi"], ["Sérgio Henrique Guaraldi", "Sérgio Henrique Guaraldi"]),
        (["Vieira L L V", "Lílian Luíza Viana Vieira"], ["Lílian Luíza Viana Vieira", "Lílian Luíza Viana Vieira"]),
        (["Faria Y V", "Yuri Vieira Faria"], ["Yuri Vieira Faria", "Yuri Vieira Faria"]),
        (["Sant'anna M H", "Mônica Hirata Sant'anna"], ["Mônica Hirata Sant'anna", "Mônica Hirata Sant'anna"]),
        (["Viana R G", "Raphael Gonçalves Viana"], ["Raphael Gonçalves Viana", "Raphael Gonçalves Viana"]),
        (["Moreira V O", "Veronica de Oliveira Moreira"], ["Veronica de Oliveira Moreira", "Veronica de Oliveira Moreira"])
    ])
    def test_iniciais_sem_pontos(self, lista_in, lista_out):
        assert self.curador.curar_iniciais(lista_in) == lista_out

    @pytest.mark.parametrize("lista_in, lista_out", [
        (["Seabra, A.M.", "Ana de Mattos Seabra"], ["Ana de Mattos Seabra", "Ana de Mattos Seabra"]),
        (["Souza, C.", "Cassius de Souza"], ["Cassius de Souza", "Cassius de Souza"]),
        (["Moreira, V.O.", "Verônica de Oliveira Moreira"], ["Verônica de Oliveira Moreira", "Verônica de Oliveira Moreira"]),
        (["Guaraldi, S.H.", "Sérgio Henrique Guaraldi"], ["Sérgio Henrique Guaraldi", "Sérgio Henrique Guaraldi"]),
        (["Vieira, L.L.V.", "Lílian Luíza Viana Vieira"], ["Lílian Luíza Viana Vieira", "Lílian Luíza Viana Vieira"]),
        (["Faria, Y.V.", "Yuri Vieira Faria"], ["Yuri Vieira Faria", "Yuri Vieira Faria"]),
        (["Sant'anna, M.H.", "Mônica Hirata Sant'anna"], ["Mônica Hirata Sant'anna", "Mônica Hirata Sant'anna"]),
        (["Viana, R.G.", "Raphael Gonçalves Viana"], ["Raphael Gonçalves Viana", "Raphael Gonçalves Viana"]),
        (["Moreira, V. de O.", "Veronica de Oliveira Moreira"], ["Veronica de Oliveira Moreira", "Veronica de Oliveira Moreira"]),
        (["Junior, V.C.", "Vanilda Cristina Junior"], ["Vanilda Cristina Junior", "Vanilda Cristina Junior"]),
        (["Júnior, V. C.", "Vanilda Cristina Júnior"], ["Vanilda Cristina Júnior", "Vanilda Cristina Júnior"]),
        (["Seabra, A. M.", "Ana Mattos Seabra"], ["Ana Mattos Seabra", "Ana Mattos Seabra"])
    ])
    def test_sobrenome_com_virgula_e_iniciais(self, lista_in, lista_out):
        assert self.curador.curar_iniciais(lista_in) == lista_out