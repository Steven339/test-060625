# Technical Test for Backend Developer

## Project Structure

### Microservices

```
inventory/
products/
```

### Diagram integration between microservices, inventory request to products to verify if the product exists and get information about it
```
mermaid
graph LR
    A[Inventory] -->|Request product information| B[Products]
    B -->|Product exists?| A
    B -->|No|> A
    B -->|Yes|> A
    A <--|Product information| B
```


### Infrastructure

```
infrastructure/
    api/
        dependencies.py
        routes.py
    db/
        models.py
        repositories.py
        session.py
```

### Domain

```
domain/
    models.py
    repositories.py
    schemas.py
    use_cases.py
```

### Application

```
application/
    event_publisher.py
    use_cases.py
```

### Tests

```
tests/
    conftest.py
    integration/
        test_endpoints.py
    unit/
        test_endpoints.py
```

### Docker

```
Dockerfile
docker-compose.yml
```

## Environment Variables

```
API_KEY=secret
PRODUCTS_API_KEY=secret # for inventory only to access the products api
```

## Running the API

```bash
docker-compose up --build
```

## Running Tests

```bash
docker-compose run --rm products pytest
docker-compose run --rm inventory pytest
```

## Running Tests with Coverage

```bash
docker-compose run --rm products pytest --cov=app
docker-compose run --rm inventory pytest --cov=app
```

## Running Tests with Coverage Report

```bash
docker-compose run --rm products pytest --cov=app --cov-report=html
docker-compose run --rm inventory pytest --cov=app --cov-report=html
```

## Database Migrations

This project uses Alembic for database migrations:

```bash
# Create a new migration
docker-compose run --rm products alembic revision --autogenerate -m "description"
docker-compose run --rm inventory alembic revision --autogenerate -m "description"

# Apply migrations
docker-compose run --rm products alembic upgrade head
docker-compose run --rm inventory alembic upgrade head
```

## Ports

Products: 8000
Inventory: 8001


## API Documentation

### Products

You can access the products API documentation at [http://localhost:8000/docs](http://localhost:8000/docs)

You can also access the health check at [http://localhost:8000/health](http://localhost:8000/health)

### Inventory

You can access the products API documentation at [http://localhost:8001/docs](http://localhost:8001/docs)

You can also access the health check at [http://localhost:8001/health](http://localhost:8001/health)

