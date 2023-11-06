class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print(f"Hello, my name is {self.name} and I am a {self.gender} person.")


'''

In this example, we've defined a Person class with three attributes: name, age, and gender. The attributes represent the properties of a person, such as their name, age, and gender.

The __init__ method (also known as a constructor) is a special method that gets called when you create a new object of the class. It takes four parameters: self, name, age, and gender. The self parameter refers to the object itself, and the other three parameters are used to initialize the corresponding attributes of the object.

The greet method is a regular method that prints a greeting message to the console. The method takes one parameter, self, which refers to the object that the method is called on. Inside the method, we use an f-string to format the message with the name and gender attributes of the object.

To create an object of the Person class and call its methods, you can use the following code:

python

person = Person("Alice", 30, "female")
person.greet()

This will create a Person object with the name "Alice", the age 30, and the gender "female", and then call its greet method, which will print the following message to the console:

css

Hello, my name is Alice and I am a female person.


'''
