import pandas as pd

df = pd.read_csv('myfile.csv', sep =',',  index_col=0)

df.columns =  df.columns.str.strip()

df.at['Tue','Pushups'] = 40 # 'Tue' con esto referenciamos la fila con el indice y 'Pushups'=40 cambiamos el valor

print(df) 

print()

print("Mondat squats", df.iat[0,2]) # obtenemos un valor del dataframe, en este caso el valor de la fila 0,  columna 2 

print(df) 

