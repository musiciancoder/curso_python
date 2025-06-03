import pandas as pd

df= pd.DataFrame(
    [[1,2,3],[4,5,6],[7,8,9]],
    columns = ['Dog','Cats','Mice'],
    index=['Meat','Fish','Vegetables'],
)

print(df)
print('Estos son los cats:')
cats = df['Cats'] #estraer la columna Cats
print(cats) 
print('Estos son los cats index:') #estraer los indices
print(cats.index)
print('Este es el tipo de cats index:')
print(type(cats.index)) 
print('Este es el cats index como lista:')
print(list(cats.index)) 
print('Este es el tipo de cats index como lista:')
print(type(list(cats.index)))
print('Este es el tipo de cats.values:')
print(type(cats.values))
print('Este son los cats.values:')
print((cats.values)) #usa numpy behind the scenes, como se puede apreciar aca
print('Este son los cats.values como lista:')
print(list(cats.values))

