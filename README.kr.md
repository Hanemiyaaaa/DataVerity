# Dataverity

Dataverity는 데이터 품질을 모니터링하고 데이터셋을 검증하며 재현 가능한 데이터 파이프라인을 보장하기 위한 서비스입니다.

이 프로젝트의 목표는 데이터 이상을 탐지하고 비즈니스 규칙을 검증하며 데이터 변환 과정을 추적함으로써 조직이 자신의 데이터를 신뢰할 수 있도록 돕는 것입니다.

---

# Dataverity란 무엇인가

현대 조직은 데이터 기반 의사결정에 크게 의존합니다. 그러나 데이터 파이프라인은 종종 다음과 같은 문제를 겪습니다.

* 중복 데이터
* 누락된 값
* 스키마 불일치
* 변환 오류
* 문서화되지 않은 데이터 변경
* 재현할 수 없는 계산

Dataverity는 데이터 처리 전체 과정에서 데이터 품질을 모니터링하는 중앙 서비스입니다.

---

# 주요 기능

## 데이터 품질 모니터링

Dataverity는 여러 품질 지표를 사용하여 데이터셋을 평가합니다.

* 중복 데이터 탐지
* 결측값 비율
* 스키마 검증
* 통계적 이상 탐지
* 비즈니스 규칙 검증

이 지표들은 **Data Quality Score**로 통합됩니다.

---

## 데이터 검증 규칙

사용자는 다음과 같은 규칙을 정의할 수 있습니다.

* 컬럼 고유성
* 값 범위 제한
* 허용된 카테고리
* 스키마 제약 조건
* 사용자 정의 비즈니스 규칙

규칙 위반은 자동으로 탐지되고 기록됩니다.

---

## 재현 가능한 데이터 파이프라인

각 파이프라인 실행은 다음 메타데이터를 저장합니다.

* 데이터셋 버전
* 비즈니스 날짜
* 변환 단계
* 검증 규칙
* 파이프라인 설정

이를 통해 언제든지 동일한 계산을 재현할 수 있습니다.

---

## 데이터 Lineage

Dataverity는 데이터의 출처와 변환 과정을 추적합니다.

Lineage 그래프는 다음을 보여줍니다.

* 데이터 소스
* 변환 단계
* 중간 데이터셋
* 종속 데이터셋

---

## 데이터 관측성

시스템은 다음을 지속적으로 모니터링합니다.

* 파이프라인 실행
* 데이터 품질 지표
* 이상 탐지
* 스키마 변경
* 규칙 위반

---

# 아키텍처

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

# 기술 스택

Backend:

* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic

데이터 처리:

* Apache Spark
* Pandas

오케스트레이션:

* Apache Airflow

Frontend:

* React
* TypeScript

인프라:

* Docker
* Docker Compose

---

# 금융 데이터 준비

Dataverity는 금융 기관의 재무 안정성 지표 계산에 필요한 데이터를 준비하는 데 사용할 수 있습니다.

이 서비스는 다음을 보장합니다.

* 데이터 검증
* 데이터 일관성
* 계산 재현성
* 데이터 추적 가능성

---

# 프로젝트 실행

저장소를 클론합니다.

```
git clone https://github.com/Hanemiyaaaa/DataVerity
```

서비스를 실행합니다.

```
docker compose up
```

사용 가능한 서비스:

```
Frontend: http://localhost:3000
Backend API: http://localhost:8000
Airflow: http://localhost:8080
```

---

# License

MIT License
