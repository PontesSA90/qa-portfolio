from playwright.sync_api import sync_playwright


def test_demoqa_text_box():
    """
    Teste simples de preenchimento de formulário no DemoQA.
    Valida que o Playwright está funcionando e que conseguimos interagir com elementos.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False para ver o navegador
        page = browser.new_page()

        # 1. Acessar a página de Text Box do DemoQA
        page.goto("https://demoqa.com/text-box")

        # 2. Preencher os campos do formulário
        page.fill("#userName", "Estevam Pontes")
        page.fill("#userEmail", "estevam@example.com")
        page.fill("#currentAddress", "Rua Exemplo, 123")
        page.fill("#permanentAddress", "Avenida Teste, 456")

        # 3. Clicar no botão Submit
        page.click("#submit")

        # 4. Validar que os dados aparecem na área de output
        output = page.locator("#output").inner_text()

        assert "Estevam Pontes" in output
        assert "estevam@example.com" in output
        assert "Rua Exemplo, 123" in output

        print("\n✅ Teste passou: formulário preenchido e validado com sucesso!")

        browser.close()