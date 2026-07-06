# Relatório de Refatoração: Substituir Método por Objeto-Método (Replace Method with Method Object)

## 1. Descrição da Refatoração
* **Operação:** Substituir Método por Objeto-Método (*Replace Method with Method Object*)
* **Classe / Método Alvo:** `Curador::pontuar_nome()` (`src/curador.py`)
* **Classe Objeto-Método Criada:** `PontuadorNome` (`src/curador.py`)
* **Objetivo:** Isolar a rotina de avaliação de completude e cálculo de score de nomes científicos em um componente dedicado com ciclo de vida e estado próprios.

---

## 2. Contexto e Motivação
O método `pontuar_nome()` realizava uma série de computações incrementais acumulando valores em uma variável de controle local (`score`). Embora o método não fosse longo, ele misturava regras de avaliação de strings com o fluxo principal de deduplicação da classe `Curador`. 

A transformação desse método em um objeto separado permite isolar as regras de pontuação (pesos por acentos, penalidades por pontos e bônus por partículas), liberando a classe principal dessa subtarefa matemática específica e facilitando futuras manutenções no algoritmo de ranqueamento.

---

## 3. Alterações Estruturais Realizadas

A refatoração seguiu os passos formais definidos por Martin Fowler:

1. **Criação da Classe Especializada:** Foi desenvolvida a classe `PontuadorNome` contendo um construtor que recebe a referência da instância chamadora (`Curador`) e o argumento original (`nome`).
2. **Transferência de Estado:** A variável local antiga `score` foi convertida em um atributo de instância da nova classe.
3. **Delegação de Fluxo:** O corpo original do método foi movido para a função `computar()`. O método `Curador.pontuar_nome()` original passou a atuar como uma mera casca de delegação:

```python
def pontuar_nome(self, nome):
    objeto_metodo = PontuadorNome(self, nome)
    return objeto_metodo.computar()
```

4. Benefícios Arquiteturais Observados

    - Isolamento de Estado: O cálculo de score ganhou um ciclo de vida próprio e isolado, evitando o acúmulo de variáveis temporárias na classe principal.

    - Facilidade de Expansão: Caso a equipe decida alterar os pesos ou introduzir novas regras de validação (como checagem de sufixos ou títulos acadêmicos), a alteração ficará restrita à classe PontuadorNome, sem poluir o fluxo de deduplicação dos casos de uso.

5. Verificação de Corretude

A integridade do comportamento do sistema foi avaliada por meio da execução da suíte de testes automatizados via Pytest:

<img width="1208" height="272" alt="image" src="https://github.com/user-attachments/assets/8e965f8c-38ce-4b06-b953-4211efee318d" />
