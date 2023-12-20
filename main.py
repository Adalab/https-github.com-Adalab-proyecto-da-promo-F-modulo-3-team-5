#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from src import soporte_creacion_BBDD as query
from src import BBDD_soporte as bbdd
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
df["job_satisfaction_ab"]= df["jobsatisfaction"].apply(sp.categorizar_grupos)
df["environment_satisfaction_ab"]=df["environmentsatisfaction"].apply(sp.categorizar_grupos)
df["relationship_satisfaction_ab"]=df["relationshipsatisfaction"].apply(sp.categorizar_grupos)
df["job_involvement_ab"]=df["jobinvolvement"].apply(sp.categorizar_grupos)
df["work_lifebalance_ab"]=df["worklifebalance"].apply(sp.categorizar_grupos)


# %%
''' Definimos las hipótesis para el A/B testing:

Hipotesis nula[HO]
No hay cambios significativos entre los dos grupos

Hupotesis alternanova [H1]
Hay cambios significativos entre lso dos grupos'''
#%%

job_satisfaction=sp.creo_df_AB(df,'job_satisfaction_ab')
enviroment_satisfaction=sp.creo_df_AB(df,'environment_satisfaction_ab')
relationship_satisfaction=sp.creo_df_AB(df,'relationship_satisfaction_ab')
job_involvement=sp.creo_df_AB(df,'job_involvement_ab')
work_lifebalance=sp.creo_df_AB(df,'work_lifebalance_ab')

variables_ab=[job_satisfaction,enviroment_satisfaction,relationship_satisfaction,job_involvement,work_lifebalance]
columnas_ab=['job_satisfaction',
       'environment_satisfaction', 'relationship_satisfaction',
       'job_involvement', 'work_lifebalance']
# %%

for i,k in zip(variables_ab,columnas_ab):
    sp.normalidad(i,'Rotacion_si',k) 
#%%

for i,k in zip(variables_ab,columnas_ab):
    sp.homogeneidad(i,'Grupo','Rotacion_si',k) 

# %%
columnas_ab=['job_satisfaction',
       'environment_satisfaction', 'relationship_satisfaction',
       'job_involvement', 'work_lifebalance']
for i,k in zip(variables_ab,columnas_ab):
    sp.ab_testing(i,k)

# %%
columnas_num=['percentsalaryhike','trainingtimeslastyear','yearssincelastpromotion']

#%%
for i in columnas_num:
    
       sp.normalidad(df,i,i)
       
# %%
fig, axes = plt.subplots(nrows =1, ncols = 3, figsize =(20,5), gridspec_kw={'wspace': 0.5})
sns.histplot(x='percentsalaryhike', data=df,ax=axes[0])
sns.histplot(x='trainingtimeslastyear', data=df,ax=axes[1])
sns.histplot(x='yearssincelastpromotion', data=df,ax=axes[2])

# %%
for i in columnas_num:
       sp.test_man_whitney(df,i,'yes','no','attrition')
# %%
#Barplot de las columnas numéricas agrupadas por attrition
fig, axes = plt.subplots(nrows =1, ncols = 3, figsize =(20,5), gridspec_kw={'wspace': 0.5})
axes = axes.flat
for ind, col in enumerate(columnas_num):
    sns.barplot(x = "attrition", y = col, hue= "attrition", data = df, ax = axes[ind],palette = "mako")
    axes[ind].set_ylabel(col)
    axes[ind].tick_params(axis='x', labelsize=12)
    axes[ind].tick_params(axis='y', labelsize=12)
    axes[ind].set_xlabel('attrition', fontsize=14)
    axes[ind].set_ylabel(col, fontsize=14)     
    axes[ind].spines['right'].set_visible(False)
    axes[ind].spines['top'].set_visible(False)


# %%
columnas_cat=['education','gender','remotework','joblevel', 'jobrole','distancefromhome']
colores = sns.color_palette('mako_r', n_colors=7) 
#Barplot de las variables categóricas agrupadas por attrition
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(20, 20), gridspec_kw={'hspace': 0.5})
axes = axes.flat
for ind, col in enumerate(columnas_cat):
    ax = axes[ind]
    sns.countplot(x=col, data=df, palette='mako', hue ='attrition',  ax=ax)
    if ind < 4:
        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha='center', fontsize=12)
    else:
        ax.set_xticks(ax.get_xticks())
        axes[ind].set_xticklabels(axes[ind].get_xticklabels(), rotation=75, ha='center', fontsize=12)
    ax.set_title(f'Conteo de {col}', y=1.02, fontsize=20)
    ax.set_xlabel('')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

plt.show()
# %%
columnas_conti=['education','joblevel','jobrole','gender','remotework']
for col in columnas_conti:
    sp.independencia(df,col)
