# src/curador.py
import re
from src.processador import ProcessadorTextoCientifico, PARTICULAS

class FormatoInvalidoError(Exception):
    pass

class IdInvalidoError(Exception):
    pass


class PontuadorNome:
    """Objeto-Método para o cálculo do score de qualidade de um nome."""
    
    def __init__(self, nome_normalizado):
        self.nome = nome_normalizado
        self.score = 0

    def computar(self):
        if not self.nome:
            return 0

        self.score += len(self.nome)
        self.score += sum(5 for c in self.nome if c in "áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ")
        
        self.score += self.nome.count(" de ") * 5
        self.score += self.nome.count(" da ") * 5
        self.score += self.nome.count(" do ") * 5
        self.score += self.nome.count(" das ") * 5
        self.score += self.nome.count(" dos ") * 5

        self.score -= self.nome.count(".") * 10
        return self.score


class Curador:
    """Classe principal de curadoria e deduplicação de autores."""

    def __init__(self):
        self._processador_texto = ProcessadorTextoCientifico()

    def remover_acentos(self, texto):
        return self._processador_texto.remover_acentos(texto)

    def limpar_apostrofos(self, texto):
        return self._processador_texto.limpar_apostrofos(texto)

    def limpar_espacos(self, texto):
        return self._processador_texto.limpar_espacos(texto)

    def normalizar_caixa(self, texto):
        return self._processador_texto.normalizar_caixa(texto)

    def normalizar_nome(self, nome):
        return self._processador_texto.normalizar_nome(nome)

    def _eh_inicial(self, token):
        return self._processador_texto.eh_inicial(token)

    def _expandir_iniciais(self, token):
        return self._processador_texto.expandir_iniciais(token)

    def _extrair_sobrenome(self, tokens, invertido_por_virgula):
        """Método Extraído: Isola o sobrenome principal conforme a estrutura dos tokens."""
        if invertido_por_virgula:
            return tokens[0], tokens[1:]
        
        if self._eh_inicial(tokens[-1]) and not self._eh_inicial(tokens[0]):
            return tokens[0], tokens[1:]
            
        return tokens[-1], tokens[:-1]

    def signature(self, nome):
        return self.assinatura(nome)

    def assinatura(self, nome):
        nome = self.normalizar_nome(nome)
        nome_limpo = self.remover_acentos(nome).upper()
        invertido_por_virgula = "," in nome_limpo
        nome_limpo = nome_limpo.replace(",", " ")

        tokens = [t for t in nome_limpo.split() if t.lower() not in PARTICULAS]
        if not tokens:
            return ""

        sobrenome, restantes = self._extrair_sobrenome(tokens, invertido_por_virgula)
        
        iniciais = []
        for token in restantes:
            if self._eh_inicial(token):
                iniciais.extend(self._expandir_iniciais(token))
            else:
                iniciais.append(token[0])

        primeira_inicial = iniciais[0] if iniciais else ""
        return f"{sobrenome}|{primeira_inicial}"

    def pontuar_nome(self, nome):
        """Substituir Método por Objeto-Método: Transfere execução para PontuadorNome."""
        nome_normalizado = self.normalizar_nome(nome)
        objeto_metodo = PontuadorNome(nome_normalizado)
        return objeto_metodo.computar()

    def melhor_nome(self, nomes):
        if not nomes:
            return ""
        
        candidatos = []
        for n in nomes:
            if n is not None and str(n).strip() != "":
                candidatos.append(n)
                
        if not candidatos:
            return ""
            
        return max(candidatos, key=self.pontuar_nome)

    def curar_tipografia(self, lista):
        if lista is None:
            return []
            
        valores_validos = []
        for item in lista:
            if item is not None:
                valores_validos.append(item)
                
        if not valores_validos:
            return []
            
        normalizados = []
        for x in valores_validos:
            nome_tratado = self.normalizar_nome(x)
            normalizados.append(nome_tratado)
            
        melhor = self.melhor_nome(normalizados)
        
        resultado = []
        for _ in lista:
            resultado.append(melhor)
            
        return resultado

    def curar_iniciais(self, lista):
        if lista is None:
            return []
            
        valores_validos = []
        for item in lista:
            if item is not None:
                valores_validos.append(item)
                
        if not valores_validos:
            return []
            
        melhor = self.melhor_nome(valores_validos)
        
        resultado = []
        for _ in lista:
            resultado.append(melhor)
            
        return resultado

    def curar_particulas(self, lista):
        if lista is None:
            return []
            
        valores_validos = []
        for item in lista:
            if item is not None:
                valores_validos.append(item)
                
        if not valores_validos:
            return []
            
        normalizados = []
        for x in valores_validos:
            nome_tratado = self.normalizar_nome(x)
            normalizados.append(nome_tratado)
            
        melhor = self.melhor_nome(normalizados)
        
        resultado = []
        for _ in lista:
            resultado.append(melhor)
            
        return resultado

    def curar_agrupados(self, lista):
        if lista is None:
            return []
            
        valores_validos = []
        for item in lista:
            if item is not None:
                valores_validos.append(item)
                
        if not valores_validos:
            return []
            
        melhor = self.melhor_nome(valores_validos)
        
        resultado = []
        for _ in lista:
            resultado.append(melhor)
            
        return resultado

    def consolidar_ids(self, autores):
        if autores is None:
            return {}
            
        if len(autores) == 0:
            return {}
            
        grupos = {}
        for id_bruto, nome_bruto in autores.items():
            if id_bruto is not None and nome_bruto is not None:
                chave_assinatura = self.assinatura(nome_bruto)
                id_inteiro = int(id_bruto)
                grupos.setdefault(chave_assinatura, []).append((id_inteiro, nome_bruto))

        resultado = {}
        for chave_grupo in grupos:
            colecao_grupo = grupos[chave_grupo]
            lista_nomes = []
            for par_autor in colecao_grupo:
                lista_nomes.append(par_autor[1])
                
            melhor_nome = self.melhor_nome(lista_nomes)
            
            for par_autor in sorted(colecao_grupo):
                id_atual = par_autor[0]
                resultado[str(id_atual)] = melhor_nome
                
        lista_pares_ordenados = sorted(resultado.items(), key=lambda elemento: int(elemento[0]))
        return dict(lista_pares_ordenados)

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
