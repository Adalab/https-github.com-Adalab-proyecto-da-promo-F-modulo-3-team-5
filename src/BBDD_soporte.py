import mysql.connector


def creacion_BBDD_tablas (query,contraseña,nombre_BBDD=None):

    if nombre_BBDD is not None:
        cnx=mysql.connector.connect(
            user="root",
            password=contraseña,
            host='127.0.0.1')
        
        mycursor=cnx.cursor()

        try:
            mycursor.execute(query)
            print(mycursor)
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

    else:
        cnx=mysql.connector.connect(
            user="root",
            password=contraseña,
            host='127.0.0.1',
            database=nombre_BBDD)
        
        mycursor=cnx.cursor()

        try:
            mycursor.execute(query)
            print(mycursor)
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

def insertar_datos (query, contraseña, nombre_BBDD, lista_tuplas):
    cnx=mysql.connector.connect(
            user="root",
            password=contraseña,
            host='127.0.0.1',
            database=nombre_BBDD)

    mycursor=cnx.cursor()
    try:
        mycursor.executemany(query, lista_tuplas)
        cnx.commit()
        print(mycursor.rowcount, 'registros insertados')
        cnx.close()
        
    except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)


def convertir_floats(lista_tuplas):
    datos_tabla_ventas_def=[]
    for tupla in lista_tuplas:
        lista_intermedia=[]
        for elemento in tupla:
            try:
                lista_intermedia.append(float(elemento))
            except:
                lista_intermedia.append(elemento)
        
        datos_tabla_ventas_def.append(tuple(lista_intermedia))
    return datos_tabla_ventas_def

'''def convertir_int(lista_tuplas):
    datos_tabla_ventas_def=[]
    for tupla in lista_tuplas:
        lista_intermedia=[]
        for elemento in tupla:
            try:
                lista_intermedia.append(int(elemento))
            except:
                lista_intermedia.append(elemento)
        
        datos_tabla_ventas_def.append(tuple(lista_intermedia))
    return datos_tabla_ventas_def'''