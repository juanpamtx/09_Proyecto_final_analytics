import pandas as pd

def merge_datasets(transactions, customers, products, behavior):
    """Une las 4 tablas en un único dataset final."""
    df = transactions.merge(products, on="product_id", how="left")
    df = df.merge(customers, on="customer_id", how="left")
    df = df.merge(behavior, on=["customer_id", "product_id"], how="left")
    return df
