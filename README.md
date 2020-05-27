# tempus_api

## First time setup

### Poetry Setup

Install [Poetry](https://python-poetry.org/docs/)

Install [PostgreSQL](https://www.postgresql.org/download/)

Install dependencies: `$ poetry install`

### Database setup

Configure db in `config.py` file

Stamp head: `$ flask db stamp head`

Migrate db: `$ flask db migrate`

Upgrade db `$ flask db upgrade`

### Run

Run flask: `$ flask run`

# API Documentation

Please read `tempus_api.v1.yaml`
