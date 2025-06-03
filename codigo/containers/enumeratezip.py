fruits = {"apple","pear","orange"}
days = {"Mon","Tue","Wed"}

e=enumerate(fruits)
print(type(e))

for i, fruit in e:
    print(i,fruit)

z=zip(fruits,days)
print(type(z))
for i, day in z:
    myzip=(i,day)
    print(myzip)
    

