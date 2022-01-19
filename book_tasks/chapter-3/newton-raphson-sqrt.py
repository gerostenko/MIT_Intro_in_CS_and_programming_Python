# Newton-raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0
k = int(input("Enter number: "))
epsilon = 0.01
num_guesses = 0
guess = k/2
while abs(guess**2 - k) >= epsilon:
    guess = guess - ((guess**2 - k)/(2*guess))
    
print(f"it took {num_guesses} guesses")
print(f"Square root of {k} is about {guess}")
