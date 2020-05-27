# tempus_api

## Setup

### Install Dependencies

Install python3

Install python3-pip

Install python3-venv

Install [Poetry](https://python-poetry.org/docs/)

Install [PostgreSQL](https://www.postgresql.org/download/)

### Setup Python Environment

Install poetry dependencies and create virtual environment: `$ poetry install`

### Initialize Database

Replace `'%yLb36Bs2G'` in `config.py` file with a secure password

Switch to postgres user and enter postgres: `$ sudo -u postgres psql`

Create database: `# CREATE DATABASE tempus;`

Create tempus user account: `# CREATE USER tempus WITH PASSWORD <your secure password>;`

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
