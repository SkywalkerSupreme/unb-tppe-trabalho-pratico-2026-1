# [Refact] Extrair Classe: Curador


class FormatoInvalidoError(Exception):
    pass


class IdInvalidoError(Exception):
    pass


class ValidadorRegistros:
    """
    CLASSE EXTRAÍDA (Refatoração: Extrair Classe)
    Responsável exclusiva pela validação de contrato e integridade estrutural
    dos registros de entrada (campos obrigatórios, tipagem e regras de ID)
    """

    def processar_base_dados(self, dados):
        if dados is None:
            raise FormatoInvalidoError()

        if isinstance(dados, list) and len(dados) == 0:
            raise FormatoInvalidoError()

        for registro in dados:
            if not isinstance(registro, dict):
                raise FormatoInvalidoError()

            if "id" not in registro:
                raise FormatoInvalidoError()

            if "nome" not in registro:
                raise FormatoInvalidoError()

            id_atual = registro["id"]
            if not isinstance(id_atual, int):
                raise FormatoInvalidoError()

            if id_atual <= 0:
                raise IdInvalidoError()

        return True

    def obter_id_ouro(self, autores):
        if autores is None:
            return None

        ids = []
        for autor in autores:
            if isinstance(autor, dict):
                id_registro = autor.get("id")
            else:
                id_registro = None

            if id_registro is None:
                raise IdInvalidoError()

            if not isinstance(id_registro, int):
                raise IdInvalidoError()

            if id_registro <= 0:
                raise IdInvalidoError()

            ids.append(id_registro)

        if len(ids) == 0:
            return None

        return min(ids)