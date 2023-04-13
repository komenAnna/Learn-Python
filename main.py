#Define a class before we can create objects
class Student:
    #a method inside the class that can be accessed by the objects
    #whenever we define methods for a class, we need to use self as the firs argument, which represents the object calling the method
    def check_pass_fail(self):
        if self.marks>=40:
            return True
        else:
            return False
    #pass
#"pass" is a null operation — when it is executed, nothing happens. It is useful as a placeholder when a statement is required syntactically,
#but no code needs to be executed

# the __init__() is a special method that automatically gets created when a python object is created
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

student1 = Student("Anna", 65)
student2 = Student("Kay", 35)
did_pass = student1.check_pass_fail()
print(did_pass)
did_pass = student2.check_pass_fail()
print(did_pass)
#To create objects from the class and add own attributes
#student1 = Student()
#student1.name = "Anna"
#student1.marks = 65
#student2 = Student()
#student2.name = "Kay"
#student2.marks = 35

#attributes and methods are added inside the class so that all objects created from the class, can access them
#did_pass = student1.check_pass_fail()
#did_pass = student2.check_pass_fail()
#print(did_pass)

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real, imag)
        return result

n1 = Complex(5, 2)
n2 = Complex(-2, 6)
result = n1.add(n2)
print("real = ", result.real)
print("imag = ", result.imag)