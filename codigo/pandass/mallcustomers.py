import pandas as pd

#df = pd.read_csv('mall_customers.csv') #si corrio bien

df = pd.read_csv('mall_customers.csv', index_col=0) #con esto elimina la primera columna del documento, con lo q customer_id queda como la columna primaria ahora
df.columns=["Gender","Age","Income","Spending"] #sobrescribe el nombre de las columnas q venia en el documento en el dataframe
print(df)
print("columns")
print(df.columns)
print("head")
print(df.head(6)) #primeras 6 filas