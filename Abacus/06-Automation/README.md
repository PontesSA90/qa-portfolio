# Automação de Testes com Playwright e Python

Esta seção do portfólio demonstra habilidades em automação de testes de UI (User Interface) utilizando a biblioteca Playwright com Python.

## Ferramentas Utilizadas

- **Playwright:** Framework de automação de navegador.
- **Python:** Linguagem de programação.
- **Pytest:** Framework de testes para Python.

## Configuração do Ambiente

1.  **Ambiente Virtual:**
    ```bash
    py -m venv venv
    venv\Scripts\activate
    ```
2.  **Instalação de Dependências:**
    ```bash
    pip install playwright pytest
    playwright install
    ```

## Testes Implementados

### `test_demoqa_form.py`

-   **Objetivo:** Validar o preenchimento e submissão de um formulário de "Text Box" no site DemoQA.
-   **URL:** `https://demoqa.com/text-box`
-   **Descrição:** O teste automatiza os seguintes passos:
    1.  Abre o navegador e navega até a página do formulário.
    2.  Preenche os campos "Full Name", "Email", "Current Address" e "Permanent Address".
    3.  Clica no botão "Submit".
    4.  Verifica se os dados preenchidos são exibidos corretamente na área de output após a submissão.
-   **Como Rodar:**
    ```bash
    pytest abacus/06-automation/test_demoqa_form.py -v
    ```

## Habilidades Demonstradas

-   Configuração de ambiente para automação de testes (venv, Playwright, Pytest).
-   Escrita de scripts de automação para interagir com elementos de UI (preencher campos, clicar botões).
-   Validação de resultados na interface do usuário.
-   Uso de seletores CSS para identificar elementos.
-   Organização de testes em arquivos Python.

## Próximos Passos

-   Adicionar mais cenários de teste automatizados (ex: login, validações de erro).
-   Explorar outras funcionalidades do Playwright (screenshots, waits, etc.).
-   Integrar com relatórios de teste.