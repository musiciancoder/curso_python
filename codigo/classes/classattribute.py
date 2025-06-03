class Machine:

    count =0

    def __init__(self):
        Machine.count +=1 #class atribute,  equivalente a static en java

"""
def __init__(self):
        self.count +=1 #asi seria un instance variable en python
"""

Machine()
Machine()
print(Machine.count)