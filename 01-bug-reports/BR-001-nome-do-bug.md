# BR-001 — [Abacus IA em teste]

- **Ambiente:** Windows 11 / Aplicativo AbacusAI (desktop) / Data: 2025-12-12
- **Pré-condição:** usuário logado, Conversa antiga aberta
- **Aplicação afetada:** Aplicativo AbacusAI para Windows (janela principal)
- **Frequência:** [3 tentativas]
- **Workaround:** Fechar a janela (Task manager) e reabrir o aplicativo

## Passos para reproduzir   
1. Enviar primeiro prompt
2. Esperar a resposta
3. Enviar segundo prompt na mesma conversa

## Resultado atual
Após enviar o segundo prompt na mesma conversa, a janela do aplicativo AbacusAI deixa de responder. O Windows exibe o alerta “The window is not responding”, oferecendo as opções “Reopen”, “Close” e “Keep Waiting”. É necessário fechar ou reiniciar a janela para voltar a usar o aplicativo. Não houve perda aparente de dados ao reabrir.

## Resultado esperado
O aplicativo deve processar o segundo prompt normalmente, sem travar a interface, exibindo a resposta ou uma mensagem de erro clara, mantendo a janela responsiva.

## Evidência
- `05-evidence/BR-001-print1` (print)

## Severidade
Alta -  Bloqueia o uso do aplicativo na sessão atual, exigindo que o usuário feche/reabra a janela.

## Prioridade
Alta, Afeta o fluxo principal (envio de prompts) e prejudica o uso contínuo do produto.