from playwright.sync_api import sync_playwright


def test_demoqa_checkboxes():
    """
    Test checkbox interaction on the DemoQA Check Box page.
    Selects some options and validates the result text.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Navigate to the Check Box page
        page.goto("https://demoqa.com/checkbox")

        # 2. Expand the options tree
        page.click(".rct-option-expand-all")  # 'Expand all' button

        # 3. Select some checkboxes (e.g., Desktop and Documents)
        page.click("label[for='tree-node-desktop']")
        page.click("label[for='tree-node-documents']")

        # 4. Capture the result text
        result_text = page.locator("#result").inner_text()

        # 5. Verify that the selections appear in the result
        assert "desktop" in result_text.lower()
        assert "documents" in result_text.lower()

        print("\n✅ Test passed: selected checkboxes appear in the result.")

        browser.close()