# Readme

En este repositorio se muestra el proyecto grupal del Módulo 3 de Data Analytics de Adalab, compuesto por Silvia, Eli, Anabela y Clara.

🎯 **Objetivo:**

La empresa ABC Corporation, consultora tecnológica especializada en ofrecer soluciones de inteligencia artificial (IA) y aprendizaje automático (machine learning) con sede en California, nos ha contratado para desarrollar un proyecto de análisis de datos y experimentación A/B . La finalidad del análisis es identificar los factores que llevan a un empleado a dejar la empresa, para favorecer que el talento permanezca en la consultora.

Se han llevado a cabo las siguientes fases:


**´Fase 1:´**Exploración y limpieza de datos

**´Fase 2:´** Transformación de los datos

**´Fase 3:´** Diseño e inserción de la base de datos

**´Fase 4:´** A/B Testing

**´Fase 5:´** Creación de una ETL

**´Fase 6:´** Reporte de resultados

__________________________________________________

📚 **Importación de librerías:**
 
1. Manipulación de Datos:
pandas as pd: Biblioteca fundamental para manipulación y análisis de datos en Python. Proporciona estructuras de datos flexibles y eficientes, como DataFrame, para trabajar con conjuntos de datos.
numpy as np: Biblioteca para realizar operaciones numéricas y matriciales eficientes en Python. Complementa pandas y es esencial para realizar cálculos numéricos.

2. Procesamiento de Datos:
word2number: Módulo para convertir palabras numéricas en números. Útil para manejar datos donde las cantidades están expresadas en palabras.

3. Imputación de Datos:
SimpleImputer: De la biblioteca scikit-learn, se utiliza para imputar valores faltantes en un conjunto de datos utilizando estrategias simples como la media, mediana, moda, entre otras.
IterativeImputer: También de scikit-learn, realiza imputación de datos utilizando técnicas iterativas, siendo útil cuando las relaciones entre variables son complejas.
KNNImputer: Otra opción de imputación de scikit-learn que utiliza el método de vecinos más cercanos (K-Nearest Neighbors) para estimar los valores faltantes.

4. Visualización de Datos:
seaborn as sns: Biblioteca de visualización de datos basada en matplotlib, que proporciona una interfaz de alto nivel para crear gráficos atractivos y informativos.
matplotlib.pyplot as plt: Parte de la biblioteca matplotlib, se utiliza para crear gráficos estáticos, diagramas de dispersión y otras visualizaciones.

5. Estadísticas y Pruebas:
scipy.stats as stats: Biblioteca de estadísticas científicas que incluye diversas funciones estadísticas y pruebas hipotéticas.
chisquare, kstest, chi2_contingency, ttest_ind: Funciones específicas de scipy.stats para realizar pruebas estadísticas como la prueba de chi-cuadrado, prueba de Kolmogorov-Smirnov, prueba de contingencia chi-cuadrado y prueba t de Student.

6. Conexión a Base de Datos:
mysql.connector: Conector para MySQL que permite establecer conexiones y realizar operaciones en bases de datos MySQL desde Python.
Estos imports sugieren que el código podría estar relacionado con la manipulación, análisis y visualización de datos, así como con la imputación de datos faltantes y la realización de pruebas estadísticas. Además, se incluye una librería para la conexión a una base de datos MySQL.


__________________________________________________

📂 **Estructura de los archivos del proyecto:**








