import pandas as pd

#pandas tiene built-in functions al igual q numpy


df= pd.DataFrame(
    [[1,2,3],[4,5,6],[7,8,9]],
    columns = ['Dog','Cats','Mice'],
    index=['Meat','Fish','Vegetables'],
)

print(df)
print()
print("suma")
print(df.sum()) #sumas para cada columna
print(type(df.sum())) #sum() es una built-in function de panda

