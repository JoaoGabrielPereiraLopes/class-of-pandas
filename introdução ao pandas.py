import pandas as pd
import numpy as np

alunos={'Nome':["ricardo",'pedro','roberto','carlos'], 
        'nota':[4,7,5.5,9],
        'aprovado':['não','sim','não','sim']}

dataframe=pd.DataFrame(alunos)
objeto1=pd.Series(dataframe)

array1=np.array([1,2,3])
array2=np.array([[1,2,3],
                [1,2,3],
                [1,2,3]])
print(array1)
print(array2)
for c in array2:
    y=''
    for x in c:
        if x != np.max(c):
            y+=str(x)+','
        else:
            y+=str(x)
    print(y)
print(pd.DataFrame(array2))