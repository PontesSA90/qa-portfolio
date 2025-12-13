# Test Plan — AbacusAI Desktop (Chat)

## 1. Objetivo

Este plano de teste define a estratégia de testes manuais aplicada ao aplicativo desktop do AbacusAI (modo Chat), com foco em:
- estabilidade da interface durante o envio de prompts
- experiência do usuário (usabilidade de chat)
- comportamento em condições de rede adversas
- comportamento frente a prompts complexos

## 2. Escopo

### 2.1. Incluído no escopo

- Aplicativo AbacusAI para Windows (client desktop)
- Funcionalidades de:
  - login e abertura de conversa
  - envio de mensagens (prompts)
  - exibição de respostas
  - atalhos e interação básica no campo de mensagem

### 2.2. Fora do escopo

- Backend / servidores internos do AbacusAI
- Fluxos avançados de configuração de modelos
- Integrações externas (Slack, e-mail, etc.)
- Performance sob carga massiva (stress test automatizado)

## 3. Ambiente de Teste

- Sistema Operacional: Windows 11
- Aplicativo: AbacusAI Desktop (Chat)
- Conexão: internet residencial com possibilidade de simular queda (desligando Wi‑Fi)
- Usuário de teste: conta pessoal do testador

## 4. Tipos de Teste

- **Teste funcional:** Verificar se o envio de mensagens, resposta e navegação básica funcionam conforme esperado.
- **Teste de usabilidade:** Observar clareza de feedback, organização da interface e facilidade de uso.
- **Teste de robustez/erro:** Avaliar comportamento em:
  - queda de rede durante envio de prompt
  - prompts longos ou complexos
- **Teste exploratório:** Explorar o sistema em busca de comportamentos inesperados ou melhorias de UX.

## 5. Itens de Teste

Os seguintes casos de teste foram definidos:

- `TC-001` — Comportamento frente a instruções múltiplas e contraditórias
- `TC-002` — Atalhos Enter e Shift+Enter e preservação de quebras de linha

Novos casos de teste podem ser adicionados conforme forem identificados novos cenários relevantes.

## 6. Critérios de Entrada

Os testes podem começar quando:

- O aplicativo AbacusAI desktop está instalado e acessível.
- O testador possui uma conta válida e consegue fazer login.
- A conexão de internet está disponível (para testes normais) ou controlada (para testes de queda de rede).

## 7. Critérios de Saída

Os testes são considerados concluídos quando:

- Todos os casos de teste planejados para o ciclo foram executados.
- Todos os defeitos encontrados foram:
  - registrados em `01-bug-reports/` (BR-001 a BR-004), e
  - priorizados com severidade/prioridade.
- Resultados de execução dos casos de teste foram registrados (Status: Passou/Falhou).

## 8. Riscos e Dependências

### 8.1. Riscos

- Instabilidade de rede pode afetar a reprodutibilidade de alguns cenários.
- Mudanças de versão do aplicativo podem alterar o comportamento entre testes.

### 8.2. Dependências

- Disponibilidade dos servidores do AbacusAI.
- Acesso contínuo à conta de teste.

## 9. Rastreamento (Traceability)

- **BR-001** — relacionado a estabilidade da janela/fluxo principal de envio de prompts.
- **BR-002** — relacionado à usabilidade de gerenciamento de abas/conversas.
- **BR-003** — relacionado a robustez em condição de queda de rede.
- **BR-004** — relacionado à experiência de formatação de mensagens (quebras de linha).

Cada bug report está associado a um ou mais tipos de teste descritos nas seções 4 e 5.