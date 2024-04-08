#%%
import pandas as pd
import numpy as np
import re
from src import soporte_funciones as sf

# DF con el que vamos a trabajar
df = pd.read_csv('csv-archivos/HR RAW DATA.csv', index_col=0)

# limpieza y homogeneización del DF
sf.limpieza(df)
display(df.head())
#%%
# guardar DF en repo
df.to_csv('csv-archivos/etl_data.csv')

#%%
# creación de la bbdd y carga de los datos
from src import soporte_bbdd as bbdd
from src import soporte_query as query
%%
bbdd.creacion_bbdd(query.query_schema, 'AlumnaAdalab')
bbdd.creacion_bbdd(query.employees, 'AlumnaAdalab', 'abc_company')
bbdd.creacion_bbdd(query.employee_details,'AlumnaAdalab', 'abc_company')
bbdd.creacion_bbdd(query.economic, 'AlumnaAdalab', 'abc_company')
bbdd.creacion_bbdd(query.satisfaction, 'AlumnaAdalab', 'abc_company')
# %%

# AB TESTING
from scipy.stats import chi2_contingency

df_test = sf.df_testeo(df)
tabla_contingencia = pd.crosstab(df_test['attrition'], df_test['grupo_testeo'])
sf.chi2_contingency_test(tabla_contingencia)

