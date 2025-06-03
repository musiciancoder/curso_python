import pandas as pd

df = pd.read_csv('myfile.csv', sep =',',  index_col=0)
df.columns = ['Pullups ','Pushups ','Squats '] 

print(df)

print()

print(df.columns) 

print("con strip") ##elimina espacios vacios

df.columns =  df.columns.str.strip()

print(df.columns) 