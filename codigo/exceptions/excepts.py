try:
    d = {} #set vacio
    d['Hello']
    print(1/0)

except ZeroDivisionError as zde:
    print("Failed.", zde)
except Exception as e:
    print("Caught exception", type(e))
else: #el else corre solo cuando no hay ningun error. Es para no dejar mensajes en el try.
    print("Ningun error ocurrio")
finally: #el finally corre siempre.
    print("Finally!")

