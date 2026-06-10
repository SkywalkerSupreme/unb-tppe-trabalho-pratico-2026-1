# Relatório do Processo de TDD - Fase RED e GREEN (Etapa 1)

Este documento registra a conclusão da primeira fase do ciclo **Red-Green-Refactor** do Desenvolvimento Guiado por Testes (TDD) para o projeto de Curadoria de Dados Científicos.

## Metodologia Aplicada
Conforme as boas práticas de TDD, nenhuma linha de lógica de negócio ou algoritmo de limpeza de strings foi implementado no arquivo `curador.py` antes que a suíte de testes estivesse completamente escrita e estruturada. 

Foram mapeadas as regras de negócio para os 5 casos de deduplicação solicitados pelo enunciado, além de uma suíte exclusiva para o tratamento de exceções estruturais.

## Cobertura e Análise da Fase Red
A suíte atual conta com **144 execuções de testes automatizados**, o que gerou um total de **184 verificações (*assertions*)**. O resultado obtido foi de **174 falhas** e **10 acertos**, o que reflete exatamente o estado esperado nesta etapa do desenvolvimento:

* **174 Falhas Controladas (Casos 1 a 5):** Validam que as regras de negócio ainda não foram codificadas. Como as funções do curador foram criadas retornando estruturas vazias (`[]` ou `{}`), os testes falham ao tentar comparar esses retornos com os dados reais esperados da curadoria. Isso garante a ausência de lógicas fixas (*hardcoded*) para mascarar o resultado.
* **10 Acertos Precoces (Suíte de Exceções):** Os 10 testes contidos em `test_excecoes.py` passaram com sucesso (barra verde). Isso ocorreu porque, para que o ambiente do Pytest fosse coletado sem erros de importação, foi implementada uma validação estrutural mínima de integridade no método `processar_base_dados`. Esse esqueleto analisa se o JSON possui o formato correto, disparando `FormatoInvalidoError` e `IdInvalidoError` conforme os testes de carga de dados exigem, validando o comportamento de segurança do contrato antes mesmo do processamento dos nomes.

###  Evidência do Terminal (Fase RED Coletada)
Abaixo está o registro da execução do comando `python3 -m pytest` demonstrando o comportamento controlado do ecossistema de testes do grupo:

<img width="1179" height="113" alt="Screenshot from 2026-06-08 16-07-49" src="https://github.com/user-attachments/assets/b4c57b69-9aca-436a-b02e-c6f2367b9f16" />


## Organização da Suíte de Testes

A suíte de testes foi estruturada de forma modular, com a separação dos cenários de validação em arquivos independentes, o que permite a execução conjunta ou isolada de cada caso de deduplicação.

A organização adotada segue diretamente os requisitos definidos no enunciado do trabalho e garante a rastreabilidade entre cada regra de negócio e sua respectiva unidade de teste.

| Suíte | Objetivo | Arquivo |
|---------|---------|---------|
| Caso 1 | Validar diferenças tipográficas e normalização textual | [test_caso1_tipografia.py](../src/tests/test_caso1_tipografia.py) |
| Caso 2 | Validar nomes compostos por sobrenome e iniciais | [test_caso2_iniciais.py](../src/tests/test_caso2_iniciais.py) |
| Caso 3 | Validar partículas de ligação e pontuação opcional | [test_caso3_particulas.py](../src/tests/test_caso3_particulas.py) |
| Caso 4 | Validar iniciais agrupadas associadas ao sobrenome | [test_caso4_agrupados.py](../src/tests/test_caso4_agrupados.py) |
| Caso 5 | Validar deduplicação e consolidação de identificadores | [test_caso5_deduplicacao.py](../src/tests/test_caso5_deduplicacao.py) |
| Exceções | Validar integridade estrutural e tratamento de erros | [test_excecoes.py](../src/tests/test_excecoes.py) |

A execução integrada da suíte é realizada por meio do framework Pytest e utiliza testes parametrizados, marcadores (*markers*), fixtures e verificações de exceção.

- **Observação:** Todos os testes podem ser executados de forma independente ou em conjunto, sem dependência de ordem de execução e sem compartilhamento de estado entre cenários.


## Fase GREEN: Implementação da Lógica de Negócio

Concluída a Fase RED, deu-se início à Fase GREEN, cujo objetivo é escrever o código mínimo necessário para que cada teste anteriormente vermelho passe a apresentar barra verde, sem alterar a suíte de testes já definida.

As funções do `curador.py` que antes retornavam estruturas vazias (`[]` ou `{}`) foram implementadas com a lógica real de curadoria, organizada em métodos auxiliares reutilizáveis (`normalizar_nome`, `assinatura`, `pontuar_nome` e `melhor_nome`), de modo a evitar duplicação e atender simultaneamente aos cinco casos de deduplicação:

* **Caso 1 (Tipografia):** normalização de apóstrofos, acentuação, caixa e espaços excedentes, elegendo a grafia mais completa do grupo.
* **Caso 2 (Sobrenome + Iniciais):** unificação das versões abreviadas com a versão por extenso do nome.
* **Caso 3 (Partículas):** reintegração das partículas de ligação (*de*, *da*, *do*) e tratamento dos pontos opcionais nas abreviações.
* **Caso 4 (Iniciais agrupadas):** desmembramento de blocos de iniciais colados ao sobrenome (ex.: `SH Guaraldi`).
* **Caso 5 (Deduplicação de IDs):** agrupamento dos registros de um mesmo autor por assinatura e mapeamento de todos para o menor ID.

### Cobertura e Análise da Fase GREEN

Após a implementação, a suíte completa foi executada novamente sem qualquer alteração nos testes. O resultado obtido foi de **184 verificações (*assertions*) bem-sucedidas e 0 falhas** (barra verde total), confirmando que todas as unidades passaram a estar implementadas conforme o critério de correção do enunciado.

Reforça-se que nenhuma unidade foi resolvida por meio de valores fixos (*hardcoded*): cada caso é tratado por algoritmos genéricos de normalização e pontuação de nomes, de forma que os mesmos métodos atendem tanto aos dados da tabela do enunciado quanto às variações complementares incluídas nos testes parametrizados.

## Evidência do Terminal (Fase GREEN Coletada)

Abaixo está o registro da execução do comando `python3 -m pytest` demonstrando a suíte completa em estado verde:

<img src="https://i.ibb.co/1fBv85NL/image.png" />
