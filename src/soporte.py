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

import scipy.stats as stats
from scipy.stats import chisquare, kstest,chi2_contingency,ttest_ind

#import os
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
#os.getcwd()  
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

    dataframe = dataframe.drop(indices_a_sacar, inplace=True)

    return dataframe

#%%
def transformacion_datos (dataframe, columna, diccionario):
    dataframe[columna]= dataframe[columna].replace(diccionario)

    return dataframe
#%%
def nulos_cat (dataframe,columnas_desconocidas): 

    df_nulos = pd.DataFrame((dataframe.isnull().sum() / dataframe.shape[0]) * 100, columns = ["%_nulos"])
    df_nulos= df_nulos[df_nulos["%_nulos"] > 0]
     #clomnas categoricas
    nulos_esta_cat = dataframe[dataframe.columns[dataframe.isnull().any()]].select_dtypes(include = "O").columns
    print("Las columnas categóricas que tienen nulos son : \n ")
    print(nulos_esta_cat)
    
    for col in nulos_esta_cat:
        print(f"La distribución de las categorías para la columna {col.upper()}")
        display(dataframe[col].value_counts() / dataframe.shape[0])
        print("..........")

    # iteramos por la lista de columnas a las que le vamos a cambiar los nulos por "Uknown"
   
    for columna in columnas_desconocidas:
        
        # reemplazamos los nulos por el valor Unknown para cada una de las columnas de la lista
        dataframe[columna] = dataframe[columna].fillna("Unknown")
        
    # comprobamos si quedan nulos en las columnas categóricas. 
    print("Después del reemplazo usando 'fillna' quedan los siguientes nulos")
    dataframe[columnas_desconocidas].isnull().sum()

    display(dataframe.describe(include='O').T)

    
            
    return df_nulos
#%%
def visualizacion_num_nulos (dataframe):
    colores = sns.color_palette('mako_r', n_colors=3)
    nulos_esta_num = dataframe[dataframe.columns[dataframe.isnull().any()]].select_dtypes(include = np.number).columns
    print("Las columnas numéricas que tienen nulos son : \n ")
    print(nulos_esta_num)
    
    dataframe[nulos_esta_num].isnull().sum() / dataframe.shape[0]

    fig, axes = plt.subplots(nrows = 3, ncols = 3, figsize = (20,10)) 

    axes = axes.flat

    for indice, col in enumerate(nulos_esta_num):
        sns.boxplot(x = col, data = dataframe, ax = axes[indice],color=colores[0])
        
    plt.tight_layout()
    fig.delaxes(axes[-1]);

    return display(dataframe.describe(exclude='O').T)

#%%
def gestion_nulos_num (dataframe):
    imputer_iterative = IterativeImputer(max_iter = 20, random_state = 42)

    # ajustamos y tranformamos los datos
    imputer_iterative_imputado = imputer_iterative.fit_transform(dataframe[["dailyrate","totalworkingyears"]])

    # comprobamos que es lo que nos devuelve, que en este caso es un array también
    imputer_iterative_imputado

    dataframe[["dailyrate_iterative","totalworkingyears_iterative"]] = imputer_iterative_imputado

    # instanciamos la clase del KNNImputer
    imputer_knn = KNNImputer(n_neighbors = 5)

    # ajustamos y transformamos los datos
    imputer_knn_imputado = imputer_knn.fit_transform(dataframe[["dailyrate","totalworkingyears"]])

    # comprobamos que es lo que nos devuelve, que sigue siendo un array
    imputer_knn_imputado

    # por último nos queda añadir ese array al DataFrame como hemos hecho hasta ahora
    dataframe[["dailyrate_knn","totalworkingyears_knn"]] = imputer_knn_imputado

    # comprobamos los nulos
    print(f'Después del KNN tenemos: \n{dataframe[["dailyrate_knn","totalworkingyears_knn"]].isnull().sum()} nulos')

    dataframe.describe()[["dailyrate","dailyrate_iterative", "dailyrate_knn", "totalworkingyears", "totalworkingyears_iterative", "totalworkingyears_knn"]]

    #eliminamos las columnas que ya no nos interesan para guardar el DataFrame 
    dataframe.drop(["dailyrate", "totalworkingyears", "dailyrate_knn", "totalworkingyears_iterative" ], axis = 1, inplace = True)

    # ahora vamos a cambiar el nombre de las columnas que quedaron para que tengan el mismo nombre de origen
    nuevo_nombre = {"dailyrate_iterative": "dailyrate", "totalworkingyears_knn": "totalworkingyears"}
    dataframe.rename(columns = nuevo_nombre, inplace = True)

    median_worklifebalance = dataframe["worklifebalance"].median()
    print(f"La media de la columna 'worklifebalance' es: {round(median_worklifebalance, 2)}")

    # aplicamos el método 'fillna()' a la columna
    dataframe["worklifebalance"] = dataframe["worklifebalance"].fillna(median_worklifebalance)

    # comprobamos los nulos para la columna
    print(f"Después del 'fillna' tenemos {dataframe['worklifebalance'].isnull().sum()} nulos")
    
    # aplicamos el método 'fillna()' a la columna
    lista_columnas=["performancerating","monthlyincome", "employeenumber","distancefromhome"]

    dataframe[lista_columnas] = dataframe[lista_columnas].fillna("unknown")

    # comprobamos los nulos para la columna
    print(f"Después del 'fillna' tenemos {dataframe[lista_columnas].isnull().sum()} nulos")

    display(dataframe.isnull().sum())

