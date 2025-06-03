import pandas as pd #matplotlib se puede usar igual sin pandas
import matplotlib.pyplot as plt


df = pd.read_csv('mall_customers.csv', index_col=0) #con esto elimina la primera columna del documento, con lo q customer_id queda como la columna primaria ahora
df.columns=["Gender","Age","Income","Spending"] #sobrescribe el nombre de las columnas q venia en el documento en el dataframe
print(df)

#GRAFICAR DOS COLUMNAS DEL DATAFRAME (EN ESTE CASO AGE VS SPENDING)
plt.figure(figsize=(16,9))
plt.grid(True) #activa la malla para poder visualizar
plt.title("Age vs Spending")
plt.xlabel("Age")
plt.ylabel("Spending")

plt.scatter(df["Age"].values,df["Spending"].values, color="green")  #tipo de grafico, en este grafico caso de  puntos
plt.show()
plt.close()
