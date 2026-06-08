import pytest
from src.curador import Curador

@pytest.mark.caso1
@pytest.mark.tipografia
class TestCaso1Tipografia:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.curador = Curador()

    @pytest.mark.parametrize("lista_in, lista_out", [
        (["Sant`anna M. H."], ["Sant'anna M. H."]),
        (["Mônica Hirata Sant’anna"], ["Mônica Hirata Sant'anna"]),
        (["Monica Hirata Sant`anna", "Mônica Hirata Sant’anna"], ["Mônica Hirata Sant'anna", "Mônica Hirata Sant'anna"]),
        (["Sant\`anna M. H.", "Sant'anna M. H."], ["Sant'anna M. H.", "Sant'anna M. H."]),
        (["D’Avila", "D\`Avila", "D'Avila"], ["D'Avila", "D'Avila", "D'Avila"]),
        (["Sant’anna", "Sant`anna"], ["Sant'anna", "Sant'anna"]),
        (["Mônica Hirata Sant\`anna"], ["Mônica Hirata Sant'anna"]),
        (["Sant'anna M. H.", "Sant’anna M. H."], ["Sant'anna M. H.", "Sant'anna M. H."]),
        (["Cox’a"], ["Cox'a"]),
        (["O’Brian", "O`Brian"], ["O'Brian", "O'Brian"])
    ])
    def test_apostrofos_variados(self, lista_in, lista_out):
        assert self.curador.curar_tipografia(lista_in) == lista_out

    @pytest.mark.parametrize("lista_in, lista_out", [
        (["Sergio Henrique Guaraldi", "Sérgio Henrique Guaraldi"], ["Sérgio Henrique Guaraldi", "Sérgio Henrique Guaraldi"]),
        (["Lilian Luíza Viana Vieira", "Lílian Luíza Viana Vieira"], ["Lílian Luíza Viana Vieira", "Lílian Luíza Viana Vieira"]),
        (["Veronica de Oliveira Moreira", "Verônica de Oliveira Moreira"], ["Verônica de Oliveira Moreira", "Verônica de Oliveira Moreira"]),
        (["Raphael Goncalves Viana", "Raphael Gonçalves Viana"], ["Raphael Gonçalves Viana", "Raphael Gonçalves Viana"]),
        (["Vanilda Cristina Junior", "Vanilda Cristina Júnior"], ["Vanilda Cristina Júnior", "Vanilda Cristina Júnior"]),
        (["Monica Hirata Sant'anna", "Mônica Hirata Sant'anna"], ["Mônica Hirata Sant'anna", "Mônica Hirata Sant'anna"]),
        (["Sergio Henrique Guaraldi"], ["Sergio Henrique Guaraldi"]),
        (["Sérgio Henrique Guaraldi"], ["Sérgio Henrique Guaraldi"]),
        (["Lilian Luiza Viana Vieira", "Lílian Luíza Viana Vieira"], ["Lílian Luíza Viana Vieira", "Lílian Luíza Viana Vieira"]),
        (["Yuri Vieira Faria", "Yúri Vieira Faria"], ["Yuri Vieira Faria", "Yuri Vieira Faria"]),
        (["Cassius de Souza", "Cássius de Souza"], ["Cassius de Souza", "Cassius de Souza"]),
        (["Luiz Oliveira Souza", "Luíz Oliveira Souza"], ["Luiz Oliveira Souza", "Luiz Oliveira Souza"])
    ])
    def test_acentuacao_predominante(self, lista_in, lista_out):
        assert self.curador.curar_tipografia(lista_in) == lista_out

    @pytest.mark.parametrize("lista_in, lista_out", [
        (["sergio henrique guaraldi", "Sérgio Henrique Guaraldi"], ["Sérgio Henrique Guaraldi", "Sérgio Henrique Guaraldi"]),
        (["MÔNICA HIRATA SANT'ANNA", "Mônica Hirata Sant'anna"], ["Mônica Hirata Sant'anna", "Mônica Hirata Sant'anna"]),
        (["LÍLIAN LUÍZA VIANA VIEIRA"], ["Lílian Luíza Viana Vieira"]),
        (["veronica de oliveira moreira", "VERÔNICA DE OLIVEIRA MOREIRA"], ["Verônica de Oliveira Moreira", "Verônica de Oliveira Moreira"]),
        (["RAPHAEL GONÇALVES VIANA", "Raphael Goncalves Viana"], ["Raphael Gonçalves Viana", "Raphael Gonçalves Viana"]),
        (["vanilda cristina júnior", "Vanilda Cristina Junior"], ["Vanilda Cristina Júnior", "Vanilda Cristina Júnior"]),
        (["ANA DE MATTOS SEABRA", "ana de mattos seabra"], ["Ana de Mattos Seabra", "Ana de Mattos Seabra"]),
        (["CASSIUS DE SOUZA"], ["Cassius de Souza"]),
        (["YURI VIEIRA FARIA", "yuri vieira faria"], ["Yuri Vieira Faria", "Yuri Vieira Faria"]),
        (["LUIZ OLIVEIRA SOUZA", "Luiz Oliveira Souza"], ["Luiz Oliveira Souza", "Luiz Oliveira Souza"])
    ])
    def test_padronizacao_caixa(self, lista_in, lista_out):
        assert self.curador.curar_tipografia(lista_in) == lista_out

    @pytest.mark.parametrize("lista_in, lista_out", [
        (["Sérgio  Henrique  Guaraldi", "Sérgio Henrique Guaraldi"], ["Sérgio Henrique Guaraldi", "Sérgio Henrique Guaraldi"]),
        ([" Mônica Hirata Sant'anna "], ["Mônica Hirata Sant'anna"]),
        (["Lílian Luíza Viana Vieira  "], ["Lílian Luíza Viana Vieira"]),
        (["   Verônica de Oliveira Moreira"], ["Verônica de Oliveira Moreira"]),
        (["Raphael   Gonçalves   Viana", "Raphael Gonçalves Viana"], ["Raphael Gonçalves Viana", "Raphael Gonçalves Viana"]),
        (["Vanilda  Cristina  Júnior "], ["Vanilda Cristina Júnior"]),
        (["Ana de Mattos Seabra  ", "  Ana de Mattos Seabra"], ["Ana de Mattos Seabra", "Ana de Mattos Seabra"]),
        ([" Cassius de Souza "], ["Cassius de Souza"]),
        (["Yuri  Vieira  Faria"], ["Yuri Vieira Faria"]),
        (["Luiz   Oliveira   Souza"], ["Luiz Oliveira Souza"])
    ])
    def test_limpeza_espacos_sobressalentes(self, lista_in, lista_out):
        assert self.curador.curar_tipografia(lista_in) == lista_out