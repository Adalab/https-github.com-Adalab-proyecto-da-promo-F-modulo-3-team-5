#%%
import pandas as pd
import numpy as np
import os
#import sys
#sys.path.append("../")
from src import soporte as sp
#os.getcwd() 
# %%
df= sp.abrir_archivo('HR RAW DATA.csv')
# %%
eda = sp.exploracion_dataframe(df)
# %%
columnas_eliminar = ['roledepartament','numberchildren','over18', 'sameasmonthlyincome','employeecount','salary','standardhours', 'yearsincurrentrole']
#%%
df = sp.limpieza_columnas(df, df.columns.to_list(),columnas_eliminar )
# %%
columnas_limpiar = ['dailyrate','employeenumber','monthlyincome','performancerating','totalworkingyears','worklifebalance','distancefromhome']
#info gral a minusculas
columnas_minusculas=['age', 'attrition', 'businesstravel', 'department','education', 'educationfield','environmentsatisfaction', 'gender', 'hourlyrate', 'jobinvolvement',
       'joblevel', 'jobrole', 'jobsatisfaction', 'maritalstatus', 'monthlyrate', 'numcompaniesworked', 'overtime',
       'percentsalaryhike', 'relationshipsatisfaction','stockoptionlevel', 'trainingtimeslastyear', 'worklifebalance',
       'yearsatcompany', 'yearssincelastpromotion','yearswithcurrmanager', 'yearbirth', 'remotework', 'dailyrate','totalworkingyears']
# %%
sp.limpieza_datos(df, columnas_limpiar, columnas_minusculas)
# %%
df['age'] = df['age'].apply(sp.convertir_a_numero)
# %%
df['gender'] = df['gender'].replace({0: 'male', 1: 'female'})
df['gender'].value_counts()
#%%
df['maritalstatus']=df['maritalstatus'].replace({'marreid':'married'})
#%%
df['remotework']= df['remotework'].replace({('1'):'yes',('0') or ('false'): 'no', 'true': 'yes', 'false': 'no'})
df['remotework'].value_counts()
#%%
df["distancefromhome"] = df["distancefromhome"].apply(lambda x: np.nan if x < 0 else x)

#%%
sp.eliminar_duplicados(df, 'employeenumber')

#%%
categorias_educacion = {1: 'high school', 2: 'college', 3: 'university', 4:'master degree', 5: 'phd'}
categorias_joblevel = {1: 'entry', 2: 'intermediate', 3: 'experienced', 4: 'advanced', 5: 'expert'}

sp.transformacion_datos(df, 'education', categorias_educacion)
sp.transformacion_datos(df, 'joblevel', categorias_joblevel)

#%%
df['hourlyrate'] = df['hourlyrate'].replace( 'not available', 'unknown')
#%%
df["dailyrate"] = df["dailyrate"].apply(lambda x: np.nan if x == 'nan' else float(x))
# %%
columnas_desconocidas = ['businesstravel', 'department', 'educationfield', 'maritalstatus', 'overtime']
sp.nulos_cat(df, columnas_desconocidas)

#%%
sp.visualizacion_num_nulos(df)

#%%
sp.gestion_nulos_num(df)
# %%
