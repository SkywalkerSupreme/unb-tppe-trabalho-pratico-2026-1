# [Refact] Extrair Classe: Curador 


import unicodedata

PARTICULAS = {"de", "da", "do", "das", "dos"}

class ProcessadorTextoCientifico:
    """
    CLASSE EXTRAÍDA (Refatoração: Extrair Classe)
    Responsável exclusiva pelas operações de manipulação textual,
    higienização de caracteres e análise de tokens estruturais.
    """

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

    def eh_inicial(self, token):
        miolo = token.replace(".", "")
        if not miolo:
            return False
        if len(miolo) == 1:
            return True
        return miolo.isupper() and len(miolo) <= 3

    def expandir_iniciais(self, token):
        return list(token.replace(".", ""))