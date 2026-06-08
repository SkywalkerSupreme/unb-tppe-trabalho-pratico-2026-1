# ==============================================================================
# CLASSES DE EXCEÇÃO (REGRAS DE ERRO DO PROGRAMA)
# ==============================================================================
class CuradorError(Exception):
    """Exceção base para o nosso sistema de curadoria científica."""
    pass

class DatasetInvalidoError(CuradorError):
    """Lançada quando a estrutura geral do arquivo/dataset fornecido está vazia."""
    pass

class RegistroCorrompidoError(CuradorError):
    """Lançada quando falta o ID ou o NOME de alguém na tabela."""
    pass

class RegraNegocioVioladaError(CuradorError):
    """Lançada quando os dados contêm valores impossíveis (idade negativa, email sem @)."""
    pass


# ==============================================================================
# CLASSES DO SISTEMA DE CURADORIA
# ==============================================================================
class CuradorDados:
    """
    Classe Principal Orquestradora (Orientação a Objetos).
    Recebe a tabela do JSON e gerencia a pipeline de checagem e limpeza.
    """
    def __init__(self, dados_originais: list):
        # Validação do Dataset exigida no test_excecoes.py
        if dados_originais is None or len(dados_originais) == 0:
            raise DatasetInvalidoError("Erro de Processamento: O dataset fornecido está completamente vazio.")
        self.dados = dados_originais

    def processar_curadoria(self) -> list:
        """Passa os dados pela pipeline de validação e limpeza."""
        dados_processados = []
        
        for registro in self.dados:
            # Validações estruturais exigidas no test_excecoes.py
            if "id" not in registro:
                raise RegistroCorrompidoError("Erro de Integridade: Campo obrigatório 'id' ausente no registro.")
            if "nome" not in registro:
                raise RegistroCorrompidoError("Erro de Integridade: Campo obrigatório 'nome' ausente no registro.")
            if not isinstance(registro["id"], int):
                raise TypeError("Erro de Tipagem: O campo 'id' deve ser obrigatoriamente um número inteiro.")
                
            # Validações das Regras de Negócio avançadas exigidas no test_excecoes.py
            if "idade" in registro and (registro["idade"] <= 0 or registro["idade"] > 120):
                raise RegraNegocioVioladaError(f"Erro de Negócio: Idade inválida detectada ({registro['idade']}).")
            if "email" in registro and "@" not in registro["email"]:
                raise RegraNegocioVioladaError(f"Erro de Negócio: Formato de e-mail inválido ({registro['email']}).")
            if "orcid" in registro and len(registro["orcid"]) != 19:
                raise RegraNegocioVioladaError(f"Erro de Negócio: Formato ou tamanho de ORCID inválido.")

            # Por enquanto, devolve o registro sem alterar o nome
            dados_processados.append(registro)
            
        return dados_processados


class LimpadorTipografico:
    """Unidade do Caso 1: Trata erros tipográficos, acentuação e crases."""
    def limpar_texto(self, nome_sujo: str) -> str:
        return nome_sujo


class LimpadorIniciais:
    """Unidade do Caso 2: Expande iniciais e abreviações intermediárias."""
    def expandir_iniciais(self, nome_sujo: str) -> str:
        return nome_sujo


class LimpadorParticulas:
    """Unidade do Caso 3: Padroniza o uso das partículas 'de'."""
    def padronizar_particulas(self, nome_sujo: str) -> str:
        return nome_sujo


class LimpadorIniciaisAgrupadas:
    """Unidade do Caso 4: Resolve iniciais aglutinadas (ex: SH, VC)."""
    def expandir_agrupados(self, nome_sujo: str) -> str:
        return nome_sujo