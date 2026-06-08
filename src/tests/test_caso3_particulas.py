import pytest
from src.curador import LimpadorParticulas

@pytest.mark.caso3
class TestSuiteCaso3Particulas:

    @pytest.mark.parametrize("autor_id, descricao_cenario", [
        (28367, "Luiz Oliveira Souza - Omissão do 'de' índice 194"),
        (72773, "Luiz Oliveira Souza - Omissão do 'de' índice 200"),
        (63963, "Luiz Oliveira Souza - Omissão do 'de' índice 252"),
        (95823, "Ana Mattos Seabra - Omissão do 'de' índice 82"),
        (47700, "Ana Mattos Seabra - Omissão do 'de' índice 87"),
        (58623, "Ana Mattos Seabra - Omissão do 'de' índice 148"),
        (96235, "Ana Mattos Seabra - Omissão do 'de' índice 440"),
        (87992, "Cassius Souza - Omissão do 'de' índice 24"),
        (93066, "Cassius Souza - Omissão do 'de' índice 84"),
        (96760, "Cassius Souza - Omissão do 'de' índice 129"),
        (38298, "Cassius Souza - Omissão do 'de' índice 442"),
        (48382, "Cassius Souza - Omissão do 'de' índice 484"),
        (74332, "Luiz de O. de Souza - Ponto intermediário índice 59"),
        (98395, "Luiz de O. de Souza - Ponto intermediário índice 93"),
        (71814, "Luiz de O. de Souza - Ponto intermediário índice 171"),
        (51934, "Luiz de O. de Souza - Ponto intermediário índice 264")
    ])
    def test_deve_padronizar_particulas_e_pontos_opcionais_do_json(self, datasets, autor_id, descricao_cenario):
        dados_ruins, gabarito = datasets
        
        registro_sujo = next((item for item in dados_ruins if item["id"] == autor_id), None)
        assert registro_sujo is not None, f"Erro: ID {autor_id} não encontrado."
        
        registro_gabarito = next((item for item in gabarito if item["nome_original"] == registro_sujo["nome"]), None)
        assert registro_gabarito is not None, f"Erro: Mapeamento de '{registro_sujo['nome']}' não encontrado."
        
        limpador = LimpadorParticulas()
        nome_processado = limpador.padronizar_particulas(registro_sujo["nome"])
        
        assert nome_processado == registro_gabarito["nome_canonico"], (
            f"Falha ({descricao_cenario}). Esperado: '{registro_gabarito['nome_canonico']}' | Retornado: '{nome_processado}'"
        )

    @pytest.mark.parametrize("autor_id", [28367, 95823, 87992, 74332])
    def test_deve_garantir_que_a_padronizacao_nao_gere_efeitos_colaterais(self, datasets, autor_id):
        dados_ruins, _ = datasets
        registro_original = next(item for item in dados_ruins if item["id"] == autor_id)
        
        limpador = LimpadorParticulas()
        nome_corrigido = limpador.padronizar_particulas(registro_original["nome"])
        
        registro_processado = registro_original.copy()
        registro_processado["nome"] = nome_corrigido
        
        campos_obrigatorios = ["idade", "sexo", "profissao", "email", "orcid", "instituicao", "area_pesquisa"]
        
        for campo in campos_obrigatorios:
            assert registro_processado[campo] == registro_original[campo]

    def test_deve_garantir_que_nenhum_nome_corrigido_termine_com_ponto_final(self, datasets):
        dados_ruins, _ = datasets
        limpador = LimpadorParticulas()
        
        for registro in dados_ruins[:150]:
            if "Souza" in registro["nome"] or "Seabra" in registro["nome"]:
                nome_corrigido = limpador.padronizar_particulas(registro["nome"])
                assert not nome_corrigido.endswith(".")