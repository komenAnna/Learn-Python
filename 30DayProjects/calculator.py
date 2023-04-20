# Create a function
# While loop to keep asking the user for input until they enter valid numbers and an operation
# Check operation against +, -, *, /, **
# Display result
# Throw error if invalid

def Calculator():
    print('Welcome to your calculator...')
    while True:
        try:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            operation = input('Enter the operation (+, -, *, /, **): ')

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            elif operation == '**':
                result = num1 ** num2
            else:
                print('Invalid operation')
                continue
            print(f'Result: {result}')
            break
        except ValueError:
            print('Invalid input, please enter a valid number')
Calculator()