import pandas as pd
from pathlib import Path

def load_csv(path: str) -> pd.DataFrame:
    """Carga un CSV desde un path y devuelve un DataFrame."""
    return pd.read_csv(path)

def save_csv(df: pd.DataFrame, path: str) -> None:
    """Guarda un DataFrame como CSV."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
