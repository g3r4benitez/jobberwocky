# Publications-API

## Requirements

Python 3.9+

## Installation
Install the required packages in your local environment (ideally virtualenv, conda, etc.).

```sh
pip install -r requirements.txt
```

## Setup
1. Duplicate the `.env.example` file and rename it to `.env`
2. Ask a teammate for the .env file

## Migrations
### Create Migration

```sh
alembic revision --autogenerate -m "comment"
```

### Run Migrations

```sh
alembic upgrade head
```

## Project

### Run It

1. Start your app with:

```sh
python3 -m uvicorn app.main:app --reload --port 9009
```

2. Go to [http://localhost:8000/docs](http://localhost:8000/docs).

