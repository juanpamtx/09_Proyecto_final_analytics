from utils.io_utils import load_csv, save_csv
from utils.transform_utils import merge_datasets
from config import PROCESSED_DATA_PATH, FINAL_DATA_PATH

transactions = load_csv(PROCESSED_DATA_PATH + "transactions_clean.csv")
customers = load_csv(PROCESSED_DATA_PATH + "customers_clean.csv")
products = load_csv(PROCESSED_DATA_PATH + "products_clean.csv")
behavior = load_csv(PROCESSED_DATA_PATH + "behavior_clean.csv")

final_df = merge_datasets(transactions, customers, products, behavior)
save_csv(final_df, FINAL_DATA_PATH + "ecommerce_master_dataset.csv")
