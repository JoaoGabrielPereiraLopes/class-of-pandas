#importa a biblioteca pandas,numpy e excel
import pandas as pd
import numpy
import math

# Lê o arquivo Excel
arquivo_excel = 'C:/Users/gabri/Desktop/programacao/backending/python/pandas/numeros.xlsx'
dados = pd.read_excel(arquivo_excel)
dados.head()
