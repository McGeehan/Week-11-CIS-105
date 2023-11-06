class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self._age = age  # protected attribute
        self.gender = gender

    def get_age(self):
        return self._age


'''
In this example, we've made a slight modification to the Person class from the previous example. We've changed the age attribute to _age, which makes it a protected attribute. In Python, an attribute that starts with an underscore (_) is considered protected, which means it should not be accessed directly from outside the class.

We've also added a get_age method that returns the value of the _age attribute. This method provides a way to access the value of the _age attribute from outside the class, without directly exposing the attribute itself.

To create an object of the Person class and call its methods, you can use the following code:

python

person = Person("Alice", 30, "female")
print(person.get_age())

This will create a Person object with the name "Alice", the age 30, and the gender "female", and then call its get_age method, which will print the following message to the console:

30

Note that you should not access the _age attribute directly, as it is considered protected. Instead, you should use the get_age method to get the value of the attribute.

'''
