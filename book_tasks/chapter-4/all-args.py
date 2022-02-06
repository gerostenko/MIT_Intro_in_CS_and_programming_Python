import functools

def mean(*numbers):    
    # Assumes at least one argument and all arguments arenumbers    
    # Returns the mean of the arguments    
    tot = functools.reduce(lambda num1, num2: num1+num2, numbers)  
    return tot/len(numbers)

print(mean(1, 2, 3, 4, 5))