from playwright.sync_api import sync_playwright


def test_saucedemo_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Acessar a página de login do SauceDemo
        page.goto("https://www.saucedemo.com/")

       

        # 2. Preencher usuário e senha válidos
        # (você vai precisar descobrir os seletores dos campos e do botão)
        page.fill("#user-name","standard_user")
        page.fill("#password", "secret_sauce")


        # 3. Clicar em Login
        page.click("#login-button")


        # 4. Verificar se o login foi bem sucedido
        # (Dica: pode ser pela URL, por um texto na tela, ou pelos dois)
        titulo = page.locator(".title").inner_text()

        assert "inventory.html" in page.url
        assert "Products" in titulo
        print("\n Teste passou: Login efetuado com sucesso")
        browser.close()

    
    def test_saucedemo_login_locked_out_user():
    # login que NÃO deve funcionar (locked_out_user)
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto("https://www.saucedemo.com/")

            page.fill("#user-name", "locked_out_user")
            page.fill("#password", "secret_sauce")

            page.click("#login-button")

            error_elem = page.locator("[data-test='error']")
            error_text = error_elem.inner_text()

            assert "locked out" in error_text.lower()

            print("\n✅ Teste passou: usuário bloqueado recebeu mensagem de erro.")

        browser.close()