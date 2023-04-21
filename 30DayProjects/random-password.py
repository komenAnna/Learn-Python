# Build a program that can generate and print a random password.
#In this program, we first import the random and string modules.
import random
import string

# We then define a function called generate_password() 
# that takes an optional parameter length with a default value of 8.
def generate_password(length=8):
    # We create a string of all possible characters for the password 
    # using the ascii_letters, digits, and punctuation constants from the string module.
    characters = string.ascii_letters + string.digits + string.punctuation
    # we then use a for loop and the random.choice() function to randomly select 
    # length number of characters from the string and concatenate them into a password string.
    password = ''.join(random.choice(characters) for i in range(length))
    #return password
    print(f'Your random password is {password}')
generate_password()

#
# ascii_letters constant in the string module contains all the English letters from a to z. 
# These letters are in lowercase and uppercase as a single string.