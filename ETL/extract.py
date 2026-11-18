import pandas as pd
import requests

BASE_URL = "https://fakestoreapi.com"

def extract_products():
    """
    Extracts product data from the Fake Store API.
    """
    response = requests.get(f"{BASE_URL}/products")
    response.raise_for_status()  # Raise an error for bad responses
    products = response.json()
    products_df = pd.DataFrame(products)

    return products_df

def extract_users():
    """
    Extracts user data from the Fake Store API.
    """
    response = requests.get(f"{BASE_URL}/users")
    response.raise_for_status()  # Raise an error for bad responses
    users = response.json()
    users_df = pd.DataFrame(users)

    return users_df



    