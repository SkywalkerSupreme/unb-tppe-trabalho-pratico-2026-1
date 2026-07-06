# Relatório de Refatoração: Extração de Classe (Extract Class)

## 1. Descrição da Refatoração
* **Operação:** Extração de Classe (*Extract Class*)
* **Classe Alvo:** `Curador` (`src/curador.py`)
* **Classe Extraída:** `ProcessadorTextoCientifico` (`src/processador.py`)
* **Objetivo:** Separar as responsabilidades de manipulação e higienização textual de baixo nível, que antes sobrecarregavam a classe principal de regras de negócio.

---

## 2. Contexto e Motivação
No design anterior, a classe `Curador` acumulava tarefas demais e violava o **Princípio de Responsabilidade Única (SRP)**. Além de coordenar os cinco casos de deduplicação, gerenciar as assinaturas fonéticas e consolidar os IDs, o componente também resolvia todo o trabalho pesado de tratamento de strings. Essa carga incluía:
* Remoção de acentuação gráfica.
* Normalização e substituição de variantes de apóstrofos.
* Limpeza de espaços em branco e padronização de caixas (*case*).
* Análise estrutural e desmembramento de iniciais.

Essa sobrecarga transformou a classe `Curador` em uma *Large Class* (Classe Grande ou "Classe Deus"). O resultado foi a perda de coesão do código, o que prejudicou a legibilidade e dificultou a manutenção na inteligência de deduplicação.

---

## 3. Alterações Estruturais Realizadas

A refatoração isolou os mecanismos puros de tratamento de strings em um arquivo físico independente. Essa escolha manteve o ecossistema modular.

### Engenharia do Novo Componente (`src/processador.py`)
A nova classe `ProcessadorTextoCientifico` absorveu as rotinas técnicas de infraestrutura textual:
* `remover_acentos(texto)`
* `limpar_apostrofos(texto)`
* `limpar_espacos(texto)`
* `normalizar_caixa(texto)`
* `normalizar_nome(nome)`
* `eh_inicial(token)`
* `expandir_iniciais(token)`

### Adaptação da Classe Original (`src/curador.py`)
A classe `Curador` adotou o padrão de projeto de **Delegação via Composição**. Ela instancia o novo componente e redireciona as chamadas internas. Desse modo, a infraestrutura de strings fica oculta para o cliente externo:

```python
class Curador:
    def __init__(self):
        # Injeção de dependência da classe extraída por composição
        self._processador_texto = ProcessadorTextoCientifico()

    def normalizar_nome(self, nome):
        # Delegação pura de comportamento
        return self._processador_texto.normalizar_nome(nome)

```

As funções core de inteligência de deduplicação (assinatura e pontuar_nome) e os fluxos dos Casos de 1 a 5 permaneceram sob o escopo do Curador, mas agora operam de forma muito mais limpa e coesa.

## 4. Benefícios Arquiteturais Observados

    1. **Alta Coesão**: Cada classe possui agora apenas uma razão para mudar. Modificações na forma como a linguagem trata caracteres (como suporte a novas aspas ou acentos) impactam apenas ProcessadorTextoCientifico, enquanto mudanças nos critérios de deduplicação impactam apenas Curador.
 
    2. **Baixo Acoplamento**: A separação física em arquivos (curador.py e processador.py) isola o código de produção, facilitando o trabalho paralelo na equipe.

    3. **Preservação do Contrato Público**: A interface de métodos da classe Curador foi integralmente mantida. Isso garantiu compatibilidade com as chamadas externas (como no script main.py) e evitou qualquer necessidade de alteração na suite de testes do projeto.

## 5. Verificação de Corretude e Impacto

Para validar o critério de que os testes deveriam continuar efetivos e passando sem efeitos colaterais, a suíte automatizada via Pytest foi executada imediatamente após as modificações estruturais da arquitetura:

<img width="1208" height="272" alt="image" src="https://github.com/user-attachments/assets/8739f7ed-8c03-45e0-92ef-0e967b9de2e8" />


