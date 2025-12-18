# QA Portfolio — PontesSA90

This repository serves as a practical portfolio, demonstrating skills in manual Quality Assurance (QA), API testing, and UI test automation.

## 1. Manual QA Testing (AbacusAI Desktop)

This section of the portfolio focuses on applying manual QA techniques to the AbacusAI desktop application (Chat mode).

### Structure

Artifacts related to AbacusAI are organized as follows:

- `abacus/01-bug-reports/` — Bug and improvement reports:
  - BR-001 — AbacusAI desktop window stops responding after sending second prompt
  - BR-002 — Conversation tab rename option unavailable in AbacusAI
  - BR-003 — No network failure warning when connection is lost during prompt submission
  - BR-004 — Blank lines inserted with Shift+Enter are ignored when sending the message (usability improvement)

- `abacus/02-test-cases/` — Documented test cases for AbacusAI functionality:
  - TC-001 — Behavior under multiple and contradictory instructions
  - TC-002 — Enter and Shift+Enter shortcuts in the chat message field
  - API-001 — Create post via JSONPlaceholder public API (POST /posts)
  - API-002 — Create post WITHOUT title via JSONPlaceholder public API (POST /posts)

- `abacus/03-test-plan/` — Initial test plan for the AbacusAI Desktop application.

- `abacus/04-api-tests-postman/` — Contains information about the Postman collection used and may store the exported collection file.

- `abacus/05-evidence/` — Visual evidence (screenshots) that support the bug reports.

## General Skills Demonstrated

- Creation of clear bug reports, with steps to reproduce, actual/expected results, severity, and priority.
- Design of test cases based on real scenarios and API requirements.
- Creation of a structured test plan.
- Use of Git and GitHub for versioning and organizing QA artifacts.
- Exploratory testing of usability and behavior under failure conditions (e.g., network outage).
- Critical thinking to identify and document unexpected behaviors or potential improvements.

---

## 2. API Testing (JSONPlaceholder with Postman)

This section demonstrates API testing skills using Postman and a public demo API (JSONPlaceholder). These tests are practice exercises and are not related to the AbacusAI product.

### Structure

- `abacus/02-test-cases/` — Documented test cases for API scenarios:
  - API-001 — Create post via JSONPlaceholder public API (POST /posts)
  - API-002 — Create post WITHOUT title via JSONPlaceholder public API (POST /posts)

- `abacus/04-api-tests-postman/` — Contains information about the Postman collection used and may store the exported collection file.

### Skills Demonstrated

- Creation and execution of HTTP requests (GET, POST) in Postman.
- Analysis of API responses (status codes, JSON body).
- Planning and documentation of test cases for both successful and error/validation API scenarios.

## 3. Test Automation (Playwright with Python)

This section demonstrates UI (User Interface) test automation skills using the Playwright framework with Python.

### Structure

- `abacus/06-automation/` — Contains the automation scripts and a detailed `README.md` about the setup and implemented tests.

### Skills Demonstrated

- Environment setup for test automation.
- Writing scripts to interact with UI elements.
- Validation of results in the user interface.
- Use of CSS selectors.

### Next Steps

This portfolio is continuously evolving. New sections and examples may be added to expand the range of demonstrated skills.