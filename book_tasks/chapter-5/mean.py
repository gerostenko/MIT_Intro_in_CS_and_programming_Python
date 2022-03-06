# Finger exercise: Write an expression that evaluates to the mean of a tuple of numbers. 
# Use the function sum.

mean = lambda tuple: sum(tuple)/len(tuple) 

print(mean((1, 2, 3, 4)))