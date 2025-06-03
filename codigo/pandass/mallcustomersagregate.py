import pandas as pd

#df = pd.read_csv('mall_customers.csv') #si corrio bien

df = pd.read_csv('mall_customers.csv', index_col=0) #con esto elimina la primera columna del documento, con lo q customer_id queda como la columna primaria ahora
df.columns=["Gender","Age","Income","Spending"] #sobrescribe el nombre de las columnas q venia en el documento en el dataframe

print(df)
print("medias")
print(df.loc[:, "Age":"Spending"].mean()) #medias para cada columna
print(df["Age"].mean()) #media para una sola columna

gp= df.groupby("Gender")
print("media para cada gender agrupado")
print(gp.mean())
print("media de edad para mujeres")
mynumber= gp.mean().loc["Female","Age"]
print(mynumber)
formatted_number=f"{mynumber:.2f}"
print(formatted_number)


