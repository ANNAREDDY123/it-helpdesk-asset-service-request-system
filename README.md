# it-helpdesk-asset-service-request-system
FastAPI IT Helpdesk Asset Service Request System with JWT Authentication, Asset Management, Service Request Management, Request Assignment, Reports, Search, SQLAlchemy ORM, Pagination, Logging, Docker Support, and Unit Tests.
# IT Helpdesk Asset Service Request System

## Features

- JWT Authentication
- Asset Management (CRUD)
- Service Request Management
- Request Assignment
- Reports & Search
- SQLAlchemy ORM
- SQLite Database
- Docker Support
- Logging
- Basic Unit Tests



## Setup Instructions

### Install Dependencies


pip install -r requirements.txt


### Run Project


py -m uvicorn main:app --reload


Swagger


http://127.0.0.1:8000/docs


## Environment Variables


SECRET_KEY=helpdesk_secret_key
ALGORITHM=HS256


## API Examples

- POST `/auth/register`
- POST `/auth/login`
- POST `/assets`
- POST `/requests`


## Docker Deployment


docker build -t helpdesk-system .
docker run -p 8000:8000 helpdesk-system


## Assumptions

- Asset tag must be unique.
- Closed requests cannot be updated.
- Resolution date is automatically recorded when a request is marked as **Resolved**.
- One asset can have multiple service requests.
