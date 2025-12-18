# Test Automation with Playwright and Python

This section of the portfolio demonstrates UI (User Interface) test automation skills using the Playwright library with Python.

## Tools Used

- **Playwright:** Browser automation framework.
- **Python:** Programming language.
- **Pytest:** Testing framework for Python.

## Environment Setup

1.  **Virtual Environment:**
    ```bash
    py -m venv venv
    venv\Scripts\activate
    ```
2.  **Install Dependencies:**
    ```bash
    pip install playwright pytest
    playwright install
    ```

## Implemented Tests

### `test_demoqa_form.py`

-   **Objective:** Validate the filling and submission of a "Text Box" form on the DemoQA website.
-   **URL:** `https://demoqa.com/text-box`
-   **Description:** The test automates the following steps:
    1.  Opens the browser and navigates to the form page.
    2.  Fills in the "Full Name", "Email", "Current Address", and "Permanent Address" fields.
    3.  Clicks the "Submit" button.
    4.  Verifies that the filled data is correctly displayed in the output area after submission.
-   **How to Run:**
    ```bash
    pytest abacus/06-automation/test_demoqa_form.py -v
    ```

### `test_demoqa_form_validation.py`

- Negative scenario: invalid email in the Practice Form.
- Demonstrates browser-side validation (`checkValidity()`).

### `test_demoqa_checkboxes.py`

- Interaction with a checkbox tree on the "Check Box" page.
- Validates that selected options appear in the result area.

## Skills Demonstrated

-   Test automation environment setup (venv, Playwright, Pytest).
-   Writing automation scripts to interact with UI elements (fill fields, click buttons).
-   Validation of results in the user interface.
-   Use of CSS selectors to identify elements.
-   Organization of tests in Python files.

## Next Steps

-   Add more automated test scenarios (e.g., login, error validations).
-   Explore other Playwright features (screenshots, waits, etc.).
-   Integrate with test reporting tools.