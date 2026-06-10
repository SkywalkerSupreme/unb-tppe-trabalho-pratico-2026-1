# Trabalho Prático - TPPE (UnB - FCTE)

## Integrantes

| Foto | Nome | Matrícula |
| :---: | :---: | :---: |
| <a href="https://github.com/kalipassos"><img src="https://github.com/kalipassos.png" width="100px;" alt="Foto kalipassos"/><br /><sub><b>@kalipassos</b></sub></a> | Kallyne Macedo Passos | 202046229 |
| <a href="https://github.com/SkywalkerSupreme"><img src="https://github.com/SkywalkerSupreme.png" width="100px;" alt="Foto SkywalkerSupreme"/><br /><sub><b>@SkywalkerSupreme</b></sub></a> | Larissa Stéfane Barboza Santos | 211039573 |
| <a href="https://github.com/west7"><img src="https://github.com/west7.png" width="100px;" alt="Foto west7"/><br /><sub><b>@west7</b></sub></a> | Guilherme Westphall | 211061805 |


## Sobre o Trabalho

Este projeto consiste no desenvolvimento de um sistema de **Curadoria e Deduplicação de Dados Científicos** para repositórios de instituições de pesquisa. O objetivo principal é integrar diferentes fontes de dados (como o Currículo Lattes, ACM, ScienceDirect, etc.), identificar registros duplicados de autores numa mesma publicação e unificá-los para um **padrão-ouro**.

O desenvolvimento do projeto está estruturado com base na metodologia **TDD (Test-Driven Development)**, dividindo-se nas duas etapas principais da disciplina de Técnicas de Programação para Plataformas Emergentes (TPPE):
1. **Etapa 1 (TDD):** Implementação das unidades de código totalmente guiada por testes unitários automatizados (Fase RED/GREEN). 
2. **Etapa 2 (Refactoring):** Aplicação de operações de refatoração para melhoria contínua da arquitetura e qualidade do código.

### Casos de Deduplicação Contemplados:
* **Caso 1 (Diferenças Tipográficas):** Padronização de acentuação, cedilhas e uso correto de caracteres (como o apóstrofo).
* **Caso 2 (Sobrenome + Iniciais):** Identificação de equivalência entre versões abreviadas e extensas de nomes, unificando para a versão completa.
* **Caso 3 (Partículas e Pontuação Opcional):** Tratamento de omissões de partículas (como "de") e pontos após abreviações.
* **Caso 4 (Iniciais Agrupadas + Sobrenome):** Preferência pela versão por extenso em vez de iniciais agrupadas (ex: "SH Guaraldi" para "Sérgio Henrique Guaraldi").
* **Caso 5 (IDs Diferentes para o Mesmo Autor):** Mapeamento de múltiplos registros da mesma pessoa para o ID de menor valor.

---

## Objetivo

Desenvolver um sistema de curadoria e deduplicação de dados científicos capaz de identificar registros equivalentes de autores, normalizar inconsistências textuais e consolidar informações em um padrão-ouro, utilizando a metodologia Test-Driven Development (TDD).

---


## Tecnologias Utilizadas

| Item | Tecnologia |
|--------|--------|
| Linguagem Orientada a Objetos | Python 3.12.3 |
| Framework de Testes | Pytest |
| Versão do Framework | 7.4.4  |
| Paradigma de Desenvolvimento | Test-Driven Development (TDD) |


---

## Documentação Adicional do Projeto

Para uma avaliação detalhada dos artefatos de engenharia criados pelo grupo, consulte nossa pasta de documentações dedicada:

| Documento | Descrição |
|------------|------------|
| **[Simulação da Base de Dados (800 registros)](./docs/base_dados.md)** | Explicação da modelagem do arquivo JSON e links de rastreabilidade. |
| **[Relatório do Ciclo TDD - Fases RED e GREEN](./docs/processo_tdd.md)** | Detalhamento técnico da cobertura dos 184 testes automatizados e evidências de execução do terminal. |

---

## Métricas do Projeto

| Métrica | Valor |
|----------|--------|
| Registros simulados | 800 |
| Arquivos de teste | 6 |
| Casos de deduplicação | 5 |
| Suíte de exceções | 1 |
| Testes aprovados | 184 |

---

## Resultados Obtidos

- 184 testes automatizados aprovados;
- 5 casos de deduplicação implementados;
- Validação estrutural da base de dados implementada;
- Tratamento de exceções implementado;
- Base de simulação contendo 800 registros;
- Aplicação do ciclo RED → GREEN do TDD e preparação da etapa de refatoração.

---

##  Como Executar os Testes

Para rodar e validar a suíte completa de testes automatizados (contendo testes parametrizados, suítes dedicadas, categorias/marcadores e testes de exceção), siga as instruções abaixo:

### 1. Pré-requisitos
Certifique-se de ter o Python 3.12+ e o gerenciador de pacotes `pip` instalados na sua máquina local.

### 2. Instalação do Framework
Instale o framework de testes `pytest` executando o comando no terminal:
```bash
pip install pytest==7.4.4
```

### 3. Execução Completa dos Testes
Na raiz do projeto (onde se encontra o arquivo `pytest.ini`), execute o comando para rodar todas as suítes em conjunto:
```bash
python3 -m pytest
```

### 4. Execução por Categorias (Marcadores do enunciado)
Caso queira testar categorias ou casos isolados utilizando os marcadores registrados no pytest.ini, utilize a flag -m:

```bash
# Executar apenas o Caso 1 (Tipografia)
python3 -m pytest -m caso1

# Executar apenas a suíte de Testes de Exceção
python3 -m pytest -m excecoes

```

## Evidência de Execução

Execução da suíte completa de testes:


<img width="1203" height="244" alt="image" src="https://github.com/user-attachments/assets/1388dba6-8b80-4756-8fba-60c76ae2ffa7" />

