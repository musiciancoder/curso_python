import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sn #para ver varios graficos a la vez


df = pd.read_csv('mall_customers.csv', index_col=0) #con esto elimina la primera columna del documento, con lo q customer_id queda como la columna primaria ahora
df.columns=["Gender","Age","Income","Spending"] #sobrescribe el nombre de las columnas q venia en el documento en el dataframe

#sn.pairplot(df)

sn.pairplot(df,  height=2, aspect=1, palette="husl", hue="Gender")

plt.show()
plt.close()