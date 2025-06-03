funcs = []

for i in range(5):
    funcs.append(lambda i=i:print(i)) #con esto logramos agregar e imprimir al mismo tiempo

for k in funcs:
    k()