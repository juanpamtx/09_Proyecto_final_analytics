import pandas as pd


def eda_preliminar(df):

    """ Realiza un análisis exploratorio preliminar sobre un DataFrame dado.

    Este análisis incluye:
    - Muestra aleatoria de 5 filas del DataFrame.
    - Información general del DataFrame.
    - Porcentaje de valores nulos por columna.
    - Conteo de filas duplicadas
    - Distribución de valores para columnas categóricas.
    - Distribución de valores para columnas numéricas.

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.

    Returns:
    None

    """
    
    display(df.sample(5))

    print('-' * 15)

    print('DIMENSIONES')

    print(f'Nuestro conjunto de datos presenta un total de {df.shape[0]} filas y {df.shape[1]} columnas')

    print('-' * 15)
    
    print('INFO')

    display(df.info())

    print('-' * 15)
    
    print('NULOS')

    display(df.isnull().mean()*100)

    print('-' * 15)
    
    print('DUPLICADOS')

    print(f'Tenemos un total de {df.duplicated().sum()} duplicados')

    print('-' * 15)

    print('FRECUENCIAS CATEGÓRICAS')
     
    for col in df.select_dtypes(include= 'object').columns:
        print(col.upper())
        print(df[col].value_counts())
        print('----------')

    print('-' * 15)

    print('ESTADISTICOS NUMÉRICOS')
    
    display(df.describe().T)
