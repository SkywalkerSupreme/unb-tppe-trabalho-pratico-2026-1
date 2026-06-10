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
| **[Arquitetura](./docs/arquitetura.md)** | Descrição da organização do sistema, responsabilidades dos componentes, fluxo de processamento e estratégia de deduplicação adotada. |

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


## Base de Dados de Simulação

O projeto utiliza uma base de dados sintética composta por **800 registros científicos**, desenvolvida para reproduzir cenários de duplicidade de autores, divergências de grafia, abreviações, omissão de partículas e redundância de identificadores.

O conjunto de dados serve como insumo para a validação das unidades de curadoria e para a execução da suíte de testes automatizados.

| Recurso | Descrição |
|----------|------------|
| **[dados_curadoria_800.json](./src/tests/data/dados_curadoria_800.json)** | Base de dados utilizada nos testes e experimentos de deduplicação. |
| **[Documentação da Base de Dados](./docs/base_dados.md)** | Descrição da estrutura dos registros e dos cenários simulados. |

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

#### Caso 1 — Diferenças Tipográficas

```bash
python3 -m pytest -m caso1
```

#### Caso 2 — Sobrenome + Iniciais

```bash
python3 -m pytest -m caso2
```

#### Caso 3 — Partículas Opcionais

```bash
python3 -m pytest -m caso3
```

#### Caso 4 — Iniciais Agrupadas

```bash
python3 -m pytest -m caso4
```

#### Caso 5 — Deduplicação de IDs

```bash
python3 -m pytest -m caso5
```

#### Testes de Exceção

```bash
python3 -m pytest -m excecoes
```

#### Categorias Específicas

```bash
# Testes tipográficos
python3 -m pytest -m tipografia

# Testes de iniciais
python3 -m pytest -m iniciais

# Testes de partículas
python3 -m pytest -m particulas

# Testes de iniciais agrupadas
python3 -m pytest -m agrupados

# Testes de deduplicação
python3 -m pytest -m deduplicacao

# Testes de tratamento de erros
python3 -m pytest -m erros
```

## Evidência de Execução

Execução da suíte completa de testes:


<img width="1203" height="244" alt="image" src="https://github.com/user-attachments/assets/1388dba6-8b80-4756-8fba-60c76ae2ffa7" />

## Execução dos testes por seção

As imagens a seguir apresentam a execução individual dos testes associados a cada caso. Essa evidência complementa a execução da suíte completa e permite verificar separadamente o comportamento e a aprovação de cada unidade implementada.

### Caso 1 – Diferenças Tipográficas

Execução da suíte referente ao tratamento de diferenças tipográficas, acentuação, caracteres especiais e normalização textual.

<img width="1203" height="244" alt="Screenshot from 2026-06-10 10-25-27" src="https://github.com/user-attachments/assets/31272b61-3864-467d-97a4-660380ffa680" />


---

### Caso 2 – Sobrenome Acompanhado de Iniciais

Execução da suíte referente à identificação e unificação de autores representados por sobrenome acompanhado de iniciais.


<img width="1203" height="177" alt="Screenshot from 2026-06-10 10-28-37" src="https://github.com/user-attachments/assets/114b4590-7b96-4335-8cc6-64dee9f3fa29" />

---

### Caso 3 – Partículas e Pontuação Opcional

Execução da suíte referente ao tratamento de partículas de ligação e variações de pontuação em nomes de autores.

<img width="1203" height="177" alt="Screenshot from 2026-06-10 10-29-16" src="https://github.com/user-attachments/assets/fe2255a6-a12f-4074-b447-f4ed734309ea" />


---

### Caso 4 – Iniciais Agrupadas e Sobrenome

Execução da suíte referente à expansão de iniciais agrupadas e à seleção da representação mais completa do autor.

<img width="1203" height="177" alt="image" src="https://github.com/user-attachments/assets/f8df0c0e-beca-4d48-b0a7-109d9f0bef72" />


---

### Caso 5 – Deduplicação e Consolidação de IDs

Execução da suíte referente ao agrupamento de registros equivalentes e à definição do identificador padrão-ouro.

<img width="1203" height="177" alt="Screenshot from 2026-06-10 10-30-06" src="https://github.com/user-attachments/assets/d60308c8-1a30-4a84-add5-9359962ea184" />


---

### Suíte de Exceções

Execução da suíte responsável pela validação estrutural dos dados e pelo tratamento das exceções definidas para o projeto.


<img width="1203" height="177" alt="Screenshot from 2026-06-10 10-31-13" src="https://github.com/user-attachments/assets/c27da53d-5ec2-47fb-a108-89ed86d4ee80" />

