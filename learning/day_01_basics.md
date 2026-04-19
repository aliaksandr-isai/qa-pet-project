# Day 1 — pytest foundations

## 🎯 Goal
Set up pytest and write first working tests to build a foundation for further QA automation work.

---

## ✅ What I did
- Created project structure
- Set up virtual environment (venv)
- Installed pytest
- Wrote first tests for:
  - math functions
  - strings
  - lists
  - dictionaries
- Ran test suite successfully (`pytest -v`)
- Pushed project to GitHub

---

## 🧠 What I learned (practical)

### pytest basics
- pytest discovers tests in files named `test_*.py`
- test functions must start with `test_`
- `assert` provides readable failure output
- how to run tests from CLI

### Python basics for testing
- list operations:
  - `append`, `remove`, `pop`, `sort`
- dict operations:
  - access via `[]`
  - safe access via `.get()`
- difference between:
  - `user["key"]` → raises error
  - `user.get("key")` → returns `None`

### Control flow
- how `for x in list` works (iteration over values, not indexes)
- understanding variable scope inside loops

### Testing behavior
- difference between:
  - checking truthy values (`assert something`)
  - checking expected result (`assert result == expected`)
- how to test exceptions using:
  with pytest.raises(...)

### Git basics (practical)
- initial repo setup
- commit / push workflow
- handling remote changes (`git pull`)
- first merge commit
- interaction with git editor (vim)

---

## ❌ Problems (real)
- Confusion between list element and list itself (`n` vs `numbers`)
- Incorrect operator usage (`^` instead of `**`)
- Misunderstanding of how `.pop()` and `.remove()` work
- Writing asserts without checking expected value
- Wrong assumption about which assert failed
- Using incorrect Python syntax (e.g. old-style `print`)
- Git issues:
  - "dubious ownership" error
  - first merge after remote changes
  - unexpected vim editor during merge

---

## 🔁 What I would do differently
- Start with fewer tests and build understanding step by step
- Verify behavior before writing assertions
- Avoid copying patterns without understanding underlying logic

---

## 🧩 Why this matters for the project

Although Day 1 tests are not domain-specific, they build the foundation for:

- testing business logic
- validating state changes
- writing reliable assertions
- understanding test failures

This is required before moving to:

- API testing
- database validation
- integration tests

---

## ➡️ Next step

Move from generic Python tests to domain-oriented logic:

### Currency operations
- add_currency
- spend_currency

### Inventory operations
- add_item
- remove_item

### Order lifecycle
- create_order
- change_order_status

Also introduce:
- pytest fixtures
- test parametrization

---

## ❓ Questions
- When should fixtures be used instead of inline test data?
- How to structure tests as the project grows?
- How to avoid duplicated test data?
- How to design domain-level test cases for entities like player, item, order?