# Dataverity

Dataverity is a service for monitoring data quality, validating datasets, and ensuring reproducible data pipelines.

The goal of the project is to help organizations trust their data by detecting anomalies, validating business rules, and tracking how datasets are produced and transformed.

---

# What is Dataverity?

Modern organizations rely heavily on data-driven decisions. However, data pipelines frequently encounter problems such as:

* duplicate records
* missing values
* schema inconsistencies
* transformation errors
* undocumented data changes
* non-reproducible calculations

Dataverity provides a centralized service that monitors the health and quality of datasets throughout the entire data lifecycle.

---

# Core Features

## Data Quality Monitoring

Dataverity evaluates datasets using several quality metrics:

* duplicate detection
* null value ratio
* schema validation
* statistical anomaly detection
* business rule validation

These indicators are aggregated into a **Data Quality Score**.

---

## Data Validation Rules

Users can define validation rules such as:

* column uniqueness
* value ranges
* allowed categories
* schema constraints
* custom business logic

Rule violations are detected automatically and stored for further analysis.

---

## Reproducible Data Pipelines

Each pipeline execution stores metadata including:

* dataset version
* business date
* transformation steps
* validation rules
* pipeline configuration

This allows teams to reproduce calculations exactly at any time.

---

## Data Lineage

Dataverity tracks the origin and transformation of data.

The lineage graph visualizes:

* upstream data sources
* transformations
* intermediate datasets
* downstream dependencies

---

## Data Observability

The system continuously monitors:

* pipeline executions
* dataset quality metrics
* anomalies
* schema changes
* rule violations

---

# Architecture

Dataverity is designed as a modular service architecture.

```
Frontend (React)
        │
        ▼
Backend API (FastAPI)
        │
 ┌──────┼───────────┐
 ▼      ▼           ▼
PostgreSQL     Airflow      Spark
(Database)     (ETL)     (Processing)
```

---

# Technology Stack

Backend:

* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic

Data Processing:

* Apache Spark
* Pandas

Orchestration:

* Apache Airflow

Frontend:

* React
* TypeScript

Infrastructure:

* Docker
* Docker Compose

---

# Financial Data Preparation

Dataverity can be used to prepare datasets required for financial ratio calculations in credit and financial organizations.

The service ensures that financial reporting data is:

* validated
* consistent
* reproducible
* traceable

This is particularly important for preparing data used in financial stability indicators.

---

# Running the Project

Clone the repository:

```
git clone https://github.com/Hanemiyaaaa/DataVerity
```

Start the services:

```
docker compose up
```

Available services:

```
Frontend: http://localhost:3000
Backend API: http://localhost:8000
Airflow: http://localhost:8080
```

---

# License

MIT License
