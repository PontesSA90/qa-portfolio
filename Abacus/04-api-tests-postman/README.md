# Testes de API — JSONPlaceholder (Postman)

Esta pasta está relacionada à collection do Postman **`04-api-tests-postman`**, usada para exercícios de teste de API em uma API pública de demonstração.  
Estes testes **não** estão ligados ao produto AbacusAI; são apenas para treinar habilidades de QA de API.

## API sob teste

- **Nome:** JSONPlaceholder
- **Site:** https://jsonplaceholder.typicode.com
- **Descrição:** API REST pública fake, usada para testes e prototipagem.

## Collection no Postman

No Postman, foi criada a collection:

- `04-api-tests-postman`

Requests principais:

- `GET All Users` — `GET /users`
- `GET Single User by ID` — `GET /users/1`
- `API001-test` — `POST /posts` (criar post de exemplo)

## Casos de teste relacionados (no repositório)

Os casos de teste documentados em Markdown ficam na pasta `02-test-cases/`:

- `API-001-create-post-jsonplaceholder.md` — valida o cenário de criação de post via `POST /posts` com corpo JSON válido.

## Como usar (resumo)

1. Abrir o Postman.
2. Acessar a collection `04-api-tests-postman`.
3. Executar as requests (`GET` ou `POST`) conforme descrito nos casos de teste em `02-test-cases/`.
4. Validar:
   - Status code da resposta.
   - Corpo (JSON) retornado.
   - Comportamento em casos de sucesso e, futuramente, de erro/validação.