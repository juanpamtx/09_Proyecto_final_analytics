from utils.io_utils import load_csv, save_csv
from utils.cleaning_utils import (
    remove_duplicates,
    standardize_column_names,
    fill_missing,
    clean_string_columns,
)
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH

FILES = ["products.csv", "transactions.csv", "customers.csv", "behavior.csv"]

for file in FILES:
    df = load_csv(RAW_DATA_PATH + file)
    df = standardize_column_names(df)
    df = remove_duplicates(df)
    df = fill_missing(df)
    df = clean_string_columns(df)

    save_csv(df, PROCESSED_DATA_PATH + file.replace(".csv", "_clean.csv"))
