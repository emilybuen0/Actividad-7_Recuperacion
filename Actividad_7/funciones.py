#Función_1. Carga los archivos con extensiones .csv y .html y los convierte a dataframe, si es un  archivo con cualquier otra extensión, emitirá el raise (“Hola, acabas de ingresar un documento que desconozco, con extensión: .formato”)
def cargar_dataset (archivo):
    import pandas as pd
    import numpy as np
    import os
    import matplotlib.pyplot as plt

    extension = os.path.splitext(archivo)[1].lower()
    if extension == '.csv':
        df = pd.read_csv (archivo)
        return (df)
    elif extension == '.html':
         df = pd.read_html (archivo)
         return (df)
    else : 
        raise ValueError (f"Hola, acabas de ingresar un documento que desconozco, con extensión: .{extension}")


#Función_2. Sustituye los valores nulos de las variables
def limpieza_nulos(df):
    df_copy = df.copy()

#Las columnas que no sean de tipo numérico se sustituirán con el string “Valor Nulo”
    cualitativas = df_copy.select_dtypes(include=['object', 'datetime', 'category'])
    df_copy[cualitativas.columns] = cualitativas.fillna("Valor_Nulo")

#valores nulos de las variables de las columnas primas con la constante numérica  “1111111"
    columnas_primas = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71}
    columnas_primas = cuantitativas.loc[:, indice[indice.isin(columnas_primas)].index]

#Demás columnas numéricas con la constante “1000001”
    cuantitativas = df_copy.select_dtypes(include=['float64', 'int64','float','int'])
    indice = df.columns.to_series().apply(df.columns.get_loc)
    otras_columnas = cuantitativas.loc[:, indice[~indice.isin(columnas_primas)].index]
    
    df_copy[columnas_primas.columns] = columnas_primas.fillna(1111111)
    df_copy[otras_columnas.columns] = otras_columnas.fillna(1000001)
    
    return df_copy

#Función_3. Identifica los valores nulos “por columna” y “por dataframe”
def cuenta_nulos(df):
    nulos_columna = df.isnull().sum()
    nulos_dataframe = df.isnull().sum().sum()
    
    return("Valores nulos por columna", nulos_columna,
            "Valores nulos por dataframe", nulos_dataframe)


#Función_4. Identifica  los valores atípicos de las columnas numéricas con el método de “Rango intercuartílico” y los sustituye con la leyenda “Valor Atípico”
def limpieza_atipicos(df):
    import pandas as pd
    import numpy as np

    cuantitativas = df.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    cualitativas = df.select_dtypes(exclude=['float64', 'int64', 'float', 'int'])

    Q1 = cuantitativas.quantile(0.25)  # Primer cuartil
    Q3 = cuantitativas.quantile(0.75)  # Tercer cuartil
    IQR = Q3 - Q1  # Rango intercuartílico

    # Límites para detectar valores atípicos
    Limite_Superior = Q3 + 1.5 * IQR
    Limite_Inferior = Q1 - 1.5 * IQR

    # Reemplazo de valores atípicos con la leyenda "Valor Atípico"
    data_iqr = cuantitativas.mask((cuantitativas < Limite_Inferior) | (cuantitativas > Limite_Superior), "Valor Atípico")

    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_limpios = pd.concat([cualitativas, data_iqr], axis=1)

    return Datos_limpios
