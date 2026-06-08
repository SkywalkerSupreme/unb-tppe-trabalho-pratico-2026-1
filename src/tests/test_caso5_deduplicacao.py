import pytest
from src.curador import CuradorDados

@pytest.mark.caso5
class TestSuiteCaso5Deduplicacao:

    @pytest.mark.parametrize("id_duplicado_alto, id_canonico_esperado, nome_autor", [
        (746938, 30000, "Raphael Gonçalves Viana"),
        (608297, 30000, "Raphael Gonçalves Viana"),
        (549243, 30000, "Raphael Gonçalves Viana"),
        (92397, 30001, "Lílian Luíza Viana Vieira"),
        (96951, 30001, "Lílian Luíza Viana Vieira"),
        (38657, 30002, "Ana de Mattos Seabra"),
        (14207, 30002, "Ana de Mattos Seabra")
    ])
    def test_deve_unificar_registros_duplicados_para_o_id_canonico_do_gabarito(self, datasets, id_duplicado_alto, id_canonico_esperado, nome_autor):
        dados_ruins, _ = datasets
        
        curador = CuradorDados(dados_ruins)
        dados_processados = curador.processar_curadoria()
        
        # O ID sujo/alto antigo deve deixar de existir de forma isolada
        registro_com_id_antigo = next((item for item in dados_processados if item["id"] == id_duplicado_alto), None)
        assert registro_com_id_antigo is None, f"Falha: O ID duplicado {id_duplicado_alto} ({nome_autor}) não foi unificado."

    @pytest.mark.parametrize("id_canonico", [30000, 30001, 30002])
    def test_deve_garantir_que_os_ids_canonicos_principais_existam_pos_processamento(self, datasets, id_canonico):
        dados_ruins, gabarito = datasets
        
        curador = CuradorDados(dados_ruins)
        dados_processados = curador.processar_curadoria()
        
        registro_sistema = next((item for item in dados_processados if item["id"] == id_canonico), None)
        registro_gabarito = next((item for item in gabarito if item["id_canonico"] == id_canonico), None)
        
        assert registro_sistema is not None, f"Erro: O ID canônico {id_canonico} desapareceu da tabela limpa."
        assert registro_sistema["nome"] == registro_gabarito["nome_canonico"]

    def test_deve_garantir_que_a_deduplicacao_nao_altere_metadados_essenciais(self, datasets):
        dados_ruins, _ = datasets
        
        curador = CuradorDados(dados_ruins)
        dados_processados = curador.processar_curadoria()
        
        # Verifica se campos obrigatórios continuam existindo nos registros processados
        campos_obrigatorios = ["idade", "sexo", "profissao", "email", "orcid", "instituicao", "area_pesquisa"]
        for registro in dados_processados[:30]:
            for campo in campos_obrigatorios:
                assert campo in registro

    def test_deve_garantir_que_a_unificacao_nao_altere_tipagem_dos_ids(self, datasets):
        dados_ruins, _ = datasets
        
        curador = CuradorDados(dados_ruins)
        dados_processados = curador.processar_curadoria()
        
        for registro in dados_processados[:50]:
            assert isinstance(registro["id"], int)