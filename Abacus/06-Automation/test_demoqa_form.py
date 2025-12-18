from playwright.sync_api import sync_playwright


def test_demoqa_text_box():
    """
    Simple form filling test on DemoQA.
    Validates that Playwright is working and that we can interact with elements.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False to see the browser
        page = browser.new_page()

        # 1. Navigate to the DemoQA Text Box page
        page.goto("https://demoqa.com/text-box")

        # 2. Fill the form fields
        page.fill("#userName", "Estevam Pontes")
        page.fill("#userEmail", "estevam@example.com")
        page.fill("#currentAddress", "Rua Exemplo, 123")
        page.fill("#permanentAddress", "Avenida Teste, 456")

        # 3. Click the Submit button
        page.click("#submit")

        # 4. Validate that the data appears in the output area
        output = page.locator("#output").inner_text()

        assert "Estevam Pontes" in output
        assert "estevam@example.com" in output
        assert "Rua Exemplo, 123" in output

        print("\n✅ Test passed: form filled and validated successfully!")

        browser.close()