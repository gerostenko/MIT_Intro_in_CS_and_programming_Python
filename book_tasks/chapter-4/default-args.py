# Write a function mult that accepts either one or two ints as 
# arguments. If called with two arguments, the function prints 
# the product of the two arguments. If called with one argument,
# it prints that argument.

def mult(num1, num2 = None):
    if num2 == None:
        print(f"Printing just one argument {num1}")
    else:
        print(f"Printing the product of {num1} and {num2}: {num1*num2}")

mult(10)
mult(10, 3)