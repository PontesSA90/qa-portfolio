# QA Portfolio — PontesSA90

Este repositório serve como um portfólio prático, demonstrando habilidades em Quality Assurance (QA) manual e teste de API.

## 1. Testes de QA Manual (AbacusAI Desktop)

Esta seção do portfólio foca na aplicação de técnicas de QA manual sobre o aplicativo desktop do AbacusAI (modo Chat).

### Estrutura

- `01-bug-reports/` — Relatórios de bug e melhorias identificados:
  - BR-001 — Travamento da janela do aplicativo ao enviar segundo prompt
  - BR-002 — Melhoria na renomeação de abas de conversa
  - BR-003 — Falta de aviso de falha de rede durante envio de prompt
  - BR-004 — Remoção de múltiplas linhas em branco ao enviar mensagem (melhoria de usabilidade)

- `02-test-cases/` — Casos de teste documentados para funcionalidades do AbacusAI:
  - TC-001 — Comportamento frente a instruções múltiplas e contraditórias
  - TC-002 — Atalhos Enter e Shift+Enter e preservação de quebras de linha

- `03-test-plan/` — Plano de teste inicial para o aplicativo AbacusAI Desktop.

- `05-evidence/` — Evidências visuais (prints) que suportam os bug reports.

## 2. Testes de API (JSONPlaceholder com Postman)

Esta seção demonstra habilidades em teste de API utilizando a ferramenta Postman e uma API pública de demonstração (JSONPlaceholder). Estes testes são exercícios práticos e não estão relacionados ao produto AbacusAI.

### Estrutura

- `02-test-cases/` — Casos de teste documentados para cenários de API:
  - API-001 — Criar post via API pública JSONPlaceholder (POST /posts)
  - API-002 — Criar post SEM título via API pública JSONPlaceholder (POST /posts)

- `04-api-tests-postman/` — Contém informações sobre a collection do Postman utilizada e pode abrigar o arquivo de exportação da collection.

### Habilidades demonstradas

- Criação e execução de requisições HTTP (GET, POST) no Postman.
- Análise de respostas de API (status codes, JSON body).
- Planejamento e documentação de casos de teste para cenários de sucesso e de erro/validação em APIs.

## Habilidades Gerais Demonstradas

- Criação de bug reports claros, com passos para reproduzir, resultado atual/esperado, severidade e prioridade.
- Criação de casos de teste (test cases) a partir de cenários reais e requisitos de API.
- Elaboração de um plano de teste.
- Uso de Git e GitHub para versionamento e organização de artefatos de QA.
- Testes exploratórios de usabilidade e comportamento sob falhas (ex.: queda de rede).
- Pensamento crítico para identificar e documentar comportamentos inesperados ou melhorias.

---

### Próximos Passos

Este portfólio está em constante evolução. Novas seções e exemplos podem ser adicionados para expandir as habilidades demonstradas.