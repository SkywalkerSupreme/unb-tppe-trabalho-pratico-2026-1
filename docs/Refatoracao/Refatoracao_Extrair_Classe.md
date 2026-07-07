# Relatório de Refatoração: Extração de Classe (Extract Class)

## 1. Descrição da Refatoração
* **Operação:** Extração de Classe (*Extract Class*)
* **Classe Alvo:** `Curador` (`src/curador.py`)
* **Classes Extraídas:**
    * `ProcessadorTextoCientifico` (`src/processador.py`)
    * `ValidadorRegistros` (`src/validador.py`)
* **Objetivo:** Separar as responsabilidades de manipulação e higienização textual de baixo nível, bem como a validação de contrato dos registros de entrada, que antes sobrecarregavam a classe principal de regras de negócio.

---

## 2. Contexto e Motivação
No design anterior, a classe `Curador` acumulava tarefas demais e violava o **Princípio de Responsabilidade Única (SRP)**. Além de coordenar os cinco casos de deduplicação, gerenciar as assinaturas fonéticas e consolidar os IDs, o componente também resolvia todo o trabalho pesado de tratamento de strings e a validação de contrato dos dados de entrada. Essa carga incluía:
* Remoção de acentuação gráfica.
* Normalização e substituição de variantes de apóstrofos.
* Limpeza de espaços em branco e padronização de caixas (*case*).
* Análise estrutural e desmembramento de iniciais.
* Verificação de dataset vazio, campos obrigatórios, tipagem e regra de IDs positivos.

Essa sobrecarga transformou a classe `Curador` em uma *Large Class* (Classe Grande ou "Classe Deus"). O resultado foi a perda de coesão do código, o que prejudicou a legibilidade e dificultou a manutenção na inteligência de deduplicação.

---

## 3. Alterações Estruturais Realizadas

A refatoração isolou os mecanismos puros de infraestrutura em arquivos físicos independentes. Essa escolha manteve o ecossistema modular.

### Engenharia do Novo Componente (`src/processador.py`)
A nova classe `ProcessadorTextoCientifico` absorveu as rotinas técnicas de infraestrutura textual:
* `remover_acentos(texto)`
* `limpar_apostrofos(texto)`
* `limpar_espacos(texto)`
* `normalizar_caixa(texto)`
* `normalizar_nome(nome)`
* `eh_inicial(token)`
* `expandir_iniciais(token)`

### Engenharia do Novo Componente (`src/validador.py`)
A nova classe `ValidadorRegistros` absorveu as rotinas técnicas de validação de contrato:
* `processar_base_dados(dados)`
* `obter_id_ouro(autores)`

As exceções de domínio `FormatoInvalidoError` e `IdInvalidoError` foram movidas para junto do componente que as lança e são reexportadas por `Curador`, preservando a identidade de classe e o contrato público consumido por `main.py`.

### Adaptação da Classe Original (`src/curador.py`)
A classe `Curador` adotou o padrão de projeto de **Delegação via Composição**. Ela instancia os novos componentes e redireciona as chamadas internas. Desse modo, a infraestrutura de strings e a validação de registros ficam ocultas para o cliente externo:

```python
class Curador:
    def __init__(self):
        # Injeção de dependência das classes extraídas por composição
        self._processador_texto = ProcessadorTextoCientifico()
        self._validador = ValidadorRegistros()

    def normalizar_nome(self, nome):
        # Delegação de comportamento
        return self._processador_texto.normalizar_nome(nome)

    def processar_base_dados(self, dados):
        # Delegação de comportamento
        return self._validador.processar_base_dados(dados)

```

As funções core de inteligência de deduplicação (assinatura e pontuar_nome) e os fluxos dos Casos de 1 a 5 permaneceram sob o escopo do Curador, mas agora operam de forma muito mais limpa e coesa.

## 4. Benefícios Arquiteturais Observados

    1. **Alta Coesão**: Cada classe possui agora apenas uma razão para mudar. Modificações na forma como a linguagem trata caracteres (como suporte a novas aspas ou acentos) impactam apenas ProcessadorTextoCientifico; mudanças na forma como os registros são validados (novos campos obrigatórios ou novas regras de ID) impactam apenas ValidadorRegistros; enquanto mudanças nos critérios de deduplicação impactam apenas Curador.
 
    2. **Baixo Acoplamento**: A separação física em arquivos (curador.py, processador.py e validador.py) isola o código de produção, facilitando o trabalho paralelo na equipe.

    3. **Preservação do Contrato Público**: A interface de métodos da classe Curador foi integralmente mantida. Isso garantiu compatibilidade com as chamadas externas (como no script main.py) e evitou qualquer necessidade de alteração na suite de testes do projeto.

## 5. Verificação de Corretude e Impacto

Para validar o critério de que os testes deveriam continuar efetivos e passando sem efeitos colaterais, a suíte automatizada via Pytest foi executada imediatamente após as modificações estruturais da arquitetura:

<a href="https://ibb.co/yB7GhLB9"><img src="https://i.ibb.co/mFg1vQFj/image.png" alt="image" border="0"></a>