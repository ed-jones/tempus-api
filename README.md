# tempus_api

## Setup

### Install Dependencies

Install python3

Install python3-venv

Install libpq-dev

Install [Poetry](https://python-poetry.org/docs/)

Install [PostgreSQL](https://www.postgresql.org/download/)

### Setup Python Environment

Activate virtual environment `$ poetry shell`

Install poetry dependencies: `$ poetry install`

### Initialize Database

Switch to postgres user and enter postgres: `$ sudo -u postgres psql`

Create database: `# CREATE DATABASE tempus;`

Create tempus user account: `# CREATE USER tempus WITH PASSWORD '%yLb36Bs2G';`

Grant tempus user access to tempus database: `# GRANT ALL PRIVILEGES ON database tempus TO tempus;`

Exit: `# exit`

Start db: `$ sudo service postgresql start`

Stamp head: `$ flask db stamp head`

Migrate db: `$ flask db migrate`

Upgrade db: `$ flask db upgrade`

### Run Server

Run flask: `$ flask run`

# API Documentation

Please read `tempus_api.v1.yaml`
