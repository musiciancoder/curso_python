import pandas as pd
import  numpy as np


#crear dataframe a partir de un dictionary
data = { 
    "Mon":[1,2,3],
    "Tue":[0.1,0.2,0.3],
    "Wed":[5,6,7],
}

df= pd.DataFrame(data)

print(df) 

print("multiplicando por 3.0")
df *=3.0
print(df) 

dx = pd.DataFrame(data, index=["Coffe","Tea", "Water"])
print(dx)
print()

print("obtener seno")
df = np.sin(df)
print(df) 

df.loc["Coffe":"Tea"] -= 100
print(df)

