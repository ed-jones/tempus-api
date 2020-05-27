# tempus_api

## First time setup

### Set up Virtual Environment

Create virtual environemnt: `$ python -m venv venv`

Enable virtual environment: `$ source venv/bin/activate`

### Database setup

Configure db in `config.py` file

Stamp head: `$ flask db stamp head`

Migrate db: `$ flask db migrate`

Upgrade db `$ flask db upgrade`

### Run

Run flask: `$ flask run`

## Package Management

Add package: `$ poetry add package-name`

Install packages: `$ poetry install`

# API Documentation

Please read `tempus_api.v1.yaml`
