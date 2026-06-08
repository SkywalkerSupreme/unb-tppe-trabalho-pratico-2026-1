import pytest
from src.curador import LimpadorIniciaisAgrupadas

@pytest.mark.caso4
class TestSuiteCaso4IniciaisAgrupadas:
    """Suíte para o Caso 4: Iniciais agrupadas (SH, VC)."""

    @pytest.mark.parametrize("autor_id, descricao_cenario", [
        (44179, "SH Guaraldi - Iniciais de Sérgio Henrique"),
        (70946, "SH Guaraldi - Segunda ocorrência"),
        (51505, "VC Junior - Iniciais de Vanilda Cristina"),
        (45986, "VC Junior - Terceira ocorrência")
    ])
    def test_deve_identificar_e_expandir_iniciais_agrupadas_do_json(self, datasets, autor_id, descricao_cenario):
        dados_ruins, gabarito = datasets
        
        registro_sujo = next(item for item in dados_ruins if item["id"] == autor_id)
        registro_gabarito = next((item for item in gabarito if item["nome_original"] == registro_sujo["nome"]), None)
        
        assert registro_gabarito is not None, f"Erro: Nome '{registro_sujo['nome']}' não mapeado no gabarito."
        
        limpador = LimpadorIniciaisAgrupadas()
        nome_processado = limpador.expandir_agrupados(registro_sujo["nome"])
        
        assert nome_processado == registro_gabarito["nome_canonico"]

    def test_deve_garantir_comprimento_minimo_do_nome_expandido(self, datasets):
        dados_ruins, _ = datasets
        limpador = LimpadorIniciaisAgrupadas()
        for registro in dados_ruins[:100]:
            if "SH" in registro["nome"] or "VC" in registro["nome"]:
                nome_corrigido = limpador.expandir_agrupados(registro["nome"])
                assert len(nome_corrigido) > 5