# %%
df_distance=df[df['distancefromhome']!='unknown']
sp.independencia(df_distance,'distancefromhome')
# %%
df_job=df[['attrition','joblevel','jobrole']]
#%%
df_job['grouplevel']=df_job['joblevel'].apply(sp.categorizar_grupos_level)
# %%
df_job['grouprole']=df_job['jobrole'].apply(sp.categorizar_grupos_role)
# %%

sp.transformacion_datos(df_job,'attrition',{'yes':1,'no':0})

# %%
sp.test_man_whitney(df_job,'attrition','level A','level B','grouplevel')
# %%
sp.test_man_whitney(df_job,'attrition','role A','role B','grouprole')

# %%
bbdd.creacion_BBDD_tablas(query.query_creacion_bbdd,'AlumnaAdalab')
#%%
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_rotacion,'AlumnaAdalab','base_datos_empleados_ETL')
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_datos_personales,'AlumnaAdalab','base_datos_empleados_ETL')
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_datos_contrato,'AlumnaAdalab','base_datos_empleados_ETL')
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_datos_salario,'AlumnaAdalab','base_datos_empleados_ETL')
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_empleado_encuesta,'AlumnaAdalab','base_datos_empleados_ETL')
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_datos_encuesta_empleado,'AlumnaAdalab','base_datos_empleados_ETL')
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_datos_encuesta_manager,'AlumnaAdalab','base_datos_empleados_ETL')
# %%
lis_num=[]
for i in range (1,1581):
    lis_num.append(i)
lis_num_2=[]
for i in range (1580,3161):
    lis_num_2.append(i)
#%%
datos_tabla_rotacion=list(tuple(zip(lis_num,df['employeenumber'].values,df['attrition'].values)))
datos_tabla_datos_personales=list(tuple(zip(lis_num,df['yearbirth'].values,df['age'].values,df['distancefromhome'].values,df['gender'].values,df['education'].values,
                                          df['educationfield'].values,df['numcompaniesworked'].values,df['totalworkingyears'].values,df['maritalstatus'].values,
                                          df['yearswithcurrmanager'].values,df['yearssincelastpromotion'].values,df['yearsatcompany'].values)))
datos_tabla_datos_contrato=list(tuple(zip(lis_num,df['department'].values,df['businesstravel'].values,df['joblevel'].values,df['jobrole'].values,df['stockoptionlevel'].values,
                                          df['trainingtimeslastyear'].values,df['remotework'].values)))
datos_tabla_datos_salario=list(tuple(zip(lis_num,df['overtime'].values,df['monthlyincome'].values,df['monthlyrate'].values,df['percentsalaryhike'].values,df['hourlyrate'].values)))

datos_tabla_encuesta_empleado=list(tuple(zip(lis_num,lis_num,lis_num_2)))

datos_tabla_datos_encuestas_empleado=list(tuple(zip(lis_num,df['environmentsatisfaction'].values,
                                                    df['jobsatisfaction'].values,df['relationshipsatisfaction'].values,
                                                    df['worklifebalance'].values,df['jobinvolvement'].values)))

datos_tabla_datos_encuestas_manager=list(tuple(zip(lis_num_2,df['performancerating'].values)))

#%%
datos_tabla_datos_personales=bbdd.convertir_floats(datos_tabla_datos_personales)
datos_tabla_datos_contrato=bbdd.convertir_floats(datos_tabla_datos_contrato)
datos_tabla_datos_salario=bbdd.convertir_floats(datos_tabla_datos_salario)
datos_tabla_datos_encuestas_empleado=bbdd.convertir_floats(datos_tabla_datos_encuestas_empleado)
datos_tabla_datos_encuestas_manager=bbdd.convertir_floats(datos_tabla_datos_encuestas_manager)
#%%
bbdd.insertar_datos(query.query_insertar_rotacion,'AlumnaAdalab','base_datos_empleados_ETL',datos_tabla_rotacion)
bbdd.insertar_datos(query.query_insertar_datos_personales,'AlumnaAdalab','base_datos_empleados_ETL',datos_tabla_datos_personales)
bbdd.insertar_datos(query.query_insertar_datos_contrato,'AlumnaAdalab','base_datos_empleados_ETL',datos_tabla_datos_contrato)
bbdd.insertar_datos(query.query_insertar_datos_salario,'AlumnaAdalab','base_datos_empleados_ETL',datos_tabla_datos_salario)
bbdd.insertar_datos(query.query_insertar_empleado_encuesta,'AlumnaAdalab','base_datos_empleados_ETL',datos_tabla_encuesta_empleado)
bbdd.insertar_datos(query.query_insertar_datos_encuesta_empleado,'AlumnaAdalab','base_datos_empleados_ETL',datos_tabla_datos_encuestas_empleado)
bbdd.insertar_datos(query.query_insertar_datos_encuesta_manager,'AlumnaAdalab','base_datos_empleados_ETL',datos_tabla_datos_encuestas_manager)
#%%