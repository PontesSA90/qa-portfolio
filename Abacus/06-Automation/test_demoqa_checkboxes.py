from playwright.sync_api import sync_playwright


def test_demoqa_checkboxes():
    """
    Teste de interação com checkboxes na página Check Box do DemoQA.
    Seleciona algumas opções e valida o texto de resultado.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Acessar a página de Check Box
        page.goto("https://demoqa.com/checkbox")

        # 2. Expandir a árvore de opções
        page.click(".rct-option-expand-all")  # botão 'Expand all'

        # 3. Selecionar alguns checkboxes (por exemplo: Desktop e Documents)
        page.click("label[for='tree-node-desktop']")
        page.click("label[for='tree-node-documents']")

        # 4. Capturar o texto de resultado
        result_text = page.locator("#result").inner_text()

        # 5. Verificar se as seleções aparecem no resultado
        assert "desktop" in result_text.lower()
        assert "documents" in result_text.lower()

        print("\n✅ Teste passou: checkboxes selecionados aparecem no resultado.")

        browser.close()