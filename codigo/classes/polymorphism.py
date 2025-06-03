#de W3SCHOOLS y chatgpt

"""
Polymorphism is a fundamental concept in Object-Oriented Programming (OOP) that allows objects to be treated as instances 
of their parent class, enabling method overriding and dynamic behavior. Both Python and Java support polymorphism, but they 
implement it differently.
"""

#En intellij tengo In java, why Animal myDog = new Dog(); and not Dog myDog = new Dog(); ?

class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

my_dog = Dog()  
my_dog.make_sound()  # Output: "Dog barks"

"""
Feature	            Python	                                                      Java
Method Overloading	❌ Not natively supported (handled via default arguments)	✅ Supported (multiple methods with same name but different parameters)
Method Overriding	✅ Supported (dynamic method resolution)	                    ✅ Supported (requires @Override annotation)
Dynamic Typing	✅ Allows duck typing (methods work as long as they exist)	    ❌ Strict type checking (methods must match declared types)
Interfaces	❌ No explicit interfaces (uses abstract base classes)	            ✅ Uses interfaces for polymorphism
Operator Overloading	✅ Supported (e.g., __add__, __mul__)	                ❌ Not supported
"""

"Duck typing is a dynamic type system used in Python, where an object's suitability for a task is determined by its behavior rather than its explicit type. The name comes from the saying: If it walks like a duck and quacks like a duck, then it must be a duck. Done at runtime"
"Strict type checking refers to the way Java enforces data types at compile time, ensuring that variables, parameters, and return values match the expected types before the code runs. This prevents accidental type mismatches and enhances code reliability."







