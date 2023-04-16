#Challenge 1: Print "Hello, World!" to the console
print("Hello World. I'm listening to 'Ghost' by Justin Beiber!")

#Challenge 2: Print your name to the console
print("My name is Marianna Komen and i aspire to be a good programmer/data scientist")

#Create a variable and assign it a value
name = "Anna"
age = 26
weight = 48.9
occupation = 'CSR-IT'
hobbies = ['coding', 'watching shows', 'cocktails at sundown']

#Use arithmetic operators (+, -, *, /) on variables
result = (26-9)*7/3+9

#Create a list of numbers and print each element
num_list = [8, 5, 9, 2, 6, 0, 3]
for num in num_list:
    print(num)

#Use the len() function to find the length of a list
print("The length of the list is, ", len(num_list))

#Create a function that takes two arguments and returns their sum
def find_sum(x,y):
    result = x + y
    print("The sum of the two numbers is: ", result)
find_sum(6, 16)

def check_if_greater_than(x):
    if x > 10:
        print (f'{x} is greater than 10')
    else:
        print (f'{x} is less than 10')
check_if_greater_than(15)    

#Use a for loop to print the first 10 even numbers
for n in range(0,20):
    if n % 2 == 0:
        print(n)

#Use a while loop to print numbers from 1 to 10
num = 1
while num < 10:
    print(num)
    num +=1

#Create a dictionary and print each key-value pair
current_listens = {'shawn mendes': 'Treat you better', 'Ed Sheeran': 'Photograph', 'Fifth Harmony': 'He like that'}
print(current_listens)
print(current_listens["Fifth Harmony"])
print(current_listens.keys())
print(current_listens.values())

#Use the range() function to create a list of numbers from 1 to 10
list_of_numbers = list(range(0,10))
print(list_of_numbers)

#Use the input() function to get user input and print it
user_input = input("What makes you happy?")
print(user_input)

#Create a function that takes a list as an argument and returns the sum of all the elements
def sum_of_elements(li):
    sum = 0
    for el in li:
        sum = sum + el
    print("The total sum of the elements: " ,sum)
sum_of_elements([3, 4, 5])

#Use a list comprehension to create a list of even numbers from 1 to 20
even_numbers = list(range(0, 20, 2))
print(even_numbers)

#Use the random module to generate a random number between 1 and 10
import random
random_number = random.randint(1,10)
print("The random number is: ", random_number)

#Use a try-except block to handle an exception
temp = 0
try:
    normal_temp = 27 / temp
    print("The normal temperature should be: ", normal_temp)
except ZeroDivisionError:
    print("Zero Division Error")

#Use the time module to measure the execution time of a function
#The Python time module provides various time-related functions, 
#such as getting the current time and suspending the calling thread’s execution for the given number of seconds. 
import time

#Store the start time
#get the start time before executing the first line of the program
start_time = time.time()

#write the main program
sum_of_nums = 0
for i in range(1000):
    sum_of_nums += 1
# wait for 3 seconds
time.sleep(3)
print('Sum of first 1000 numbers is:', sum_of_nums)

#store the end time of execution
end_time = time.time()

#execution time
execution_time = end_time - start_time
print("The execution time of the program is ", execution_time, "seconds")

#Use the string methods to manipulate a string (e.g., upper(), lower(), replace())
my_name = "Marianna Komen"
print(my_name.upper())
print(my_name.lower())
print(my_name.replace('Marianna', 'Ashly'))

#Use the datetime module to get the current date and time
#import the datetime class from using datetime import datetime module
from datetime import datetime

#use the now() of the datetime class
#The datetime.now() returns the current local date and time. 
# By default, it represents datetime in YYYY-mm-dd hh:mm:ss.microseconds format.
now = datetime.now()
print("Current day and time is ",now)

#to print only current day
current_date = now.date()
print("Today is ",current_date)

#to print only current time 
current_time = now.time()
print("Today is ",current_time)

#Create a class and instantiate an object
class Tenants:
    #attributes of the object
    def __init__(self, name, house_no):
        self.name = name
        self.house_no = house_no
        self.rent_paid = True
    #methods of the object
    def is_rent_paid(self):
        if not self.rent_paid:
            print("The tenant has not paid the rent. Send reminder message")
        else:
            print("The tenant has already paid the rent")
tenant1 = Tenants("Anna", "B16")
tenant1.is_rent_paid()
print(f'{tenant1.name} of {tenant1.house_no} rent status is: {tenant1.is_rent_paid()}')