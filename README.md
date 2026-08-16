# Amazon Backend System

[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green.svg)](https://fastapi.tiangolo.com/)
[![SQLAlchemy 2.0](https://img.shields.io/badge/SQLAlchemy-2.0%20Async-orange.svg)](https://www.sqlalchemy.org/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Search-purple.svg)](https://www.trychroma.com/)
[![Docker](https://img.shields.io/badge/Docker-Supported-blue.svg)](https://www.docker.com/)

A complete, production-ready, enterprise-grade backend system replicating Amazon's core services, built with **FastAPI**, **SQLAlchemy 2.0 Async**, **Motor (MongoDB)**, **Redis**, and **ChromaDB Vector Store**.

---

## 🌟 Key Architecture & Features

- **Authentication & Security**: JWT Access/Refresh tokens, bcrypt password hashing, OAuth2 Bearer, Role-Based Access Control (RBAC: Admin, Customer, Vendor, Manager).
- **User Management**: Profile CRUD, Avatar upload, Account Deactivation, Password updates.
- **Product Catalog**: Categories, Subcategories, Brands, Discounts, SKU tracking, Pagination, Sorting, Filtering.
- **Semantic Search Engine**: ChromaDB vector similarity embeddings search, Hybrid keyword search, Autocomplete suggestions, Trending items.
- **Inventory & Warehouse**: Multi-warehouse stock management, Stock reservation during checkout, Low-stock alerts.
- **Cart & Wishlist**: MongoDB document-backed dynamic shopping cart, Move to Cart from Wishlist.
- **Address Management**: Multiple shipping addresses per user with default flags.
- **Orders & Tracking**: Checkout pipeline, Stock reservation, Status transitions (`pending` -> `processing` -> `shipped` -> `delivered` / `cancelled`), Live tracking timeline.
- **Payment Processing**: Dummy Payment Gateway supporting UPI, Credit Card, Debit Card, Cash On Delivery (COD), Refunds.
- **PDF Invoice Generation**: Automatic PDF invoice generation using ReportLab stored in `/uploads/invoice/`.
- **Recommendation Engine**: Vector-based similar product discovery and frequently bought together items.
- **Notifications & Audit**: MongoDB notifications feed, Unread count, Audit logging.
- **Admin & Analytics**: Dashboard metrics (total revenue, total orders, low stock counters), User management, Warehouse creation.
- **Resilient Multi-DB Manager**: Runs out-of-the-box using SQLite, In-Memory ChromaDB, and resilient Mongo/Redis failover layers, with full support for PostgreSQL, real MongoDB, and Redis in production.

---

## 📁 Directory Structure

```
Amazon_Backend/
├── app/
│   ├── main.py                # FastAPI Application Entrypoint & Middleware Stack
│   ├── config.py              # Pydantic BaseSettings Environment Configuration
│   ├── database.py            # Multi-DB Manager (SQL, Mongo, Redis, ChromaDB)
│   ├── dependencies.py        # Dependency Injectors (DB, Current User, RBAC, Services)
│   ├── exceptions.py          # Custom Exceptions & Exception Handlers
│   ├── middleware.py          # Logging, Correlation ID, Execution Timer, Rate Limiting
│   ├── security.py            # Hashing (bcrypt) & JWT Token Utils
│   ├── utils.py               # ReportLab PDF Invoice Generator & Embeddings Utils
│   ├── constants.py           # App Enums (Roles, Statuses, Payment Methods)
│   ├── models/
│   │   ├── sql_models.py      # SQLAlchemy 2.0 Async Entity Models
│   │   └── mongo_models.py    # MongoDB Pydantic Document Schemas
│   ├── schemas/
│   │   └── all_schemas.py     # Pydantic v2 DTO Request/Response Schemas
│   ├── repositories/          # Data Access Layer (Repository Pattern)
│   │   ├── base_repository.py
│   │   ├── user_repository.py
│   │   ├── product_repository.py
│   │   ├── order_repository.py
│   │   ├── cart_repository.py
│   │   ├── wishlist_repository.py
│   │   ├── search_repository.py
│   │   └── notification_repository.py
│   ├── services/              # Business Logic Layer
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── product_service.py
│   │   ├── search_service.py
│   │   ├── cart_service.py
│   │   ├── order_service.py
│   │   ├── payment_service.py
│   │   ├── invoice_service.py
│   │   └── recommendation_service.py
│   └── routers/               # API Endpoints (/api/v1/...)
│       ├── auth_router.py
│       ├── users_router.py
│       ├── products_router.py
│       ├── categories_router.py
│       ├── search_router.py
│       ├── cart_router.py
│       ├── orders_router.py
│       ├── payments_router.py
│       ├── invoices_router.py
│       ├── recommendations_router.py
│       └── analytics_router.py
├── seed/
│   └── seed_data.py           # Initial Data Seeder (Admin User, Catalog, Warehouses)
├── tests/                     # Pytest Async Integration Suite
├── docs/                      # ER Diagram, API Docs & Postman Collection
├── uploads/                   # Local Filesystem Storage (Invoices, Images, Embeddings)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Python 3.13+ installed.

### 2. Environment Setup

```bash
# Navigate to project directory
cd Amazon_Backend

# Create Python Virtual Environment
python -m venv .venv

# Activate Virtual Environment
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install Dependencies
pip install -r requirements.txt
```

### 3. Seed Database & Run Server

```bash
# Seed default data (Creates Admin user: admin@amazon.com / Admin@123456)
python -m seed.seed_data

# Run FastAPI Development Server
uvicorn app.main:app --reload
```

Server will start at `http://127.0.0.1:8000`.

---

## 🔗 Swagger API Documentation & ReDoc

- **Interactive Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc Documentation**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Running Pytest Test Suite

```bash
pytest -v tests/
```

---

## 🐳 Running with Docker & Docker Compose

To deploy with PostgreSQL, MongoDB, Redis, and FastAPI in Docker:

```bash
docker-compose up --build
```

---

## 📜 Default Credentials

| Role | Email | Password |
|---|---|---|
| **Admin** | `admin@amazon.com` | `Admin@123456` |