def categorizar_grupos(numero):
    if numero >= 3:
        return "grupo A"
    else:
        return "grupo B"
    
   

def creo_df_AB(df, columnas):
    df_grupoA = df[df[columnas]== "grupo A"]
    
    df_grupoB = df[df[columnas]== "grupo B"]
     
    # Crear un DataFrame
    data_p_test = {
    'Grupo': ["Empleados Satisfechos", "Empleados Insatisfechos"],
    'Rotacion_si': [df_grupoA[df_grupoA["attrition"]== "yes"].shape[0]/df_grupoA.shape[0],df_grupoB[df_grupoB["attrition"]== "yes"].shape[0]/df_grupoB.shape[0]],
    'Rotacion_no': [df_grupoA[df_grupoA["attrition"]== "no"].shape[0]/df_grupoA.shape[0],df_grupoB[df_grupoB["attrition"]== "no"].shape[0]/df_grupoB.shape[0]]}

    df_p_test = pd.DataFrame(data_p_test)
    return df_p_test

def normalidad(dataframe, columna,col_2):
    statistic, p_value = stats.kstest(dataframe[columna],'norm')
    if p_value > 0.05:
        print(f"Para la columna {columna} los datos de {col_2} siguen una distribución normal.")
    else:
        print(f"Para la columna {columna} los datos de {col_2} no siguen una distribución normal.")

def homogeneidad(dataframe, columna, columna_metrica,col_2):
    valores_evaluar = []
    
    for valor in dataframe[columna].unique():
        valores_evaluar.append(dataframe[dataframe[columna]== valor][columna_metrica])

    statistic, p_value = stats.levene(*valores_evaluar)
    if p_value > 0.05:
        print(f"Para la métrica {columna_metrica} las varianzas de {col_2} son homogéneas entre grupos.")
    else:
        print(f"Para la métrica {columna_metrica}, las varianzas de {col_2}  no son homogéneas entre grupos.")

def ab_testing(df, columna):  
    # hacemos un análisis visual previo
    fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 5))

    sns.barplot(x="Grupo", y="Rotacion_si", data=df,  palette = "mako_r",ax = axes[0])
    sns.barplot(x="Grupo", y="Rotacion_no", data=df,  palette = "mako_r", ax = axes[1])

    axes[0].set_title(columna)
    axes[1].set_title(columna)
        
    # Crear una tabla de contingencia
    contingency_table = pd.crosstab(df['Grupo'], df['Rotacion_si'])

# Realizar la prueba de proporciones
    chi2, p_value, _, _ = chi2_contingency(contingency_table)

# Imprimir el resultado de la prueba
    alpha = 0.05
    if p_value < alpha:
        print(f"Hay una diferencia significativa entre {columna} y la rotación")
        print("""
            Los resultados sugieren que existe evidencia estadística para afirmar que los datos guardan relación. 
            """)
        print("\n ---------- \n")
    else:
        print(f"No hay una diferencia significativa entre {columna} y la rotación.")
        print("""Los resultados sugieren que no existe evidencia estadística para afirmar que los datos guardan relación""")
        print("\n ---------- \n")  

def test_man_whitney(dataframe,metrica, grupo_A, grupo_B, columna_grupos):
    grupoA = dataframe[dataframe[columna_grupos] == grupo_A]
    grupoB = dataframe[dataframe[columna_grupos] == grupo_B]
    
    metrica_grupoA = grupoA[metrica]
    metrica_grupoB = grupoB[metrica]
    
    u_statistic, p_value = stats.mannwhitneyu(metrica_grupoA, metrica_grupoB)
    
    if p_value < 0.05:
        print(f"Las medianas entre {metrica} y el tiempo de permanencia en la empresa son diferentes. Lo que significa que hay diferencias significativas en los datos")
    else:
        print(f"Las medianas entre {metrica} y el tiempo de permanencia en la empresa son iguales. Lo que significa que no hay diferencias significativas en los datos")

def independencia (df,columna):
    tabla_contingencia = pd.crosstab(df[columna], df['attrition'])
    chi2, p_value, _, _ = chi2_contingency(tabla_contingencia)
    print(p_value)

    # Imprimir el resultado de la prueba
    alpha = 0.05
    if p_value < alpha:
        print(f"Hay una diferencia significativa entre {columna} y la rotación")
        print("""
            Los resultados sugieren que existe evidencia estadística para afirmar que los datos guardan relación. 
            """)
        print("\n ---------- \n")
    else:
        print(f"No hay una diferencia significativa entre {columna} y la rotación.")
        print("""Los resultados sugieren que no existe evidencia estadística para afirmar que los datos guardan relación""")
        print("\n ---------- \n") 

def categorizar_grupos_level(joblevel):
    if joblevel == 'intermediate' or joblevel == 'entry':
        return "level B"
    else:
        return "level A" 

def categorizar_grupos_role(jobrole):
    if jobrole == ' laboratory technician ' or jobrole == ' research scientist ' or jobrole==' human resources ' or jobrole==' sales representative ' or jobrole==' healthcare representative ':
        return "role B"
    else:
        return "role A"         