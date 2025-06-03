import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.cluster import KMeans

df = pd.read_csv('mall_customers.csv', index_col=0) #con esto elimina la primera columna del documento, con lo q customer_id queda como la columna primaria ahora
df.columns=["Gender","Age","Income","Spending"] #sobrescribe el nombre de las columnas q venia en el documento en el dataframe

model = KMeans(n_clusters=2) #especificamos el numero de clusters que queremos igual a 2 en el modelo estadistico K means

X = df[["Age", "Spending"]]
model.fit(X) #agrupamos en dos clusters (que es un modelo estadistico) el gasto de las personas por edad. 

df["Cluster"] = model.labels_

sn.scatterplot(df, x="Age", y="Spending", palette="husl", hue="Cluster")  #En el grafico se aprecia que el cluster de gente joven gasta mas, lo que no significa que todos los jovenes van en este cluster
plt.show()
plt.close()