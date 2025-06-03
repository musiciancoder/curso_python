#pandas es para trabajar con spreadsheets (llamados dataframes en python) en pyton

import pandas as pd

df = pd.read_csv('myfile.csv')  ## soy un comentario y NO estoy siendo impreso
print(df)

print()

print(df.columns)

print()

print(df.head)

print() 

df = pd.read_csv('myfile.csv', sep ='\s*,\s*',  index_col=0)  ## soy un comentario y estoy siendo impreso
# sep es separator, en este caso espacios vacios antes y despues (podria haber sido coma otro separador). index_col=0 indica q el index es 0 (notar q al hacer print ahora el dataframe  se desplaza hacia la derecha)
print(df)




