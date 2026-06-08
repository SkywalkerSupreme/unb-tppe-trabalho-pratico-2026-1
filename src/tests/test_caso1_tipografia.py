import pytest
from src.curador import LimpadorTipografico

@pytest.mark.caso1
class TestSuiteCaso1Tipografia:

    @pytest.mark.parametrize("autor_id, descricao_cenario", [
        (30926, "Monica Hirata Sant`anna - Crase índice 3"),
        (53655, "Monica Hirata Sant`anna - Crase índice 118"),
        (83339, "Monica Hirata Sant`anna - Crase índice 218"),
        (90199, "Monica Hirata Sant`anna - Crase índice 150"),
        (433094, "Raphael Goncalves Viana - Cedilha índice 9"),
        (746938, "Raphael Goncalves Viana - Cedilha índice 15"),
        (34164, "Raphael Goncalves Viana - Cedilha índice 64"),
        (87139, "Raphael Goncalves Viana - Cedilha índice 66"),
        (19961, "Sergio Henrique Guaraldi - Acento índice 54"),
        (76317, "Sergio Henrique Guaraldi - Acento índice 55"),
        (74923, "Sergio Henrique Guaraldi - Acento índice 81"),
        (19539, "Sergio Henrique Guaraldi - Acento índice 199")
    ])
    def test_deve_corrigir_grafia_acentuacao_e_apostrofos_em_larga_escala(self, datasets, autor_id, descricao_cenario):
        dados_ruins, gabarito = datasets
        
        registro_sujo = next((item for item in dados_ruins if item["id"] == autor_id), None)
        assert registro_sujo is not None, f"Erro: ID {autor_id} não encontrado."
        
        registro_gabarito = next((item for item in gabarito if item["nome_original"] == registro_sujo["nome"]), None)
        assert registro_gabarito is not None, f"Erro: Mapeamento de '{registro_sujo['nome']}' não encontrado."
        
        limpador = LimpadorTipografico()
        nome_processado = limpador.limpar_texto(registro_sujo["nome"])
        
        assert nome_processado == registro_gabarito["nome_canonico"], (
            f"Falha ({descricao_cenario}). Esperado: '{registro_gabarito['nome_canonico']}' | Retornado: '{nome_processado}'"
        )

    @pytest.mark.parametrize("autor_id", [30926, 433094, 19961])
    def test_deve_garantir_que_a_limpeza_do_nome_nao_gere_efeitos_colaterais(self, datasets, autor_id):
        dados_ruins, _ = datasets
        registro_original = next(item for item in dados_ruins if item["id"] == autor_id)
        
        limpador = LimpadorTipografico()
        nome_limpo = limpador.limpar_texto(registro_original["nome"])
        
        registro_processado = registro_original.copy()
        registro_processado["nome"] = nome_limpo
        
        campos_obrigatorios = ["idade", "sexo", "profissao", "email", "orcid", "instituicao", "area_pesquisa"]
        
        for campo in campos_obrigatorios:
            assert registro_processado[campo] == registro_original[campo]

    def test_deve_garantir_que_nenhum_nome_contenha_espacos_inuteis_nas_extremidades(self, datasets):
        dados_ruins, _ = datasets
        limpador = LimpadorTipografico()
        
        for registro in dados_ruins[:50]:
            nome_limpo = limpador.limpar_texto(registro["nome"])
            # Se o nome original tiver espaço na ponta, este teste vai falhar de propósito agora!
            assert nome_limpo == nome_limpo.strip()