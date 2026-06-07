# Trabalho Prático - TPPE (UnB - FCTE)

## Sobre o Trabalho

Este projeto consiste no desenvolvimento de um sistema de **Curadoria e Deduplicação de Dados Científicos** para repositórios de instituições de pesquisa. O objetivo principal é integrar diferentes fontes de dados (como o Currículo Lattes, ACM, ScienceDirect, etc.), identificar registos duplicados de autores numa mesma publicação e unificá-los para um **padrão-ouro**.

O desenvolvimento do projeto está dividido em duas etapas principais da disciplina de Técnicas de Programação para Plataformas Emergentes (TPPE):
1. **Etapa 1 (TDD - Test-Driven Development):** Implementação das unidades de código guiada por testes unitários automatizados.
2. **Etapa 2 (Refactoring):** Aplicação de operações de refatoração (Extrair Método, Substituir Método por Objeto-Método e Extrair Classe) para melhoria da qualidade do código.

### Casos de Deduplicação Implementados:
* **Caso 1 (Diferenças Tipográficas):** Padronização de acentuação, cedilhas e uso correto de caracteres (como o apóstrofo).
* **Caso 2 (Sobrenome + Iniciais):** Identificação de equivalência entre versões abreviadas e extensas de nomes, unificando para a versão completa.
* **Caso 3 (Partículas e Pontuação Opcional):** Tratamento de omissões de partículas (como "de") e pontos após abreviações.
* **Caso 4 (Iniciais Agrupadas + Sobrenome):** Preferência pela versão por extenso em vez de iniciais agrupadas (ex: "SH Guaraldi" para "Sérgio Henrique Guaraldi").
* **Caso 5 (IDs Diferentes para o Mesmo Autor):** Mapeamento de múltiplos registos da mesma pessoa para o ID de menor valor.

---

## Integrantes

| Foto | Nome | Matrícula |
| :---: | :---: | :---: |
| <a href="https://github.com/kalipassos"><img src="https://github.com/kalipassos.png" width="100px;" alt="Foto kalipassos"/><br /><sub><b>@kalipassos</b></sub></a> | - | - |
| <a href="https://github.com/SkywalkerSupreme"><img src="https://github.com/SkywalkerSupreme.png" width="100px;" alt="Foto SkywalkerSupreme"/><br /><sub><b>@SkywalkerSupreme</b></sub></a> | - | - |
| <a href="https://github.com/west7"><img src="https://github.com/west7.png" width="100px;" alt="Foto west7"/><br /><sub><b>@west7</b></sub></a> | - | - |

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** 
* **Framework de Testes:** 
* **Versão do Framework:** 

---

## Como executar os testes

