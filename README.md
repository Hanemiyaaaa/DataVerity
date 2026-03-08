# Dataverity

Dataverity is a service for **data quality monitoring, dataset validation, and reproducible data pipelines**.

The goal of the project is to help organizations **trust their data** by detecting anomalies, validating business rules, and tracking how datasets are produced.

---

# 🚀 What is Dataverity?

Modern companies rely on data-driven decisions, but data pipelines often suffer from:

* duplicates
* missing values
* schema inconsistencies
* transformation errors
* undocumented data changes
* non-reproducible calculations

Dataverity provides a **central service** that monitors data pipelines and ensures datasets remain reliable and transparent.

---

# ✨ Core Features

### Data Quality Monitoring

Automatically evaluate datasets using multiple quality indicators:

* duplicate detection
* missing values ratio
* schema validation
* statistical anomaly detection
* business rule validation

Each dataset receives a **Data Quality Score** that summarizes its reliability.

---

### Validation Rules

Users can define validation rules such as:

* column uniqueness
* value ranges
* allowed categories
* schema constraints
* custom business rules

Violations are detected automatically and logged.

---

### Reproducible Data Pipelines

Every pipeline execution stores:

* dataset version
* business date
* pipeline configuration
* validation results

This allows users to **reproduce calculations exactly**.

---

### Data Lineage

Track how datasets are created and transformed.

The lineage graph shows:

* upstream data sources
* transformations
* downstream datasets

This helps teams understand data dependencies.

---

### Observability

Dataverity monitors:

* pipeline executions
* validation results
* anomalies
* schema changes
* rule violations

---

# 🏗 Architecture

Dataverity is built as a modular service.

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

# 📦 Technology Stack

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic

### Data Processing

* Apache Spark
* Pandas

### Orchestration

* Apache Airflow

### Frontend

* React
* TypeScript

### Infrastructure

* Docker
* Docker Compose

---

# 📊 Data Quality Metrics

Dataverity calculates dataset reliability using the following indicators:

| Metric           | Description                  |
| ---------------- | ---------------------------- |
| Duplicate Rate   | Percentage of duplicate rows |
| Null Ratio       | Ratio of missing values      |
| Schema Errors    | Data type mismatches         |
| Range Violations | Out-of-range values          |
| Rule Violations  | Failed business rules        |

These indicators are aggregated into a **Data Quality Score**.

---

# 🔁 Reproducibility

Dataverity stores metadata for every pipeline execution:

* dataset version
* business date
* transformation steps
* validation rules
* quality metrics

This ensures calculations can always be reproduced.

---

# 🛠 Running the Project

Clone the repository:

```
git clone https://github.com/yourusername/dataverity.git
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

# 🤝 Contributing

Contributions are welcome.

You can help by improving:

* validation rules
* anomaly detection
* data lineage visualization
* UI dashboards

---

# 📄 License

MIT License

---

# Vision

Dataverity aims to become a **reliable service for monitoring data quality and ensuring transparency in data pipelines**.

---

# Dataverity (Русская версия)

Dataverity — это сервис для **мониторинга качества данных, валидации датасетов и обеспечения воспроизводимости data-pipeline**.

Цель проекта — помочь компаниям **доверять своим данным**, обнаруживая ошибки, аномалии и нарушения бизнес-правил.

---

# 🚀 Что делает Dataverity

В современных компаниях решения принимаются на основе данных, однако data-pipeline часто сталкиваются с проблемами:

* дубликаты записей
* пропущенные значения
* ошибки типов данных
* некорректные трансформации
* изменения схемы данных
* невозможность воспроизвести расчёты

Dataverity предоставляет **централизованный сервис**, который контролирует качество данных и делает пайплайны прозрачными.

---

# ✨ Основные возможности

### Мониторинг качества данных

Сервис автоматически оценивает датасеты по нескольким метрикам:

* дубликаты
* доля пропущенных значений
* соответствие схемы
* статистические аномалии
* нарушения бизнес-правил

На основе этих показателей формируется **Data Quality Score**.

---

### Проверка правил

Пользователь может задавать правила валидации:

* уникальность колонок
* допустимые диапазоны значений
* список допустимых категорий
* типы данных
* пользовательские бизнес-правила

---

### Воспроизводимость расчётов

Каждый запуск пайплайна сохраняет:

* версию датасета
* business date
* конфигурацию пайплайна
* правила проверки
* результаты валидации

Это позволяет **точно воспроизвести расчёты**.

---

### Lineage данных

Dataverity отслеживает происхождение данных:

* источники данных
* этапы трансформации
* зависимые датасеты

Это помогает понимать структуру data-pipeline.

---

### Наблюдаемость пайплайнов

Сервис отслеживает:

* запуск пайплайнов
* ошибки
* аномалии
* изменения схемы
* нарушения правил

---

# 🎯 Цель проекта

Создать сервис, который позволит компаниям:

* доверять своим данным
* быстро находить ошибки в data-pipeline
* контролировать качество данных
* воспроизводить расчёты
