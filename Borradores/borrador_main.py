#%%
from src import soporte_creacion_BBDD as query
from src import BBDD_soporte as bbdd
import pandas as pd
# %%
bbdd.creacion_BBDD_tablas(query.query_creacion_bbdd,'AlumnaAdalab')
# %%
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_rotacion,'AlumnaAdalab','base_datos_empleados_ETL')
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_datos_personales,'AlumnaAdalab','base_datos_empleados_ETL')
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_datos_contrato,'AlumnaAdalab','base_datos_empleados_ETL')
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_datos_salario,'AlumnaAdalab','base_datos_empleados_ETL')
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_empleado_encuesta,'AlumnaAdalab','base_datos_empleados_ETL')
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_datos_encuesta_empleado,'AlumnaAdalab','base_datos_empleados_ETL')
bbdd.creacion_BBDD_tablas(query.query_creacion_tabla_datos_encuesta_manager,'AlumnaAdalab','base_datos_empleados_ETL')

# %%
df=pd.read_csv('hr_limpio.csv',index_col=0)
# %%
lis_num=[]
for i in range (1,1511):
    lis_num.append(i)
lis_num_2=[]
for i in range (1511,3021):
    lis_num_2.append(i)
# %%
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

#%%
bbdd.insertar_datos(query.query_insertar_rotacion,'AlumnaAdalab','base_datos_empleados_ETL',datos_tabla_rotacion)
bbdd.insertar_datos(query.query_insertar_datos_personales,'AlumnaAdalab','base_datos_empleados_ETL',datos_tabla_datos_personales)
bbdd.insertar_datos(query.query_insertar_datos_contrato,'AlumnaAdalab','base_datos_empleados_ETL',datos_tabla_datos_contrato)
bbdd.insertar_datos(query.query_insertar_datos_salario,'AlumnaAdalab','base_datos_empleados_ETL',datos_tabla_datos_salario)
bbdd.insertar_datos(query.query_insertar_empleado_encuesta,'AlumnaAdalab','base_datos_empleados_ETL',datos_tabla_encuesta_empleado)
bbdd.insertar_datos(query.query_insertar_datos_encuesta_empleado,'AlumnaAdalab','base_datos_empleados_ETL',datos_tabla_datos_encuestas_empleado)
bbdd.insertar_datos(query.query_insertar_datos_encuesta_manager,'AlumnaAdalab','base_datos_empleados_ETL',datos_tabla_datos_encuestas_manager)
#%%



# %%

