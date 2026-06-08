import pytest
from src.curador import (
    CuradorDados, 
    DatasetInvalidoError, 
    RegistroCorrompidoError, 
    RegraNegocioVioladaError
)

@pytest.mark.excecoes
class TestSuiteExcecoesCuradoria:

    def test_deve_lancar_excecao_se_o_dataset_estiver_vazio(self, dados_corrompidos_dinamicos):
        dados_vazios = dados_corrompidos_dinamicos["dataset_vazio"]
        with pytest.raises(DatasetInvalidoError):
            CuradorDados(dados_vazios)

    def test_deve_lancar_excecao_se_faltar_o_campo_id(self, dados_corrompidos_dinamicos):
        dados_sem_id = dados_corrompidos_dinamicos["registro_sem_id"]
        with pytest.raises(RegistroCorrompidoError):
            curador = CuradorDados(dados_sem_id)
            curador.processar_curadoria()

    def test_deve_lancar_excecao_se_faltar_o_campo_nome(self, dados_corrompidos_dinamicos):
        dados_sem_nome = dados_corrompidos_dinamicos["registro_sem_nome"]
        with pytest.raises(RegistroCorrompidoError):
            curador = CuradorDados(dados_sem_nome)
            curador.processar_curadoria()

    def test_deve_lancar_excecao_se_o_tipo_do_id_nao_for_inteiro(self, dados_corrompidos_dinamicos):
        dados_id_string = dados_corrompidos_dinamicos["id_tipo_invalido"]
        with pytest.raises(TypeError):
            curador = CuradorDados(dados_id_string)
            curador.processar_curadoria()

    @pytest.mark.parametrize("chave_cenario", ["idade_negativa", "idade_extrema"])
    def test_deve_lancar_excecao_para_idades_fora_do_limite_biologico(self, dados_corrompidos_dinamicos, chave_cenario):
        dados_ruins = dados_corrompidos_dinamicos[chave_cenario]
        with pytest.raises(RegraNegocioVioladaError):
            curador = CuradorDados(dados_ruins)
            curador.processar_curadoria()

    def test_deve_lancar_excecao_se_o_email_nao_possuir_arroba(self, dados_corrompidos_dinamicos):
        dados_ruins = dados_corrompidos_dinamicos["email_invalido"]
        with pytest.raises(RegraNegocioVioladaError):
            curador = CuradorDados(dados_ruins)
            curador.processar_curadoria()

    def test_deve_lancar_excecao_se_o_orcid_tiver_comprimento_errado(self, dados_corrompidos_dinamicos):
        dados_ruins = dados_corrompidos_dinamicos["orcid_curto"]
        with pytest.raises(RegraNegocioVioladaError):
            curador = CuradorDados(dados_ruins)
            curador.processar_curadoria()