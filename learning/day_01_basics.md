# NOTES

## Day 1

### Learned

- How pytest discovers and runs tests (`test_*.py`, `test_*` functions)
- Difference between `assert` checking truthy values vs explicit comparison (`assert x` vs `assert x == expected`)
- Basic Python data structures:
  - list (append, remove, pop, sort)
  - dict (key access, mutation, `.get()` vs `[]`)
- Difference between safe and unsafe access:
  - `user["key"]` → raises `KeyError`
  - `user.get("key")` → returns `None`
- How to test exceptions using `pytest.raises`
- Basic understanding of loops (`for x in list`) and iteration
- Difference between mutation and non-mutation operations (e.g. `.sort()` vs `sorted()`)

---

### Problems

- Confusion between list element and list itself (`n` vs `numbers`)
- Incorrect usage of operators (`^` instead of `**`)
- Writing asserts without checking actual expected value (truthy checks)
- Misunderstanding of how `.pop()` and `.remove()` work
- Confusion between `all()` and `any()`
- Using Python syntax from other languages (e.g. `print` without parentheses)
- Git issues:
  - dubious ownership error
  - first merge conflict / merge commit (vim)

---

### Commands

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1

pip install pytest

pytest -v

git init
git add .
git commit -m "day 1: basic pytest tests"

git remote add origin <repo>
git push -u origin main

git pull
git push