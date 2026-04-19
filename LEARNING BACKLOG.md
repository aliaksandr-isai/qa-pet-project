# 📌 LEARNING BACKLOG

---

## 🎯 Project Direction

Game Economy Backend Service

Focus:

* Stateful backend system
* Business logic testing
* Full testing pyramid
* CI/CD and quality gates

---

# 🧭 Sprint 1 — Python + pytest Foundations

## Sprint Goal

Build confidence with pytest and basic Python needed for test automation.

---

## ✅ Done

### Day 1

* pytest installed and configured
* repository initialized
* basic tests created:

  * math
  * strings
  * lists
  * dicts
* first successful test run

---

## 🔄 In Progress

### Day 2

* extend test coverage
* add more edge cases
* introduce negative scenarios

---

## ⏭️ Next

### Day 3

* exceptions handling
* pytest.raises

### Day 4

* fixtures introduction
* reusable test data

### Day 5

* parametrization
* data-driven tests

### Day 6

* domain logic functions (game context):

  * add_gold
  * spend_gold

### Day 7

* cleanup
* README alignment
* test structure review

---

# 🔜 Sprint 2 — API Testing Foundations

## Planned Focus

* REST basics
* httpx
* status codes
* headers
* auth basics
* test design for API

## Expected Outcome

* API test framework
* smoke & regression suites
* reusable fixtures

---

# 🔜 Sprint 3 — Backend MVP (Game Economy)

## Planned Focus

* FastAPI service
* PostgreSQL
* Docker
* Alembic

## Core Entities

* Player
* Item
* Order
* Inventory

## Core Flow

* purchase flow (order lifecycle)

---

# 🔜 Sprint 4 — Integration Testing

## Planned Focus

* testcontainers
* DB validation
* state consistency

## Key Checks

* balance updates
* inventory updates
* order state transitions

---

# 🔜 Sprint 5 — CI/CD & Quality Gates

## Planned Focus

* GitHub Actions
* lint (ruff, black)
* pytest in CI
* coverage
* Allure reports

---

# 🔜 Sprint 6 — E2E Testing

## Planned Focus

* Playwright
* basic JavaScript
* flaky test handling
* Gherkin (limited)

---

# 🧠 Observations (to fill during progress)

## What works well

*

## What is difficult

*

## Questions

*

---

# 📈 Progress Rule

* 1 day = 1 task
* 1 task = 1 commit
* If blocked → write it down here

---

# 🚧 Risks

* Overengineering backend
* Adding too many technologies too early
* Losing focus on testing

Mitigation:

* Keep backend simple
* Focus on tests first
* Follow sprint structure

---

# 📊 Definition of Done (High-Level)

* Backend runs via docker-compose
* PostgreSQL integrated
* API implemented (auth, shop, orders, inventory, rewards)
* Full testing pyramid implemented
* CI pipeline configured
* Allure reports generated
* Documentation complete
