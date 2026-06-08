# Relatório do Processo de TDD - Fase RED (Etapa 1)

Este documento registra a conclusão da primeira fase do ciclo **Red-Green-Refactor** do Desenvolvimento Guiado por Testes (TDD) para o projeto de Curadoria de Dados Científicos.

## 1. Metodologia Aplicada
Conforme as boas práticas de TDD, nenhuma linha de lógica de negócio ou algoritmo de limpeza de strings foi implementado no arquivo `curador.py` antes que a suíte de testes estivesse completamente escrita e estruturada. 

Foram mapeadas as regras de negócio para os 5 casos de deduplicação solicitados pelo enunciado, além de uma suíte exclusiva para o tratamento de exceções estruturais.

## 2. Cobertura e Análise da Fase Red
A suíte atual conta com **144 execuções de testes automatizados**, o que gerou um total de **184 verificações (*assertions*)**. O resultado obtido foi de **174 falhas** e **10 acertos**, o que reflete exatamente o estado esperado nesta etapa do desenvolvimento:

* **174 Falhas Controladas (Casos 1 a 5):** Validam que as regras de negócio ainda não foram codificadas. Como as funções do curador foram criadas retornando estruturas vazias (`[]` ou `{}`), os testes falham ao tentar comparar esses retornos com os dados reais esperados da curadoria. Isso garante a ausência de lógicas fixas (*hardcoded*) para mascarar o resultado.
* **10 Acertos Precoces (Suíte de Exceções):** Os 10 testes contidos em `test_excecoes.py` passaram com sucesso (barra verde). Isso ocorreu porque, para que o ambiente do Pytest fosse coletado sem erros de importação, foi implementada uma validação estrutural mínima de integridade no método `processar_base_dados`. Esse esqueleto analisa se o JSON possui o formato correto, disparando `FormatoInvalidoError` e `IdInvalidoError` conforme os testes de carga de dados exigem, validando o comportamento de segurança do contrato antes mesmo do processamento dos nomes.

## 3. Evidência do Terminal (Fase RED Coletada)
Abaixo está o registro da execução do comando `python3 -m pytest` demonstrando o comportamento controlado do ecossistema de testes do grupo:

<img width="1179" height="113" alt="Screenshot from 2026-06-08 16-07-49" src="https://github.com/user-attachments/assets/b4c57b69-9aca-436a-b02e-c6f2367b9f16" />
