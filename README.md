# QA Game Economy Backend Pet Project

## 📌 Project Vision

**Game Economy Backend Service**

This project is a QA-focused backend system that simulates a simplified game economy for an RPG-like environment.

The system models:

* Player profile (level, balance)
* Shop with items
* Order/purchase flow
* Inventory management
* Reward mechanics (basic progression)

This is **not a game** and not a UI-driven product.

👉 It is an **API-first backend system designed for testing** complex stateful logic.

---

## 🎯 Project Goal

Build a backend service and fully cover it with a testing pyramid to gain hands-on experience in:

* API testing
* Test design
* Stateful system validation
* Integration testing with database
* Test data management
* CI/CD pipelines and quality gates
* E2E testing
* Test stability and flaky test handling

---

## 🧠 Key Concept

> This project focuses on testing a **stateful system with business logic**, not just CRUD endpoints.

Core idea:

* Validate transitions between states
* Ensure consistency between API and database
* Cover real-world flows end-to-end

---

## 🧩 Core Domain

### Entities

* User
* PlayerProfile
* Item
* Order
* InventoryEntry
* Reward

### Core Flows

* Authentication (JWT)
* View player profile
* Browse shop items
* Create order
* Pay order
* Fulfill order
* Update inventory
* Apply reward

---

## 🔄 Example Core Scenario

**Item Purchase Flow**

1. Player logs in
2. Player checks balance
3. Player creates order
4. Order goes through status flow:

   * CREATED → PAID → FULFILLED
5. Balance is reduced
6. Item is added to inventory

This single scenario is covered by:

* API tests
* Integration tests (DB validation)
* E2E tests

---

## ⚠️ Scope restrictions

To keep the project focused and achievable:

❌ No real-time mechanics
❌ No multiplayer
❌ No complex combat system
❌ No heavy frontend
❌ No microservices architecture

✅ Simple, testable backend
✅ Clear business rules
✅ Deterministic behavior for testing

---

## 🏗️ Tech Stack

### Backend

* Python 3.11+
* FastAPI
* SQLAlchemy 2.0
* Alembic
* PostgreSQL

### Testing

* pytest
* httpx
* testcontainers
* Faker

### Code Quality

* ruff
* black
* pre-commit

### E2E

* Playwright (primary)
* Gherkin/Cucumber (limited usage)

### CI/CD

* GitHub Actions

### Reporting

* Allure

---

## 🧪 Testing Pyramid

* Unit tests (20+)
* API tests (50+)
* Integration tests (20+)
* E2E tests (10+)

---

## ⚙️ Infrastructure

* Docker
* docker-compose (app + postgres)
* Alembic migrations

Run:

```
docker-compose up
```

---

## 🚀 CI/CD Pipeline

Pipeline runs on every push/PR and includes:

* Lint checks (ruff, black)
* pytest execution
* Coverage threshold (≥70%)
* Smoke tests (< 2 minutes)
* Allure report generation (artifact)

---

## 📊 Project Structure

```
qa-pet-project/
  src/
    app/
  tests/
    unit/
    api/
    integration/
    e2e/
  migrations/
  docker/
  .github/workflows/
  docker-compose.yml
  Dockerfile
  pyproject.toml
  README.md
  LEARNING_BACKLOG.md
  NOTES.md
```

---

## 📚 Learning Approach

* 1 task per day (60–90 min)
* 1 commit per task
* Focus on practical application
* No unnecessary theory

---

## 📈 Current Progress

### Sprint 1 — Python + pytest foundation

* ✅ Day 1: pytest setup, basic tests

(see LEARNING_BACKLOG.md for details)

---

## 🧾 Notes

All learning notes, mistakes, and findings are documented in:

```
NOTES.md
```

---

## 💬 Final Goal

By completing this project, the goal is to confidently demonstrate:

* Practical QA engineering skills
* Ability to design and test complex systems
* Understanding of CI/CD and test automation pipelines

This project serves as a **portfolio-level artifact** for QA Lead / Senior QA roles.
