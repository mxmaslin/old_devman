# Microservice for Search Index of Phone Numbers

## Script features

The script performs following actions:

1. Connects to database.
2. Gets existing entries.
3. For each existing entry:
    1. Gets its phone number.
    2. Normalizes it to national format
    3. Writes it to corresponding entry's column.
4. Gets entries for last `N` minutes.
5. For each entry:
    1. Gets its phone number.
    2. Normalizes it to national format
    3. Writes it to corresponding entry's column.
6. Waits `N` minutes.
7. Repeats.
    
## Preparing to start script

1. Install the requirements: `pip install -r requirements.txt`
2. Obtain database dump.
    - Host: shopscore.devman.org
    - Port: 5432
    - User: score
    - Password: Rysherat2
    - Database: shop
3. Extract the dump to your postgres.
4. Run migration to add a column for normalized phone numbers in national format: `alembic upgrade head`

## Starting the script

    $ cd app
    $ python phones.py

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
