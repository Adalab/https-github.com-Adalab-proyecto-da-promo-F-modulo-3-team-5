#%%
import pandas as pd
import os

import sys
from src import soporte as sp
# %%
# %%
df= sp.abrir_archivo('../HR RAW DATA.csv')
# %%
eda = sp.exploracion_dataframe(df)
# %%
