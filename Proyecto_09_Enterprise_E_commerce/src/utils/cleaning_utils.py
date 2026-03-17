import pandas as pd


# =========================================================
#  FUNCIONES AUXILIARES (GENÉRICAS Y REUTILIZABLES)
# =========================================================

def crear_copia(df: pd.DataFrame, nombre: str) -> pd.DataFrame:
    """
    Crea y devuelve una copia del dataframe original para evitar modificarlo directamente.
    """
    print(f"→ Creando copia del dataframe: {nombre}")
    return df.copy()


def convertir_minusculas(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """Convierte a minúsculas todo el contenido de una columna."""
    df[columna] = df[columna].astype(str).str.lower()
    return df


def reemplazar_espacios(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """Sustituye los espacios por guiones bajos en una columna de texto."""
    df[columna] = df[columna].astype(str).str.replace(" ", "_")
    return df


def convertir_a_fecha(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """Convierte una columna al tipo datetime sin romper el flujo."""
    df[columna] = pd.to_datetime(df[columna], errors="coerce")
    return df


def convertir_porcentaje(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """
    Convierte valores decimales (0.25) en porcentajes (25.0).
    Si el valor ya es mayor que 1 no se transforma.
    """
    df[columna] = df[columna].astype(float)
    df[columna] = df[columna].apply(lambda x: x * 100 if x <= 1 else x)
    return df


def convertir_a_booleano(df: pd.DataFrame, columna: str, valores_verdaderos=None) -> pd.DataFrame:
    """
    Crea DOS nuevas columnas:
    - {columna}_binaria → True/False
    - {columna}_yes_no → "Yes"/"No"

    La columna original NO SE MODIFICA.
    """
    if valores_verdaderos is None:
        valores_verdaderos = ["1", "true", "yes", "sí"]

    comparador = df[columna].astype(str).str.lower()
    col_bool = columna + "_binaria"
    col_yn = columna + "_yes_no"

    # Crear nueva columna booleana
    df[col_bool] = comparador.isin(valores_verdaderos)

    # Crear nueva columna "Yes"/"No"
    df[col_yn] = df[col_bool].map({True: "Yes", False: "No"})

    return df


# =========================================================
#  FUNCIONES ESPECÍFICAS DE LIMPIEZA POR DATASET
# =========================================================

# -------- BEHAVIOR --------
def limpiar_behavior(df: pd.DataFrame) -> pd.DataFrame:
    df = crear_copia(df, "behavior")

    df = convertir_minusculas(df, "customer_id")

    df = convertir_a_booleano(df, "behavior_churn_signal", valores_verdaderos=["1", "true"])

    df = convertir_porcentaje(df, "cart_abandon_rate")
    df = convertir_porcentaje(df, "return_rate")

    return df


# -------- CUSTOMERS --------
def limpiar_customers(df: pd.DataFrame) -> pd.DataFrame:
    df = crear_copia(df, "customers")

    df = convertir_minusculas(df, "customer_id")
    df = convertir_minusculas(df, "gender")
    df = convertir_minusculas(df, "country")

    df = convertir_a_fecha(df, "registration_date")

    df = convertir_a_booleano(df, "churn_label", valores_verdaderos=["1", "true"])

    return df


# -------- PRODUCTS --------
def limpiar_products(df: pd.DataFrame) -> pd.DataFrame:
    df = crear_copia(df, "products")

    df = convertir_minusculas(df, "product_id")
    df = convertir_minusculas(df, "category")
    df = reemplazar_espacios(df, "category")

    return df


# -------- TRANSACTIONS --------
def limpiar_transactions(df: pd.DataFrame) -> pd.DataFrame:
    df = crear_copia(df, "transactions")

    df = convertir_minusculas(df, "transaction_id")
    df = convertir_minusculas(df, "customer_id")
    df = convertir_minusculas(df, "product_id")

    df = convertir_a_fecha(df, "order_date")

    df = convertir_minusculas(df, "payment_method")
    df = reemplazar_espacios(df, "payment_method")

    df = convertir_minusculas(df, "device_type")
    df = reemplazar_espacios(df, "device_type")

    df = convertir_porcentaje(df, "discount_applied")

    df = convertir_a_booleano(df, "fraud_label", valores_verdaderos=["1", "true"])

    return df