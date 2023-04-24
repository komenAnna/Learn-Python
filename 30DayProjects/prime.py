# a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 
# (e.g. 2, 3, 5, 7, 11).

# we define a function called is_prime() that takes a number n as input and 
# returns True if it is prime and False otherwise. 
def is_prime(n):
    # check if n is less than or equal to 1, which is not prime. 
    if n <= 1:
        return print(False)
    # a for loop to check if n is divisible by any number from 2 to the square root of n.
    for i in range(2, int(n**0.5) + 1):
        # If it is divisible by any number in that range, it is not prime and we return False. 
        # Otherwise, we return True.
        if n % i == 0:
            return print(False)
    return print(True)

# define a function called generate_primes() that takes a number n as input 
# and generates a list of prime numbers up to n. 
def generate_primes(n):
    # We use a for loop to iterate over each number from 2 to n, and if it is prime 
    # (according to the is_prime() function), we append it to the primes list.
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return print(primes)

# we prompt the user to enter a number n and generate the list of primes up to n 
# using the generate_primes() function. 
# We then print out the list of primes using the print() function.
n = int(input("Enter a number to generate primes up to: "))
primes = generate_primes(n)
print(f"The primes up to {n} are:", primes)
