# Test Plan — AbacusAI Desktop (Chat)

## 1. Objective

This test plan defines the manual testing strategy applied to the AbacusAI desktop application (Chat mode), focusing on:
- UI stability during prompt submission
- User experience (chat usability)
- Behavior under adverse network conditions
- Behavior when handling complex prompts

## 2. Scope

### 2.1. In scope

- AbacusAI application for Windows (desktop client)
- Functionalities of:
  - login and conversation initiation
  - message (prompt) submission
  - response display
  - shortcuts and basic interaction in the message input field

### 2.2. Out of scope

- AbacusAI backend / internal servers
- Advanced model configuration flows
- External integrations (Slack, email, etc.)
- Performance under massive load (automated stress testing)

## 3. Test Environment

- Operating System: Windows 11
- Application: AbacusAI Desktop (Chat)
- Connection: Home internet with the ability to simulate outages (by turning off Wi-Fi)
- Test user: Tester's personal account

## 4. Test Types

- **Functional testing:** Verify that message submission, response, and basic navigation work as expected.
- **Usability testing:** Observe feedback clarity, UI organization, and ease of use.
- **Robustness/Error testing:** Evaluate behavior under:
  - network outage during prompt submission
  - long or complex prompts
- **Exploratory testing:** Explore the system for unexpected behaviors or UX improvements.

## 5. Test Items

The following test cases have been defined:

- `TC-001` — Behavior under multiple and contradictory instructions
- `TC-002` — Enter and Shift+Enter shortcuts in the message field

New test cases may be added as new relevant scenarios are identified.

## 6. Entry Criteria

Testing can begin when:

- The AbacusAI desktop application is installed and accessible.
- The tester has a valid account and can log in.
- Internet connection is available (for normal tests) or controlled (for network outage tests).

## 7. Exit Criteria

Testing is considered complete when:

- All planned test cases for the cycle have been executed.
- All defects found have been:
  - logged in `01-bug-reports/` (BR-001 to BR-004), and
  - prioritized with severity/priority.
- Test case execution results have been recorded (Status: Passed/Failed).

## 8. Risks and Dependencies

### 8.1. Risks

- Network instability may affect the reproducibility of some scenarios.
- Application version changes may alter behavior between tests.

### 8.2. Dependencies

- Availability of AbacusAI servers.
- Continuous access to the test account.

## 9. Traceability

- **BR-001** — related to window stability/main prompt submission flow.
- **BR-002** — related to conversation tab management usability.
- **BR-003** — related to robustness under network outage conditions.
- **BR-004** — related to message formatting experience (line breaks).

Each bug report is associated with one or more test types described in sections 4 and 5.