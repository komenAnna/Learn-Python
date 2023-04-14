#Define a class before we can create objects
class Student:
    #a method inside the class that can be accessed by the objects
    #whenever we define methods for a class, we need to use self as the first argument, which represents the object calling the method
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

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        total_perimeter = self.a + self.b + self.c
        return total_perimeter

triangle1 = Triangle(3, 4, 5)
total_perimeter = triangle1.perimeter()
print("The perimeter of the triangle is, ", total_perimeter)

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def check_details(self):
        if self.age > 18:
            return True
        else:
            return False
person1 = Person("Harry", 25, "male")
person2 = Person("Taylor", 12, "female")
okayed = person1.check_details()
print(f'{person1.name} is {person1.age} and {person1.gender}: {okayed}')
okayed = person2.check_details()
print(f'{person2.name} is {person2.age} and {person2.gender}: {okayed}')

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.engine_running = True

    def start_engine(self):
        if not self.engine_running:
            return print("starting engine.....")
            self.engine_running = True
        else:
            return print("Engine is already running")

my_car = Car("Toyota", "Camry", 1980)
is_running = my_car.start_engine()
print(f'{my_car.make}, {my_car.model}, {my_car.year}')

class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
my_vehicle = Vehicle("Honda", "Accord", "Blue")
print(my_vehicle.make, my_vehicle.model, my_vehicle.color)

class Employees:
    
    def __init__(self, name, age, current_position, salary):
        self.name = name
        self.age = age
        self.current_position = current_position
        self.salary = salary

    def paid (self):
        if self.salary > 30000:
            status = "The employee has not been paid"
            return status
        else:
            status = "The employee has been paid"
            return status
employee1 = Employees("Ana", 26, "CSR", 40000)
employee1_status = employee1.paid()
print(employee1.name)
print(employee1.age)
print(employee1.current_position)
print(employee1.salary)
print(employee1_status)


class Room:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area
studyRoom = Room(42.5, 38.7)
print(f'The total area of the study room is {studyRoom.calculate_area()}')