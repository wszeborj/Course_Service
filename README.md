* [General info])(#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More detailed information about modules](#more-detailed-information-about-modules)
* [Application view](#application-view)


## General info
<details>
<summary>Click here to see general information about <b>Project</b>!</summary>
<b>Course Service - Online Learning Platform API</b>.
FastAPI-based REST API for managing online programming courses, lessons, and exercises.
</details>

## Tools & Technologies
<ul>
<li>Python</li>
<li>fastapi[standard]</li>
<li>uvicorn[standard]</li>
<li>pydantic</li>
<li>pydantic-settings</li>
<li>sqlalchemy</li>
<li>alembic</li>
<li>mypy</li>
</ul>

## Setup
Clone the repo
```bash
git clone https://github.com/wszeborj/Course_Service.git
```
Go to project folder
```bash
cd course_service
```
Install poetry
```bash
pip install poetry
```
Install all modules
```bash
poetry install
```
Create PostgreSQL database
```bash
psql -U postgres
#provide password
CREATE DATABASE course_service_db;
\q
```

## Application features
<ul>
<li>Course Management: Create, read, update, delete courses</li>
<li>Lesson Management: Organize lessons within courses</li>
<li>Exercise Management: Add exercises to lessons</li>
<li>RESTful API: Clean, intuitive endpoints</li>
<li>Auto Documentation: Swagger UI & ReDoc</li>
<li>Database: PostgreSQL with SQLAlchemy ORM</li>
<li>Validation: Pydantic models for data validation</li>
</ul>

## Application View
