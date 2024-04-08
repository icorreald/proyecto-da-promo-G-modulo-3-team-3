#%%
import pandas as pd
import numpy as np
from src import soporte_funciones as sf

#%%
df = pd.read_csv('csv-archivos/HR RAW DATA.csv', index_col=0)

sf.limpieza(df)
display(df.head())
# %%
df.to_csv('csv-archivos/etl_data.csv')
