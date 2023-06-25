

# Static method:

If we don’t want to use class variables or instance variables, we can use static methods. A static method can be called without the object of the class. We use the decorator @staticmethod to declare a static method. This method requires neither the self nor the cls reference because they are not dependent on any instance or class attribute.

```python
class Sample:
  
  @staticmethod
  def method():
    print('This is a static method')

Sample.method()
```

## Class Method
The class methods are bound to a class instead of the objects of the class. These methods can be called without the instance of the class. We can create class methods by either using the classmethod() method or the decorator @classmethod. Class methods accept cls as an argument indicating that the method points to the class instead of the object instance.

```python
class Sample:
  var = "Class Variable"
 
  @classmethod
  def method(cls):
    print(cls.var)
 
Sample.method()
```
## Instance method
With the instance method, we can access all the attributes of a class. We [pass](https://www.pythonpool.com/python-pass/) the self keyword as an argument to the instance method. With the self keyword, we can access the attributes.

In python, every method created inside a class is by default considered as an [instance](https://docs.python.org/3/reference/datamodel.html) method unless specified explicitly. There is no need for a decorator for this method. With the instance method, we can access the data for each instance of the class.

```python
class Sample:
  def __init__(self, a):
        self.a = a
 
  def method(self):
    print(self.a)
 
obj = Sample(10)
obj.method()
```
# What is self in class?

The self keyword is used to pass into the instance methods inside a class. 
We use the self keyword to represent the instance for a class. 
*Self represents the current instance of the class*. Let us consider an example to understand the functionality of the self keyword.

````python
class Person:
  def __init__(self, name, age):
        self.name = name
        self.age = age
 
  def details(self):
        print(f"Person's name is {self.name} and age is {self.age}")
 
obj1 = Person('Liam',21)
obj2 = Person('Henry', 25)
 
obj1.details()
obj2.details()
````

# What is cls in class?
Using the cls keyword, we represent that the method belongs to the class. We pass cls as an argument to the class methods. With cls, we attach the class method to the class.

*The class methods can be called without having an instance of a class. Using cls, we pass the class as a reference.*

# Summarize:
```text
cls refers to the class, whereas self refers to the instance. Using the cls keyword, we can only access the members of the class, whereas using the self keyword, we can access both the instance variables and the class attributes.
```