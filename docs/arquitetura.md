# Arquitetura da Solução

## Introdução

Este documento descreve a arquitetura da solução desenvolvida para o Trabalho Prático da disciplina Técnicas de Programação para Plataformas Emergentes (TPPE).

O sistema tem como objetivo realizar a curadoria e a deduplicação de registros científicos provenientes de diferentes fontes de informação, identificando autores equivalentes, corrigindo inconsistências textuais e consolidando registros em um padrão-ouro.

Além disso, a implementação foi desenvolvida em Python utilizando a metodologia **Test-Driven Development (TDD)**, com validação por meio de testes automatizados implementados no framework **Pytest**.

---

##  Visão Geral da Arquitetura

- A arquitetura adota uma organização simples e centralizada, adequada ao escopo do trabalho proposto.

- A classe principal `Curador` concentra as regras de negócio relacionadas à normalização de nomes, identificação de equivalências entre registros, seleção da representação canônica e consolidação de identificadores.

- A solução utiliza métodos auxiliares reutilizáveis para evitar duplicação de lógica e promover maior coesão entre os diferentes casos de deduplicação.

O processamento ocorre em quatro etapas principais:

1. Validar a estrutura dos dados;
2. Normalizar os registros textuais;
3. Identificar autores equivalentes;
4. Consolidar os registros em um padrão-ouro.

---

##  Estrutura do Projeto

```text
unb-tppe-trabalho-pratico-2026-1
│
├── README.md
├── pytest.ini
├── .gitignore
│
├── docs
│   ├── arquitetura.md
│   ├── base_dados.md
│   └── processo_tdd.md
│
└── src
    ├── __init__.py
    ├── curador.py
    ├── exception.py
    ├── main.py
    │
    └── tests
        ├── test_caso1.py
        ├── test_caso2.py
        ├── test_caso3.py
        ├── test_caso4.py
        ├── test_caso5.py
        ├── test_excecoes.py
        │
        └── data
            └── dados_curadoria_800.json
```

---

##  Componente Principal

###  Classe `Curador`

A classe `Curador` representa o núcleo da aplicação.

Sua responsabilidade consiste em coordenar as operações de normalização, comparação e deduplicação dos registros científicos.

As funcionalidades implementadas incluem:

- Correção de inconsistências tipográficas;
- Padronização de nomes;
- Tratamento de partículas de ligação;
- Expansão de iniciais;
- Identificação de registros equivalentes;
- Consolidação de identificadores redundantes;
- Validação estrutural da base de dados.

---

##  Métodos Auxiliares

###  Normalização de Texto

Os métodos desta categoria realizam a padronização textual dos registros.

| Método | Responsabilidade |
|----------|----------|
| `remover_acentos()` | Remover acentuação para comparação textual |
| `limpar_apostrofos()` | Padronizar caracteres de apóstrofo |
| `limpar_espacos()` | Eliminar espaços excedentes |
| `normalizar_caixa()` | Padronizar o uso de letras maiúsculas e minúsculas |
| `normalizar_nome()` | Aplicar o processo completo de normalização |

---

###  Comparação e Agrupamento

Os métodos desta categoria apoiam a identificação de registros equivalentes.

| Método | Responsabilidade |
|----------|----------|
| `assinatura()` | Gerar uma assinatura textual para agrupamento |
| `_eh_inicial()` | Identificar abreviações e iniciais |
| `_expandir_iniciais()` | Desmembrar blocos de iniciais agrupadas |
| `pontuar_nome()` | Avaliar a qualidade de uma representação textual |
| `melhor_nome()` | Selecionar a melhor grafia disponível |

---

###  Implementação dos Casos de Deduplicação

Os métodos desta categoria implementam diretamente os cinco casos previstos no enunciado.

