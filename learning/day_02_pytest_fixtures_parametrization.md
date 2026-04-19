# Day 2 — Pytest Fixtures & Parametrization

## 🎯 Goal
Understand how to reduce duplication in tests using fixtures and how to run the same test logic against multiple inputs using parametrization.

---

## ✅ What I did
- created basic pytest fixtures (`sample_player`, `shop_item`)
- wrote simple domain functions (`can_start_quest`, `can_purchase_item`, `is_valid_item_type`)
- implemented basic tests using fixtures
- added parametrized tests for business rules
- connected constants from another module (`VALID_ITEM_TYPES`)

---

## 🧠 What I learned (practical)

### Tools / Framework
- pytest automatically injects fixture values into test functions by name
- only functions starting with `test_` are executed as tests
- `@pytest.mark.parametrize` runs the same test multiple times with different inputs

### Language / Concepts
- boolean expressions like `a >= b` directly return `True` or `False`
- type hints (`item_type: str`) do not enforce types at runtime, they are only hints
- `set` is useful for fast membership checks (`in`)

### Testing
- one test should verify one rule, not multiple unrelated things
- parametrization is useful when the logic is the same but inputs differ
- test names and parameter names must reflect real meaning, not mislead
- tests should check business rules, not random relationships between data

---

## ❌ Problems (real)
- used wrong data types (`"100"` instead of `100`)
- copied logic between functions without changing meaning (purchase logic used level instead of balance)
- wrote test that accessed empty list (`inventory[0]`) → runtime error
- created test without `test_` prefix → pytest didn’t run it
- used misleading parameter name (`valid_type` for invalid values)
- added unclear edge case `(0, 0, True)` without thinking about domain meaning

---

## 🔍 Root cause
- focused on syntax instead of understanding business logic
- did not clearly define what each function is supposed to check
- mixed up test data structure with test intent
- tried to “use more data” in tests without understanding why
- assumed pytest runs all functions automatically

---

## 🛠 Fix
- corrected types (balance → int)
- fixed function signatures to match domain logic (balance vs price)
- simplified boolean logic using direct return expressions
- renamed test functions to match pytest conventions
- corrected parametrization variable names
- removed or questioned ambiguous test cases

---

## 🔁 What I would do differently
- first define the rule (what is being tested), then write the test
- avoid using unrelated data just to “make test more complex”
- always check if test actually verifies intended behavior
- keep tests simple and readable instead of “smart”
- validate names of parameters and fixtures for clarity

---

## 🧩 Connection to project
- fixtures will later be used for API clients, auth tokens, DB setup
- parametrization will be used for:
  - API validation (different payloads)
  - order status flows
  - edge cases (balance, level, item types)
- current functions simulate core business rules of game economy:
  - player progression
  - purchase logic
  - item validation

---

## ➡️ Next step
- learn better assertion patterns (not just equality)
- start testing negative scenarios (invalid inputs, errors)
- understand how to test exceptions (`raises`)
- improve test design (boundary, equivalence classes)

---

## ❓ Open questions
- when to use fixture vs inline data?
- how to organize fixtures when project grows?
- how to structure constants and domain logic (classes vs modules)?
- when parametrization becomes too complex and should be avoided?

---

## 📌 Key takeaways
- fixtures = reusable test state, not business logic  
- parametrization = one rule, many inputs  
- tests must reflect intent, not just execute code