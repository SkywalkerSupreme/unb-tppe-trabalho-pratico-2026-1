import pytest
from src.curador import Curador

@pytest.mark.caso4
@pytest.mark.agrupados
class TestCaso4Agrupados:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.curador = Curador()

    @pytest.mark.parametrize("lista_in, lista_out", [
        (["VC Junior", "Vanilda Cristina Junior"], ["Vanilda Cristina Junior", "Vanilda Cristina Junior"]),
        (["SH Guaraldi", "Sérgio Henrique Guaraldi"], ["Sérgio Henrique Guaraldi", "Sérgio Henrique Guaraldi"]),
        (["AM Seabra", "Ana de Mattos Seabra"], ["Ana de Mattos Seabra", "Ana de Mattos Seabra"]),
        (["CSouza", "Cassius de Souza"], ["Cassius de Souza", "Cassius de Souza"]),
        (["VOMoreira", "Verônica de Oliveira Moreira"], ["Verônica de Oliveira Moreira", "Verônica de Oliveira Moreira"]),
        (["LOSouza", "Luiz de Oliveira de Souza"], ["Luiz de Oliveira de Souza", "Luiz de Oliveira de Souza"]),
        (["LLVVieira", "Lílian Luíza Viana Vieira"], ["Lílian Luíza Viana Vieira", "Lílian Luíza Viana Vieira"]),
        (["YVFaria", "Yuri Vieira Faria"], ["Yuri Vieira Faria", "Yuri Vieira Faria"]),
        (["MHSant'anna", "Mônica Hirata Sant'anna"], ["Mônica Hirata Sant'anna", "Mônica Hirata Sant'anna"]),
        (["RGViana", "Raphael Gonçalves Viana"], ["Raphael Gonçalves Viana", "Raphael Gonçalves Viana"])
    ])
    def test_iniciais_agrupadas_sem_espaco(self, lista_in, lista_out):
        assert self.curador.curar_agrupados(lista_in) == lista_out

    @pytest.mark.parametrize("lista_in, lista_out", [
        (["V.C. Junior", "Vanilda Cristina Junior"], ["Vanilda Cristina Junior", "Vanilda Cristina Junior"]),
        (["S.H. Guaraldi", "Sérgio Henrique Guaraldi"], ["Sérgio Henrique Guaraldi", "Sérgio Henrique Guaraldi"]),
        (["A.M. Seabra", "Ana de Mattos Seabra"], ["Ana de Mattos Seabra", "Ana de Mattos Seabra"]),
        (["C.S. Souza", "Cassius de Souza"], ["Cassius de Souza", "Cassius de Souza"]),
        (["V.O.M. Moreira", "Verônica de Oliveira Moreira"], ["Verônica de Oliveira Moreira", "Verônica de Oliveira Moreira"]),
        (["L.O. Souza", "Luiz de Oliveira de Souza"], ["Luiz de Oliveira de Souza", "Luiz de Oliveira de Souza"]),
        (["L.L.V. Vieira", "Lílian Luíza Viana Vieira"], ["Lílian Luíza Viana Vieira", "Lílian Luíza Viana Vieira"]),
        (["Y.V. Faria", "Yuri Vieira Faria"], ["Yuri Vieira Faria", "Yuri Vieira Faria"]),
        (["M.H. Sant'anna", "Mônica Hirata Sant'anna"], ["Mônica Hirata Sant'anna", "Mônica Hirata Sant'anna"]),
        (["R.G. Viana", "Raphael Gonçalves Viana"], ["Raphael Gonçalves Viana", "Raphael Gonçalves Viana"])
    ])
    def test_iniciais_agrupadas_com_pontos(self, lista_in, lista_out):
        assert self.curador.curar_agrupados(lista_in) == lista_out

    @pytest.mark.parametrize("lista_in, lista_out", [
        (["vc junior", "Vanilda Cristina Junior"], ["Vanilda Cristina Junior", "Vanilda Cristina Junior"]),
        (["sh guaraldi", "Sérgio Henrique Guaraldi"], ["Sérgio Henrique Guaraldi", "Sérgio Henrique Guaraldi"]),
        (["am seabra", "Ana de Mattos Seabra"], ["Ana de Mattos Seabra", "Ana de Mattos Seabra"]),
        (["c.s. de souza", "Cassius de Souza"], ["Cassius de Souza", "Cassius de Souza"]),
        (["v.o. moreira", "Verônica de Oliveira Moreira"], ["Verônica de Oliveira Moreira", "Verônica de Oliveira Moreira"]),
        (["l.o. de souza", "Luiz de Oliveira de Souza"], ["Luiz de Oliveira de Souza", "Luiz de Oliveira de Souza"]),
        (["l.l.v. vieira", "Lílian Luíza Viana Vieira"], ["Lílian Luíza Viana Vieira", "Lílian Luíza Viana Vieira"]),
        (["y.v. faria", "Yuri Vieira Faria"], ["Yuri Vieira Faria", "Yuri Vieira Faria"]),
        (["m.h. sant'anna", "Mônica Hirata Sant'anna"], ["Mônica Hirata Sant'anna", "Mônica Hirata Sant'anna"]),
        (["r.g. viana", "Raphael Gonçalves Viana"], ["Raphael Gonçalves Viana", "Raphael Gonçalves Viana"])
    ])
    def test_iniciais_agrupadas_caixa_baixa(self, lista_in, lista_out):
        assert self.curador.curar_agrupados(lista_in) == lista_out