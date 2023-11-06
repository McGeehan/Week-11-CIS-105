class Student(Person):
    def __init__(self, name, age, gender, course):
        super().__init__(name, age, gender)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}.")



'''
In this example, we've defined a new class Student that inherits from the Person class. The Student class has an additional attribute course, which represents the course that the student is studying.

The __init__ method in the Student class takes five parameters: self, name, age, gender, and course. The self parameter refers to the object itself, and the other four parameters are used to initialize the corresponding attributes of the object.

Inside the __init__ method, we call the __init__ method of the base class (Person) using the super() function. This allows us to initialize the attributes of the base class without having to repeat the code. We then initialize the course attribute with the value of the course parameter.

The study method is a regular method that prints a message to the console. The method takes one parameter, self, which refers to the object that the method is called on. Inside the method, we use an f-string to format the message with the name and course attributes of the object.

To create an object of the Student class and call its methods, you can use the following code:

python

student = Student("Bob", 20, "male", "Computer Science")
student.greet()
student.study()

This will create a Student object with the name "Bob", the age 20, the gender "male", and the course "Computer Science", and then call its greet and study methods. The greet method is inherited from the Person class, and the study method is defined in the Student class.




'''
