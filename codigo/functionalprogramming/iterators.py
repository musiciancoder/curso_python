#Your Python snippet behaves more like a Fail-Safe Iterator in Java

class PowersOfTwo:
    def __iter__(self):
        self._value = 1
        return self

    def __next__(self):
        self._value *=2 # _ es que es private

        if self._value > 20:
            raise StopIteration

        return self._value


for i in PowersOfTwo():
    print(i)
    
