#In this program, we use a while loop to keep asking the user for input until they enter valid numbers and units. 
# We use the float() function to convert the input value to a float number. 
# We then use an if statement to perform the corresponding conversion based on the user's input. 
# If the user enters an invalid unit or conversion, we print an error message and continue the loop. 
# If the user enters valid input, we print the result and exit the loop.

def unitConverter():
    print('Welcome to the unit converter...')
    while True:
        try:
            value = float(input('Enter value to be converted: '))
            from_unit = input('Enter the value\'s unit measurement: ').lower()
            to_unit = input('Enter the unit measurement to convert to(m, ft, kg, lb): ').lower()
            if from_unit == 'm'and to_unit == 'ft':
                result = value * 3.281
                print(f'{value} meters is {result} feet')
            elif from_unit == 'ft' and to_unit == 'm':
                result = value / 3.281
                print(f'{value} feet is {result} meters')
            elif from_unit == 'kg' and to_unit == 'lb':
                result = value * 2.205
                print(f'{value} kilograms is {result} pounds')
            elif from_unit == 'lb' and to_unit == 'kg':
                result = value / 2.205
                print(f'{value} pounds is {result} kilograms')
            else:
                print('Invalid units or conversion')
                continue #if there is an error, the continue statement takes back the user 
            #to the start of the loop to enter valid info but if no error, the else block will be skipped and the loop
            #will break
            break
        except ValueError:
            print("Invalid input, please enter a number.")
unitConverter()
