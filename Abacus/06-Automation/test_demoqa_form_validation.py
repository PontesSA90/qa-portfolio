from playwright.sync_api import sync_playwright


def test_practice_form_invalid_email():
    """
    Cenário negativo:
    Preencher o formulário Practice Form com e-mail inválido
    e verificar se o campo é marcado como inválido pelo navegador.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Acessar a página de Practice Form
        page.goto("https://demoqa.com/automation-practice-form")

        # 2. Preencher o formulário com e-mail inválido
        page.fill("#firstName", "Estevam")
        page.fill("#lastName", "Pontes")
        page.fill("#userEmail", "email-invalido")  # falta @ e domínio
        page.click("label[for='gender-radio-1']")  # selecionar Male
        page.fill("#userNumber", "1234567890")     # telefone válido

        # 3. Clicar em Submit
        page.click("#submit")

        # 4. Verificar se o campo de e-mail ficou marcado como inválido
        email_input = page.locator("#userEmail")

        # Alguns navegadores usam pseudo-classes CSS como :invalid;
        # aqui vamos checar o atributo 'class' que fica diferente
        classes = email_input.get_attribute("class") or ""

        # Esperamos que a classe contenha 'field-error' ou algo do tipo,
        # mas o DemoQA pode não ter isso. Então vamos checar o estado de validação nativo do input.
        is_valid = page.evaluate("(el) => el.checkValidity()", email_input.element_handle())

        assert is_valid is False, "Esperava que o e-mail fosse considerado inválido pelo navegador."

        print("\n✅ Teste passou: e-mail inválido foi detectado como inválido.")

        browser.close()