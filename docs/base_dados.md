# Documentação da Base de Dados de Simulação

Para aproximar o trabalho prático de um cenário real de curadoria de repositórios científicos, o grupo desenvolveu uma base de dados customizada em formato estruturado.

## 1. O Arquivo `dados_curadoria_800.json`
O arquivo simula o comportamento de um indexador integrado que sofreu com inserções duplicadas e divergências autodeclaratórias de pesquisadores.

* **Caminho no projeto:** `src/tests/data/dados_curadoria_800.json`
* **Link Direto no GitHub:** [Acessar dados_curadoria_800.json](https://github.com/SkywalkerSupreme/unb-tppe-trabalho-pratico-2026-1/blob/main/src/tests/data/dados_curadoria_800.json)
* **Volume de dados:** 800 registros simulados (amostra inicial contida no repositório).
* **Campos estruturados por registro:**
  * `id`: Identificador único do registro (sujeito a duplicidade de menor valor).
  * `nome`: Grafia do autor (contendo erros tipográficos, iniciais agrupadas e omissão de partículas).
  * `idade`, `sexo`, `profissao`, `email`, `orcid`, `instituicao`, `area_pesquisa`: Metadados científicos para enriquecimento do cenário de simulação.

## 2. Amostragem de Casos Identificados na Base
Os dados contidos no JSON foram mapeados para servir de insumo (*fixtures*) nos testes parametrizados, garantindo que o algoritmo real da Etapa 2 precise varrer e limpar inconsistências massivas de forma automatizada.
