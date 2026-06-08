# ==============================================================================
# CLASSES DE EXCEÇÃO (REGRAS DE ERRO)
# ==============================================================================
class CuradorError(Exception):
    """Exceção base para o sistema de curadoria."""
    pass

class DatasetInvalidoError(CuradorError):
    """Lançada quando o dataset fornecido está vazio."""
    pass

class RegistroCorrompidoError(CuradorError):
    """Lançada quando falta o ID ou o NOME de alguém na tabela."""
    pass

class RegraNegocioVioladaError(CuradorError):
    """Lançada quando os dados contêm valores impossíveis."""
    pass


# ==============================================================================
# CLASSES DO SISTEMA DE CURADORIA
# ==============================================================================
class CuradorDados:
    """Classe Principal Orquestradora encarregada da pipeline."""
    def __init__(self, dados_originais: list):
        if dados_originais is None or len(dados_originais) == 0:
            raise DatasetInvalidoError("Erro: O dataset fornecido está completamente vazio.")
        self.dados = dados_originais

    def processar_curadoria(self) -> list:
        dados_processados = []
        for registro in self.dados:
            if "id" not in registro:
                raise RegistroCorrompidoError("Campo obrigatório 'id' ausente no registro.")
            if "nome" not in registro:
                raise RegistroCorrompidoError("Campo obrigatório 'nome' ausente no registro.")
            if not isinstance(registro["id"], int):
                raise TypeError("O campo 'id' deve ser um número inteiro.")
                
            if "idade" in registro and (registro["idade"] <= 0 or registro["idade"] > 120):
                raise RegraNegocioVioladaError(f"Idade inválida detectada ({registro['idade']}).")
            if "email" in registro and "@" not in registro["email"]:
                raise RegraNegocioVioladaError(f"Formato de e-mail inválido ({registro['email']}).")

            # Retorna os dados (fará os asserts falharem no início do TDD)
            dados_processados.append(registro)
        return dados_processados


class LimpadorTipografico:
    """Unidade do Caso 1: Trata erros tipográficos."""
    def limpar_texto(self, nome_sujo: str) -> str:
        return nome_sujo


class LimpadorIniciais:
    """Unidade do Caso 2: Expande iniciais."""
    def expandir_iniciais(self, nome_sujo: str) -> str:
        return nome_sujo


class LimpadorParticulas:
    """Unidade do Caso 3: Resolve partículas de ligação."""
    def padronizar_particulas(self, nome_sujo: str) -> str:
        return nome_sujo


class LimpadorIniciaisAgrupadas:
    """Unidade do Caso 4: Resolve iniciais aglutinadas (ex: SH, VC)."""
    def expandir_agrupados(self, nome_sujo: str) -> str:
        return nome_sujo