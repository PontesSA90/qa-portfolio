from playwright.sync_api import sync_playwright


def test_practice_form_invalid_email():
    """
    Negative scenario:
    Fill the Practice Form with an invalid email
    and verify that the field is marked as invalid by the browser.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Navigate to the Practice Form page
        page.goto("https://demoqa.com/automation-practice-form")

        # 2. Fill the form with an invalid email
        page.fill("#firstName", "Estevam")
        page.fill("#lastName", "Pontes")
        page.fill("#userEmail", "invalid-email")  # missing @ and domain
        page.click("label[for='gender-radio-1']")  # select Male
        page.fill("#userNumber", "1234567890")     # valid phone number

        # 3. Click Submit
        page.click("#submit")

        # 4. Verify that the email field is marked as invalid
        email_input = page.locator("#userEmail")

        # Some browsers use CSS pseudo-classes like :invalid;
        # here we check the 'class' attribute which may differ
        classes = email_input.get_attribute("class") or ""

        # We expect the class to contain 'field-error' or similar,
        # but DemoQA may not have this. So we check the native input validation state.
        is_valid = page.evaluate("(el) => el.checkValidity()", email_input.element_handle())

        assert is_valid is False, "Expected the email to be considered invalid by the browser."

        print("\n✅ Test passed: invalid email was detected as invalid.")

        browser.close()