# Day 3 — Assertions, Exceptions & Negative Testing

## Goal
Improve test quality by:
- writing precise assertions
- understanding the difference between negative scenarios and invalid input
- using exceptions (`pytest.raises`) correctly

---

## ✅ What I did
- added validation logic to domain functions
- implemented exception handling (`ValueError`)
- wrote negative tests (both with and without exceptions)
- used `pytest.raises` for invalid input scenarios
- fixed bug in reward calculation (percentage logic)
- moved business logic from tests into `src/game/logic.py`
- fixed imports using `PYTHONPATH`
- cleaned up test structure

---

## What I learned (practical)

### Assertions
- `assert x == y` is used for exact value checks
- `assert x is True` / `assert x is False` is better for boolean logic than `== True` / `== False`
- good assertions should show expected behavior clearly

### Negative testing

#### 1. Valid negative scenario (no exception)
System behaves correctly, but the result is negative:

```python
assert can_afford(10, 50) is False
```

#### 2. Invalid input (exception)
System should reject incorrect data:

```python
with pytest.raises(ValueError):
    can_afford(-10, 50)
```

### Exceptions vs False
| Case | Behavior |
|------|----------|
| valid input, but condition not met | return `False` |
| invalid input (bad data) | raise `ValueError` |

### Function types (important mental model)

#### Check (returns bool)
- `can_afford` → `True` / `False`

#### Action (changes state)
- `buy_item` → returns new balance

#### Calculation (derived value)
- `calculate_purchase_reward` → returns computed reward

### Percentage calculations
Wrong:
```python
bonus = base_reward + bonus_percent // 100
```

Correct:
```python
bonus = base_reward * bonus_percent // 100
```

Key idea:
- percent is a multiplier, not a value to add

### Floor division (`//`)
```python
10 // 3 == 3
```

Used to:
- avoid floats
- keep reward values as integers

### Imports and project structure
After moving logic to `src/`:
- Python could not find modules
- fixed with:

```powershell
$env:PYTHONPATH = ".\src"
```

---

## ❌ Problems (real)
- mixed business logic inside test files
- confused bonus value with percentage
- used `+` instead of `*` for percent calculation
- wrote tests that did not fully reflect real logic
- did not separate negative result from invalid input at first
- got import error after moving logic into `src/`

---

## Root cause
- focused on code shape before fully understanding business meaning
- did not clearly separate:
  - check functions
  - action functions
  - calculation functions
- treated percent like a normal numeric value instead of a relative value
- delayed proper file separation until tests were already growing

---

## Fix
- moved domain logic into `src/game/logic.py`
- left only fixtures and tests in `tests/test_game_logic.py`
- corrected reward formula to use multiplication for percent calculation
- added exception checks for invalid input
- used `PYTHONPATH` so tests can import modules from `src`

---

## What I would do differently
- separate logic and tests earlier
- define business meaning of each function before writing tests
- verify formula manually before writing expected values
- be more consistent with assertion style (`is True` / `is False`)
- add boundary cases earlier for calculations

---

## Connection to project
This day is important because it builds the base for future API and integration testing:
- precise assertions will be needed for API responses
- exception thinking will help with negative API scenarios
- separating valid negative behavior from invalid input is critical for backend validation
- cleaner project structure is necessary before scaling test suites

Current functions still simulate game economy rules:
- purchase validation
- quest access rules
- item type validation
- reward calculation

---

## ➡️ Next step
- deepen fixture usage
- practice parametrization with clearer principles
- improve test data management
- add more boundary and edge-case thinking to domain tests

---

## ❓ Open questions
- when should simple checks like `can_purchase_item` also validate negative values?
- when is parametrization helpful, and when does it make tests harder to read?
- when should fixture data stay inline, and when should it be shared?
- how should test files be split as the project grows?

---

## Key takeaways
- `False` is for valid negative outcomes
- `ValueError` is for invalid input
- percent calculations require multiplication, not addition
- test logic must reflect business meaning, not just syntax
- logic belongs in `src/`, tests belong in `tests/`
