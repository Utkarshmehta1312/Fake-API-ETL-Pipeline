from sqlalchemy import create_engine

host = "localhost"
port = "5432"  
username = "postgres"
password = "****"
dbname = "fake_store_db"

def load_data_to_postgres(df, table_name):
    """
    Loads the given DataFrame into a PostgreSQL database table.
    """
    # Create a connection string
    connection_string = f"postgresql://{username}:{password}@{host}:{port}/{dbname}"
    
    # Create a SQLAlchemy engine
    engine = create_engine(connection_string)
    
    # Load data into the specified table
    df.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"Data loaded into table '{table_name}' successfully.")
