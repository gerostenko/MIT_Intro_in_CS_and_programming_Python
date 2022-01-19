# Test if an int > 2 is prime. If not, print smallest divisor
number = int (input("Ennter an integer greater than 2: "))
smallest_divisor = None
for guess in range(2, number):
    if number % guess == 0:
        smallest_divisor = guess
        break
if smallest_divisor != None:
    print(f"Smallest divisor of {number} is {smallest_divisor}")
else:
    print(f"{number} is a prime number")
    
#Task: Change the code above so that it returns the largest rather than
# the smallest divisor. 

number = int (input("Ennter an integer greater than 2: "))
smallest_divisor = None
for guess in range(number-1, 2, -1):
    if number % guess == 0:
        smallest_divisor = guess
        break
if smallest_divisor != None:
    print(f"Smallest divisor of {number} is {smallest_divisor}")
else:
    print(f"{number} is a prime number")