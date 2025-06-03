class Word:

    def __init__(self,text):#funcion predeterminada __init__
        self._text = text

    def __str__(self): #funcion predeterminada __str__
        return self._text
    
    def __add__(self,other): #funcion predeterminada __add__
        return Word(self._text + other._text)
    
    
w1  = Word("Hello ") 
w2  = Word("there")

w = w1 + w2 #aca esta llamando a la funcion __add__
print(w)