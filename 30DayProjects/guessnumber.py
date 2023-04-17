#Build a "Guess the Number" game where the computer generates a random number and the user has to guess it.
#EXPLANATION
# 1.We first import the module random, to generate a random number between 0 and 10 using the randint() function
# 2. We initilize a number_of_guesses to 0
# 3. We use a 'WHILE' loop to keep asking the user to guess a number until they guess correctly
# 4. In each iteration, we ask the user to input a number, increment the number of guesses, 
# and compare their guess to the secret number
# 5.  If the guess is correct, we print a congratulatory message and exit the loop. 
# 6. If the guess is too low or too high, we print a message telling the user to try again.

import random

def guess_number():
    secret_number = random.randint(1, 10) #generate a number between 1 and 10
    num_guesses = 0 #initialize number of guesses to 0

    while True:
        guess = int(input('Guess a number between 1 and 10: '))
        num_guesses += 1 #increment the number of guesses by 1

        if guess == secret_number:
            print(f'Congratulations, you have guessed the correct number on {num_guesses} guesses.')
            break
        elif guess > secret_number:
            print('Too high. Try again')
        else:
            print('Too low. Try again')
guess_number()

