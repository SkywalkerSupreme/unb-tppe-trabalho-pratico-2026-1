# Relatório de Refatoração: Extrair Método (Extract Method)

## 1. Descrição da Refatoração
* **Operação:** Extrair Método (*Extract Method*)
* **Classe / Método Alvo:** `Curador::assinatura()` (`src/curador.py`)
* **Métodos Extraídos:**
  * `Curador::_tokenizar_nome()` — normalização e tokenização da entrada;
  * `Curador::_extrair_sobrenome()` — identificação do sobrenome principal;
  * `Curador::_obter_primeira_inicial()` — derivação da primeira inicial.
* **Objetivo:** Decompor o método `assinatura()`, que concentrava três responsabilidades distintas em um único corpo procedural, em passos coesos e nomeados, deixando o método principal totalmente linear e declarativo.

---

## 2. Contexto e Motivação
Originalmente, `assinatura()` acumulava três tarefas heterogêneas no mesmo escopo: (1) higienizava e quebrava o nome em tokens estruturais, removendo acentos, partículas e detectando inversão por vírgula; (2) resolvia, por meio de condicionais posicionais, qual token representava o sobrenome; e (3) varria os tokens restantes montando uma lista de iniciais apenas para consumir o primeiro elemento.

Essa concentração de responsabilidades reduzia a coesão do método e obrigava a manter em mente três níveis de detalhe simultâneos (manipulação de strings, indexação de listas e regras de expansão de iniciais). A extração isola cada preocupação em uma função privada com nome autoexplicativo, de modo que `assinatura()` passe a expressar apenas o **quê** (a orquestração), delegando o **como** aos métodos auxiliares.

---

## 3. Alterações Estruturais Realizadas

### 3.1. Método extraído `_tokenizar_nome()`
O bloco de normalização e quebra em tokens foi movido para um método que devolve a dupla `(tokens, invertido_por_virgula)`:

```python
def _tokenizar_nome(self, nome):
    nome = self.normalizar_nome(nome)
    nome_limpo = self.remover_acentos(nome).upper()
    invertido_por_virgula = "," in nome_limpo
    nome_limpo = nome_limpo.replace(",", " ")

    tokens = [t for t in nome_limpo.split() if t.lower() not in PARTICULAS]
    return tokens, invertido_por_virgula
```

### 3.2. Método extraído `_extrair_sobrenome()`
O bloco de condicionais posicionais que decide o sobrenome permaneceu isolado, agora com docstring esclarecendo o contrato de retorno:

```python
def _extrair_sobrenome(self, tokens, invertido_por_virgula):
    if invertido_por_virgula:
        return tokens[0], tokens[1:]

    if self._eh_inicial(tokens[-1]) and not self._eh_inicial(tokens[0]):
        return tokens[0], tokens[1:]

    return tokens[-1], tokens[:-1]
```

### 3.3. Método extraído `_obter_primeira_inicial()`
A varredura que construía a lista completa de iniciais para consumir apenas o primeiro elemento foi substituída por um método que retorna diretamente a primeira inicial encontrada, eliminando a variável temporária `iniciais`:

```python
def _obter_primeira_inicial(self, tokens):
    for token in tokens:
        if self._eh_inicial(token):
            expandidas = self._expandir_iniciais(token)
            if expandidas:
                return expandidas[0]
        elif token:
            return token[0]
    return ""
```

### 3.4. Método `assinatura()` resultante
Após as extrações, o corpo tornou-se uma composição direta e sem ruído:

```python
def assinatura(self, nome):
    tokens, invertido_por_virgula = self._tokenizar_nome(nome)
    if not tokens:
        return ""

    sobrenome, restantes = self._extrair_sobrenome(tokens, invertido_por_virgula)
    primeira_inicial = self._obter_primeira_inicial(restantes)
    return f"{sobrenome}|{primeira_inicial}"
```

---

## 4. Benefícios Arquiteturais Observados
* **Legibilidade:** o corpo de `assinatura()` passou de um bloco procedural com laços e condicionais para uma sequência de três chamadas nomeadas, lendo-se quase como pseudocódigo.
* **Coesão:** cada método extraído possui uma única razão para mudar — mudanças na tokenização, na heurística de sobrenome ou na coleta de iniciais ficam confinadas ao respectivo método.
* **Testabilidade:** as três sub-rotinas passaram a ser testáveis isoladamente, sem depender do formato final da assinatura (ver seção 5).
* **Eliminação de variável temporária:** a lista intermediária `iniciais`, cujo único uso era fornecer `iniciais[0]`, deixou de existir.

---

## 5. Verificação de Corretude
A operação foi realizada de forma manual, sem suporte ferramental de refatoração automática. A equivalência comportamental foi garantida em duas frentes:

1. **Suíte pré-existente intacta:** os 196 testes originais dos Casos 1 a 5 continuam passando sem qualquer alteração, comprovando que a assinatura gerada não mudou.
2. **Novos testes dedicados** (`tests/test_caso6_extrair_metodo.py`): 30 novos casos exercitam cada método extraído em isolamento (`_tokenizar_nome`, `_extrair_sobrenome`, `_obter_primeira_inicial`) e verificam a composição em `assinatura()`, incluindo colisão de assinaturas entre variações do mesmo autor.

Resultado da execução via Pytest:

```
237 passed
```