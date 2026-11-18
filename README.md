# Fake API ETL Pipeline

## Project Overview
An end-to-end ETL pipeline built using Python that extracts product and user data from the Fake Store API, transforms the data using Pandas, and loads it into a PostgreSQL database.

## Architecture

Extract → Transform → Load

- **Extract:** Retrieves products and users from Fake Store API using Python Requests.
- **Transform:** Cleans and transforms the extracted data using Pandas.
- **Load:** Loads transformed data into PostgreSQL using SQLAlchemy and psycopg2.

## Tech Stack
- Python
- Pandas
- Requests
- SQLAlchemy
- PostgreSQL
- psycopg2

## Project Structure

```text
FAKE_API_PROJECT/
├── ETL/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
├── .gitignore
├── requirements.txt
└── README.md
```

## How to Run

1. Clone this repository.
2. Install dependencies:

   `pip install -r requirements.txt`

3. Configure your PostgreSQL connection credentials.
4. Execute the pipeline:

   `python ETL/main.py`

## Output

The pipeline loads two datasets into PostgreSQL:
- Products
- Users