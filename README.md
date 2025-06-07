# Technical Test for Backend Developer

## Project Structure

### Microservices

```
inventory/
products/
```

## Ports

Products: 8000
Inventory: 8001

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and configure environment variables
3. Build and run with Docker:
```bash
docker-compose up --build
```

## API Documentation

### Products

You can access the products API documentation at [http://localhost:8000/docs](http://localhost:8000/docs)

You can also access the health check at [http://localhost:8000/health](http://localhost:8000/health)

### Inventory

You can access the products API documentation at [http://localhost:8001/docs](http://localhost:8001/docs)

You can also access the health check at [http://localhost:8001/health](http://localhost:8001/health)

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

## Testing

Run tests using:

```bash
# Run all tests
docker-compose run --rm products pytest
docker-compose run --rm inventory pytest

# Run with coverage
docker-compose run --rm products pytest --cov=app
docker-compose run --rm inventory pytest --cov=app
```