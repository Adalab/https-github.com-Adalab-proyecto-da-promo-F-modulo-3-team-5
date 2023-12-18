#%%
import pandas as pd
import numpy as np
from word2number import w2n

from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
# Librerías de visualización
# -----------------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt

import os
#import sys


#from dotenv import load_dotenv
#load_dotenv()
#sys.path.append("../")
# %%
#funcion para abrir csv
def abrir_archivo(nombre):
    return pd.read_csv(nombre,index_col=0)
# %%
def exploracion_dataframe(dataframe):

    print(f"Los duplicados que tenemos en el conjunto de datos son: {dataframe.duplicated().sum()}")
    print("\n ..................... \n")
    
    
    # generamos un DataFrame para los valores nulos
    print("Los nulos que tenemos en el conjunto de datos son:")
    df_nulos = pd.DataFrame(dataframe.isnull().sum() / dataframe.shape[0] * 100, columns = ["%_nulos"])
    display(df_nulos[df_nulos["%_nulos"] > 0])
    
    print("\n ..................... \n")
    print(f"Los tipos de las columnas son:")
    display(pd.DataFrame(dataframe.dtypes, columns = ["tipo_dato"]))
    
    
    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas categóricas son: ")
    dataframe_categoricas = dataframe.select_dtypes(include = "O")
    
    for col in dataframe_categoricas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valores únicos:")
        display(pd.DataFrame(dataframe[col].value_counts()).head())    
# %%
def limpieza_columnas (dataframe,columnas,columnas_drop):
    #Homogeneizamos el nombre de las columnas 
    nuevas_columnas = {columna: columna.lower() for columna in dataframe.columns}
    dataframe.rename(columns=nuevas_columnas, inplace= True)
    #renombramos una columna
    dataframe.rename(columns = {"datebirth": "yearbirth"}, inplace = True )
    #eliminamos columnas
    dataframe.drop(columnas_drop,axis = 1, inplace=True)
 

    #pasamos a minuscula el nombre de las columnas
    for columna in columnas:
    
        try:
            dataframe[columna]=dataframe[columna].str.lower()
        except:
            pass
    
    return dataframe
    
# %%
def limpieza_datos (dataframe,columnas_limpiar, columnas_minusculas):
    
    for columna in columnas_limpiar:
        try:
            dataframe[columna] =(dataframe[columna].str.replace('$', ''))
        
        except:
            pass
        
        try:
            dataframe[columna] =(dataframe[columna].str.replace(',', '.')) 

        except:
            pass
            
        try:
          dataframe[columna]=pd.to_numeric(dataframe[columna]).astype(float)
        except:
          pass
       
   
    for columna in columnas_minusculas:
    
        try:
            dataframe[columna]=dataframe[columna].str.lower()
        except:
            pass
    
    
    return dataframe
# %%
#Para columna de Age

def convertir_a_numero(valor):
    if isinstance(valor, int): # Verifica si el valor ya es un entero, si lo es no hace nada
        return valor
    elif isinstance(valor, str): # Intenta convertir el valor a número
        try: 
            numero = int(valor)
            return numero
        except ValueError:
            try: # aquí es donde se usa la función w2n en el try pq si la conversion falla entonces se usará
                numero = w2n.word_to_num(valor)
                return numero
            except ValueError:
                print(f"Error: No se pudo convertir '{valor}' a número.")
                return None
    else:
        print(f"Error: Tipo de dato no soportado para el valor '{valor}'.")
        return None

# %%
os.getcwd()  
#%%
#identificamos los números de empleado duplicados
# usamos unique para que muestre los valores únicos
def eliminar_duplicados (dataframe,columna):
    duplicados = dataframe[dataframe.duplicated(subset=[columna], keep=False)][columna].unique()
    len(duplicados)

    lista_duplicados= []

    for numero in duplicados:
        lista_duplicados.append(dataframe[dataframe[columna] == numero])

    #Hay 104 numeros de empleado duplicados más NaN

    # lo visualizamos en un nuevo dataFrame
    df_resultado = pd.concat(lista_duplicados)

    indices_a_sacar = df_resultado.iloc[::2, 0]

    dataframe = dataframe.drop(indices_a_sacar)

    return dataframe

#%%
def transformacion_datos (dataframe, columna, diccionario):
    dataframe[columna]= dataframe[columna].replace(diccionario)

    return dataframe