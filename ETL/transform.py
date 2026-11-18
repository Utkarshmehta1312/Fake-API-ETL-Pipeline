import pandas as pd

def transform_products(products_df):

    df = products_df.copy()
    """
    Transforms the product data by renaming columns and converting data types.
    """
    # Rename columns for clarity
    df = df.rename(columns={
        'id': 'product_id',
        'title': 'product_name',
        'price': 'product_price',
        'description': 'product_description',
        'category': 'product_category'
    })

    df = df[['product_id', 'product_name', 'product_price', 'product_description', 'product_category']]

    # Convert price to float
    df['product_price'] = df['product_price'].astype(float)

    return df

def transform_users(users_df):
    df = users_df.copy()

    df['firstname'] = df['name'].apply(lambda x: x['firstname'])
    df['lastname'] = df['name'].apply(lambda x: x['lastname'])

    df['street'] = df['address'].apply(lambda x: x['street'])
    df['city'] = df['address'].apply(lambda x: x['city'])
    df['zipcode'] = df['address'].apply(lambda x: x['zipcode'])

    """
    Transforms the user data by renaming columns and converting data types.
    """
    # Rename columns for clarity
    df = df.rename(columns={
        'id': 'user_id',
        'email': 'user_email',
        'username': 'username',
    })

    df = df[['user_id', 'user_email', 'username', 
             'firstname', 'lastname', 
              'street','city',
              'zipcode']]

    return df