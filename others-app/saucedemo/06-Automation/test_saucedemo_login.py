from playwright.sync_api import sync_playwright


def test_saucedemo_login_success():
    """
    Positive scenario:
    Login with standard_user should succeed and redirect to the inventory page.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Navigate to the SauceDemo login page
        page.goto("https://www.saucedemo.com/")

        # 2. Fill in valid username and password
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")

        # 3. Click Login
        page.click("#login-button")

        # 4. Verify that login was successful
        assert "inventory.html" in page.url

        titulo = page.locator(".title").inner_text()
        assert "Products" in titulo

        print("\n✅ Test passed: Login successful")

        browser.close()


def test_saucedemo_login_locked_out_user():
    """
    Negative scenario:
    Login with locked_out_user should fail and show a proper error message.
    """
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

        print("\n✅ Test passed: locked_out_user received an error message.")

        browser.close()