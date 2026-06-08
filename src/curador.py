class FormatoInvalidoError(Exception):
    pass

class IdInvalidoError(Exception):
    pass

class Curador:
    def curar_tipografia(self, lista_nomes):
        return []

    def curar_iniciais(self, lista_nomes):
        return []

    def curar_particulas(self, lista_nomes):
        return []

    def curar_agrupados(self, lista_nomes):
        return []

    def consolidar_ids(self, dicionario_autores):
        return {}

    def obter_id_ouro(self, lista_autores):
        return 0

    def processar_base_dados(self, dados_base):
        # Lógica inicial para validar formato e IDs nos testes de exceção
        for registro in dados_base:
            if not isinstance(registro, dict) or "id" not in registro or "nome" not in registro:
                raise FormatoInvalidoError()
            if not isinstance(registro["id"], int):
                raise FormatoInvalidoError()
            if registro["id"] <= 0:
                raise IdInvalidoError()
        if not dados_base:
            raise FormatoInvalidoError()
        return []