| Método | Caso |
|----------|----------|
| `curar_tipografia()` | Caso 1 – Diferenças Tipográficas |
| `curar_iniciais()` | Caso 2 – Sobrenome e Iniciais |
| `curar_particulas()` | Caso 3 – Partículas e Pontuação Opcional |
| `curar_agrupados()` | Caso 4 – Iniciais Agrupadas |
| `consolidar_ids()` | Caso 5 – Consolidação de IDs |

---

###  Validação

Os métodos desta categoria verificam a integridade dos dados de entrada.

| Método | Responsabilidade |
|----------|----------|
| `obter_id_ouro()` | Determinar o menor identificador válido |
| `processar_base_dados()` | Validar a estrutura dos registros |

---

##  Estratégia de Deduplicação

A deduplicação dos registros baseia-se na construção de assinaturas textuais derivadas dos nomes dos autores.

A assinatura é composta pelo sobrenome principal e pela inicial do primeiro nome, permitindo agrupar diferentes representações de um mesmo autor.

Após a formação dos grupos equivalentes, o sistema executa as seguintes etapas:

1. Normalizar os nomes candidatos;
2. Avaliar cada representação por meio de uma função de pontuação;
3. Selecionar a grafia considerada mais completa;
4. Associar todos os registros equivalentes à representação escolhida;
5. Consolidar os identificadores utilizando o menor ID disponível.

Essa abordagem permite tratar abreviações, omissões de partículas, diferenças tipográficas e variações de escrita sem utilizar valores fixos previamente conhecidos.

---

##  Fluxo de Processamento

```text
Base de Dados
      │
      ▼
Validação Estrutural
      │
      ▼
Normalização dos Nomes
      │
      ▼
Geração de Assinaturas
      │
      ▼
Agrupamento de Registros
      │
      ▼
Seleção da Melhor Grafia
      │
      ▼
Consolidação de IDs
      │
      ▼
Padrão-Ouro
```

---

##  Tratamento de Exceções

O sistema implementa exceções específicas para representar violações das regras de integridade dos dados.

### FormatoInvalidoError

Exceção lançada quando a estrutura dos registros não atende aos requisitos mínimos esperados.

### IdInvalidoError

Exceção lançada quando um identificador possui valor inválido ou incompatível com as regras definidas.

O tratamento explícito dessas exceções contribui para a robustez do sistema e para a previsibilidade do comportamento durante o processamento.

---

##  Estratégia de Testes

A validação da implementação utiliza o framework **Pytest**.

A suíte de testes contempla:

- Testes unitários;
- Testes parametrizados;
- Testes agrupados por categorias;
- Testes de exceção;
- Execução isolada por caso;
- Execução conjunta de toda a suíte.

Os marcadores definidos no arquivo `pytest.ini` permitem executar individualmente cada caso de deduplicação ou a suíte completa.

A execução simultânea de todos os testes ocorre sem dependência de ordem ou compartilhamento indevido de estado, atendendo aos critérios de correção definidos pelo enunciado.

### Marcadores Disponíveis

| Marcador | Finalidade |
|-----------|-----------|
| `caso1` | Testes do Caso 1 |
| `caso2` | Testes do Caso 2 |
| `caso3` | Testes do Caso 3 |
| `caso4` | Testes do Caso 4 |
| `caso5` | Testes do Caso 5 |
| `excecoes` | Testes de validação e tratamento de erros |

---

##  Considerações Finais

- A arquitetura adotada prioriza simplicidade, reutilização de código e separação de responsabilidades.

- A utilização de métodos auxiliares comuns reduz duplicações e permite que os diferentes casos de deduplicação compartilhem mecanismos de normalização e comparação.

- A estratégia implementada atende aos cinco cenários de deduplicação propostos, incorpora validação estrutural dos dados e mantém compatibilidade com a metodologia Test-Driven Development aplicada ao longo do projeto.

- Os resultados obtidos demonstram a conformidade da implementação com os requisitos definidos no enunciado e com os critérios de avaliação estabelecidos para o trabalho prático.
