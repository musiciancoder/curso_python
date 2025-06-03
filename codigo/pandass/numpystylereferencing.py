import pandas as pd

df = pd.read_csv('myfile.csv', sep =',',  index_col=0)

df.columns =  df.columns.str.strip()

print(df) 

print() 

print("con numpy") 

print(df.loc["Mon":"Wed"])

print("con step de 2") 

print(df.loc["Mon":"Wed":2])

print() 

print(df.loc[["Fri","Mon"],  "Pushups":"Squats"])


print() 
print(df.loc[:,"Pushups":"Squats"]) 

print("con iloc solo se ocupan indices")

print(df.iloc[:1:3])