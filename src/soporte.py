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
import sys
import sys

from dotenv import load_dotenv
load_dotenv()
sys.path.append("../")
# %%

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
def limpieza_datos (dataframe):
    #Homogeneizamos el nombre de las columnas 
    nuevas_columnas = {columna: columna.lower() for columna in df_ejemplo.columns}
    dataframe.rename(columns=nuevas_columnas, inplace= True)

    dataframe.rename(columns = {"datebirth": "yearbirth"}, inplace = True )
    dataframe.drop(['roledepartament','numberchildren','over18', 'sameasmonthlyincome','employeecount','salary','standardhours', 'yearsincurrentrole'],axis = 1, inplace=True)
    
    # 
    columnas_limpiar = ['dailyrate','employeenumber','monthlyincome','performancerating','totalworkingyears','worklifebalance','distancefromhome']
    for columna in columnas_limpiar:
        try:
            df_ejemplo[columna] =(df_ejemplo[columna].str.replace('$', ''))
        
        except:
            pass
        
        try:
            df_ejemplo[columna] =(df_ejemplo[columna].str.replace(',', '.')) 

        except:
            pass
            
        try:
          df_ejemplo[columna]=pd.to_numeric(df_ejemplo[columna]).astype(float)
        except:
          pass
    
    return dataframe
    