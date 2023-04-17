#Create a program that takes a user's name and birthday as input and calculates their age.
# 1. Import the date class from the datetime module
# 2. Create a function to calculate the age from the user's input of name and birthday
# 3. Split the birthday string to year, month and date using the split() method and map() function
# 4. Calculate the no. of days between today and the birthday using 'DATE()' and subtract them
# 5. Finally, we divide the result by 365 to get the user's age in years and print a message with their name and age.
from datetime import date

def calculate_age():
    name = input('What is your name? ')
    birthday = input('When is your birthday (YYYY-MM-DD): ')
    year, month, day = map(int, birthday.split('-'))
    age = (date.today() - date(year, month, day)).days // 365
    print(f'{name} you are {age} years old')
calculate_age()