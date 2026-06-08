# src/curador.py

import re
import unicodedata


class FormatoInvalidoError(Exception):
    pass


class IdInvalidoError(Exception):
    pass


PARTICULAS = {
    "de", "da", "do", "das", "dos"
}


class Curador:


    # FUNÇÕES AUXILIARES


    def remover_acentos(self, texto):
        return "".join(
            c for c in unicodedata.normalize("NFD", texto)
            if unicodedata.category(c) != "Mn"
        )

    def limpar_apostrofos(self, texto):
        return (
            texto.replace("\\`", "'")
                 .replace("`", "'")
                 .replace("´", "'")
                 .replace("’", "'")
                 .replace("‘", "'")
        )

    def limpar_espacos(self, texto):
        return " ".join(texto.strip().split())

    def normalizar_caixa(self, texto):

        palavras = []

        for p in texto.split():

            if p.lower() in PARTICULAS:
                palavras.append(p.lower())
            elif "'" in p:
                prefix, _, suffix = p.partition("'")
                # O' and D' prefixes are single-char: capitalize the independent word after.
                # Multi-char prefixes like Sant' are compound: lowercase the ending.
                suffix_norm = suffix.capitalize() if len(prefix) == 1 else suffix.lower()
                palavras.append(prefix.capitalize() + "'" + suffix_norm)
            else:
                palavras.append(p.capitalize())

        return " ".join(palavras)

    def normalizar_nome(self, nome):

        nome = self.limpar_apostrofos(nome)
        nome = self.limpar_espacos(nome)
        nome = self.normalizar_caixa(nome)

        return nome



    def assinatura(self, nome):

        nome = self.normalizar_nome(nome)

        nome_limpo = self.remover_acentos(nome).upper()

        nome_limpo = nome_limpo.replace(",", " ")

        tokens = nome_limpo.split()

        if not tokens:
            return ""

        sobrenome = tokens[-1]

        iniciais = []

        for token in tokens[:-1]:

            if token.lower() in PARTICULAS:
                continue

            token = token.replace(".", "")

            if len(token) == 1:
                iniciais.append(token)

            else:
                iniciais.append(token[0])

        return sobrenome + "|" + "|".join(iniciais)


    def pontuar_nome(self, nome):

        score = 0

        nome = self.normalizar_nome(nome)

        score += len(nome)

        score += sum(
            5
            for c in nome
            if c in "áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ"
        )

        score += nome.count(" de ") * 5

        # Each dot signals an abbreviation, making the name less complete.
        score -= nome.count(".") * 10

        return score

    def melhor_nome(self, nomes):

        return max(nomes, key=self.pontuar_nome)


    # CASO 1

    def curar_tipografia(self, lista):

        normalizados = [self.normalizar_nome(x) for x in lista]

        melhor = self.melhor_nome(normalizados)

        resultado = []

        for _ in lista:
            resultado.append(melhor)

        return resultado

    # CASO 2

    def curar_iniciais(self, lista):

        melhor = self.melhor_nome(lista)

        return [melhor] * len(lista)

    # CASO 3

    def curar_particulas(self, lista):

        normalizados = [self.normalizar_nome(x) for x in lista]

        melhor = self.melhor_nome(normalizados)

        return [melhor] * len(lista)


    # CASO 4

    def curar_agrupados(self, lista):

        melhor = self.melhor_nome(lista)

        return [melhor] * len(lista)


    # CASO 5

    def consolidar_ids(self, autores):

        grupos = {}

        for id_, nome in autores.items():

            assinatura = self.assinatura(nome)

            grupos.setdefault(assinatura, []).append(
                (int(id_), nome)
            )

        resultado = {}

        for grupo in grupos.values():

            melhor_nome = self.melhor_nome(
                [nome for _, nome in grupo]
            )

            for id_, _ in sorted(grupo):
                resultado[str(id_)] = melhor_nome

        return dict(sorted(resultado.items(), key=lambda x: int(x[0])))


    # ID OURO


    def obter_id_ouro(self, autores):

        ids = []

        for autor in autores:

            id_ = autor["id"]

            if not isinstance(id_, int):
                raise IdInvalidoError()

            if id_ <= 0:
                raise IdInvalidoError()

            ids.append(id_)

        return min(ids)

    # VALIDAÇÃO

    def processar_base_dados(self, dados):

        if not dados:
            raise FormatoInvalidoError()

        for registro in dados:

            if not isinstance(registro, dict):
                raise FormatoInvalidoError()

            if "id" not in registro:
                raise FormatoInvalidoError()

            if "nome" not in registro:
                raise FormatoInvalidoError()

            if not isinstance(registro["id"], int):
                raise FormatoInvalidoError()

            if registro["id"] <= 0:
                raise IdInvalidoError()

        return True