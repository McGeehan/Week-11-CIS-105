class Teacher(Person):
    def greet(self):
        print(f"Hello, my name is {self.name} and I am a {self.gender} teacher.")


'''

In this example, we've defined a new class Teacher that also inherits from the Person class. The Teacher class does not have any new attributes, but it does have a new method greet.

The greet method in the Teacher class is an example of method overriding. It takes one parameter, self, which refers to the object that the method is called on. Inside the method, we use an f-string to format a message with the name and gender attributes of the object.

The greet method in the Teacher class overrides the greet method in the Person class. This means that when you call the greet method on a Teacher object, it will execute the greet method defined in the Teacher class, not the one defined in the Person class.

To create an object of the Teacher class and call its methods, you can use the following code:

python

teacher = Teacher("Alice", 30, "female")
teacher.greet()

This will create a Teacher object with the name "Alice", the age 30, and the gender "female", and then call its greet method, which will print the following message to the console:

css

Hello, my name is Alice and I am a female teacher.

Note that the Teacher class does not have its own __init__ method, so it inherits the __init__ method from the Person class. This means that you can create a Teacher object using the same constructor as a Person object.


'''
