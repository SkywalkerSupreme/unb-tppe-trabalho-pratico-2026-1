import pytest
from src.curador import LimpadorIniciais

@pytest.mark.caso2
class TestSuiteCaso2Iniciais:

    @pytest.mark.parametrize("autor_id, descricao_cenario", [
        (77391, "A. M. Seabra - Tradicional com pontos"),
        (17944, "A. M. Seabra - Segunda ocorrência com pontos"),
        (43544, "A. M. Seabra - Terceira ocorrência com pontos"),
        (51365, "A. M. Seabra - Quarta ocorrência com pontos"),
        (70637, "V. de O. Moreira - Mantendo a partícula 'de'"),
        (86350, "V. de O. Moreira - Segunda ocorrência pontuada"),
        (15014, "V. de O. Moreira - Terceira ocorrência pontuada"),
        (31798, "Seabra A. M. - Sobrenome primeiro e pontuado no fim"),
        (99399, "Seabra A. M. - Segunda ocorrência invertida"),
        (57516, "Seabra A. M. - Terceira ocorrência invertida"),
        (69638, "AM Seabra - Iniciais grudadas sem pontos"),
        (56090, "AM Seabra - Segunda ocorrência sem pontos"),
        (45811, "AM Seabra - Terceira ocorrência sem pontos"),
        (80010, "Souza C. - Sobrenome e inicial isolada com ponto"),
        (30632, "Souza C. - Segunda ocorrência de inicial isolada"),
        (33053, "Souza C. - Terceira ocorrência de inicial isolada")
    ])
    def test_deve_expandir_iniciais_e_abreviacoes_para_nome_completo_do_json(self, datasets, autor_id, descricao_cenario):
        dados_ruins, gabarito = datasets
        
        registro_sujo = next((item for item in dados_ruins if item["id"] == autor_id), None)
        assert registro_sujo is not None, f"Erro: ID {autor_id} não encontrado."
        
        registro_gabarito = next((item for item in gabarito if item["nome_original"] == registro_sujo["nome"]), None)
        assert registro_gabarito is not None, f"Erro: Mapeamento de '{registro_sujo['nome']}' não encontrado."
        
        limpador = LimpadorIniciais()
        nome_processado = limpador.expandir_iniciais(registro_sujo["nome"])
        
        assert nome_processado == registro_gabarito["nome_canonico"], (
            f"Falha ({descricao_cenario}). Esperado: '{registro_gabarito['nome_canonico']}' | Retornado: '{nome_processado}'"
        )

    @pytest.mark.parametrize("autor_id", [77391, 70637, 31798, 80010])
    def test_deve_garantir_que_a_expansao_nao_gere_efeitos_colaterais(self, datasets, autor_id):
        dados_ruins, _ = datasets
        registro_original = next(item for item in dados_ruins if item["id"] == autor_id)
        
        limpador = LimpadorIniciais()
        nome_expandido = limpador.expandir_iniciais(registro_original["nome"])
        
        registro_processado = registro_original.copy()
        registro_processado["nome"] = nome_expandido
        
        campos_obrigatorios = ["idade", "sexo", "profissao", "email", "orcid", "instituicao", "area_pesquisa"]
        
        for campo in campos_obrigatorios:
            assert registro_processado[campo] == registro_original[campo]

    def test_deve_garantir_que_nomes_expandidos_nao_tenham_espacos_duplos_internos(self, datasets):
        dados_ruins, _ = datasets
        limpador = LimpadorIniciais()
        
        for registro in dados_ruins[:100]:
            if "Seabra" in registro["nome"] or "Moreira" in registro["nome"]:
                nome_expandido = limpador.expandir_iniciais(registro["nome"])
                assert "  " not in nome_expandido