import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sn

#Para agrupar por comportamiento de gastos

df = pd.read_csv('mall_customers.csv', index_col=0) #con esto elimina la primera columna del documento, con lo q customer_id queda como la columna primaria ahora
df.columns=["Gender","Age","Income","Spending"] #sobrescribe el nombre de las columnas q venia en el documento en el dataframe

df["SpendingGroup"] = pd.cut(df["Spending"], bins=3, labels=(0, 1, 2)) # Se crea una tercera columna SpendingGroup

print(df)