import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randint(0, 4, 60).reshape(20,3),
    columns=["One","Two","Three"],
    index=[chr(x) for  x  in range(65,85)]
)
print(df)

print("Sorted")

#ordenar en primera instancia por columna One, en segunda por columna Two y en tercera instancia por columna Three
df1= df.sort_values(by=["One","Two","Three"], ascending=False)
print(df1)

#transpose pasa las q eran filas a columnas y vice versa
print("transpose")
df2=df.transpose()
print(df2)

#ordenar por filas, no por columnas
print("df2 ordenado")
df2= df2.sort_values(by=["One","Two","Three"], axis=1, ascending=False)
print(df2)