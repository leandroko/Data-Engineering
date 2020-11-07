# Bibliotecas usadas no projeto
import glob
import pyodbc
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine

# Conexão com o Banco de Dados
server = 'localhost'
database = 'LIUDB'
sqleng = create_engine('mssql+pyodbc://localhost/LIUDB?driver=SQL Server?Trusted_Connection=yes')

# get data file names
path =r'C:\Users\Liu\Desktop\Dash'
filenames = glob.glob(path + "\BaseP*.csv")


dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename, sep=';'))

# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, ignore_index=True)

big_frame.to_sql(name='BASEPRODUCAO', con=sqleng, schema='LEANDRO', if_exists='append' , index=False)
