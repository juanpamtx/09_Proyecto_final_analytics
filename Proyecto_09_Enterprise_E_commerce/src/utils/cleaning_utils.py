import pandas as pd

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()

def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df

def fill_missing(df: pd.DataFrame, strategy: str = "median") -> pd.DataFrame:
    numeric_cols = df.select_dtypes(include="number").columns

    if strategy == "median":
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    elif strategy == "mean":
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    return df

def clean_string_columns(df: pd.DataFrame) -> pd.DataFrame:
    str_cols = df.select_dtypes(include="object").columns
    df[str_cols] = df[str_cols].fillna("Unknown")
    return df
