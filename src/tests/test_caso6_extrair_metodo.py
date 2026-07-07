import pytest
from src.curador import Curador


@pytest.mark.caso2
@pytest.mark.refatoracao
class TestExtrairMetodoAssinatura:
    """Testes da refatoração Extrair Método sobre Curador::assinatura().
    """

    @pytest.fixture(autouse=True)
    def setup(self):
        self.curador = Curador()

    # ---- _tokenizar_nome -------------------------------------------------

    @pytest.mark.parametrize("nome, tokens_esperados, invertido_esperado", [
        ("Ana de Mattos Seabra", ["ANA", "MATTOS", "SEABRA"], False),
        ("Souza, L. O.", ["SOUZA", "L.", "O."], True),
        ("Verônica de Oliveira Moreira", ["VERONICA", "OLIVEIRA", "MOREIRA"], False),
        ("Luiz de O de Souza", ["LUIZ", "O", "SOUZA"], False),
        ("Seabra, A. M.", ["SEABRA", "A.", "M."], True),
    ])
    def test_tokenizar_remove_particulas_acentos_e_detecta_virgula(
        self, nome, tokens_esperados, invertido_esperado
    ):
        tokens, invertido = self.curador._tokenizar_nome(nome)
        assert tokens == tokens_esperados
        assert invertido is invertido_esperado

    @pytest.mark.parametrize("nome", ["", "   ", "de da do dos das"])
    def test_tokenizar_entrada_vazia_ou_so_particulas(self, nome):
        tokens, _ = self.curador._tokenizar_nome(nome)
        assert tokens == []

    # ---- _extrair_sobrenome ---------------------------------------------

    def test_extrair_sobrenome_invertido_por_virgula(self):
        # Com vírgula, o primeiro token é o sobrenome
        sobrenome, restantes = self.curador._extrair_sobrenome(
            ["SOUZA", "L.", "O."], True
        )
        assert sobrenome == "SOUZA"
        assert restantes == ["L.", "O."]

    def test_extrair_sobrenome_com_iniciais_no_final(self):
        # Sem vírgula, mas com iniciais ao final
        sobrenome, restantes = self.curador._extrair_sobrenome(
            ["SEABRA", "A.", "M."], False
        )
        assert sobrenome == "SEABRA"
        assert restantes == ["A.", "M."]

    def test_extrair_sobrenome_ordem_natural(self):
        # Nome completo em ordem natural
        sobrenome, restantes = self.curador._extrair_sobrenome(
            ["ANA", "MATTOS", "SEABRA"], False
        )
        assert sobrenome == "SEABRA"
        assert restantes == ["ANA", "MATTOS"]

    def test_extrair_sobrenome_preserva_ordem_dos_restantes(self):
        _, restantes = self.curador._extrair_sobrenome(
            ["LUIZ", "OLIVEIRA", "SOUZA"], False
        )
        assert restantes == ["LUIZ", "OLIVEIRA"]

    # ---- _obter_primeira_inicial ----------------------------------------

    @pytest.mark.parametrize("restantes, esperado", [
        (["ANA", "MATTOS"], "A"),
        (["A.", "M."], "A"),
        (["A.M."], "A"),
        (["L.", "O."], "L"),
        (["OLIVEIRA"], "O"),
        ([], ""),
    ])
    def test_obter_primeira_inicial(self, restantes, esperado):
        assert self.curador._obter_primeira_inicial(restantes) == esperado

    def test_obter_primeira_inicial_ignora_tokens_vazios(self):
        assert self.curador._obter_primeira_inicial(["", "ANA"]) == "A"

    # ---- assinatura (composição) ----------------------------------------

    @pytest.mark.parametrize("nome, assinatura_esperada", [
        ("Ana de Mattos Seabra", "SEABRA|A"),
        ("Seabra, A. M.", "SEABRA|A"),
        ("Souza, L. O.", "SOUZA|L"),
        ("Cassius de Souza", "SOUZA|C"),
        ("Sérgio Henrique Guaraldi", "GUARALDI|S"),
    ])
    def test_assinatura_apos_refatoracao(self, nome, assinatura_esperada):
        assert self.curador.assinatura(nome) == assinatura_esperada

    def test_assinatura_nome_sem_tokens_uteis(self):
        assert self.curador.assinatura("de da do") == ""

    def test_signature_delega_para_assinatura(self):
        assert self.curador.signature("Ana de Mattos Seabra") == \
            self.curador.assinatura("Ana de Mattos Seabra")

    @pytest.mark.parametrize("nome_a, nome_b", [
        ("Raphael Goncalves Viana", "Raphael Gonçalves Viana"),
        ("Cassius de Souza", "Souza C."),
        ("Verônica de Oliveira Moreira", "Moreira V O"),
        ("Ana de Mattos Seabra", "A. M. Seabra"),
    ])
    def test_assinaturas_equivalentes_colidem(self, nome_a, nome_b):
        # Variações do mesmo autor devem gerar a mesma assinatura (dedup).
        assert self.curador.assinatura(nome_a) == self.curador.assinatura(nome_b)