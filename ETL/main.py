from extract import extract_products, extract_users
from transform import transform_products, transform_users
from load import load_data_to_postgres


def run_pipeline():
    """
    Runs the ETL pipeline: Extracts data from the Fake Store API, transforms it, and loads it into a PostgreSQL database.
    """
    
    # Extract data
    print("Starting ETL pipeline...")
    products_df = extract_products()
    users_df = extract_users()

    # Transform data
    print("Starting data transformation...")
    transformed_products_df = transform_products(products_df)
    transformed_users_df = transform_users(users_df)

    # Load data into PostgreSQL
    print("Loading data into PostgreSQL...")
    load_data_to_postgres(transformed_products_df, 'products')
    load_data_to_postgres(transformed_users_df, 'users')  

    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()  