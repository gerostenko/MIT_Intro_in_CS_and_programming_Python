# Approximate square root using exhaustive enumeration
x = float(input("Enter a number: "))
epsilon = 0.01
step = epsilon ** 2
num_guesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans**2 <= x:
    ans += step
    num_guesses += 1
print(f"number of guesses = {num_guesses}")
if abs(ans**2 - x) >= epsilon:
    print(f"Failed on square root of {x}")
else:
    print(f"{ans} is close to square root of {x}")
    
    
# Approximate square root using bisection/binary search

x = float(input("Enter a number: "))
epsilon = 0.01
num_guesses = 0
low = 0 
high = max(1, x) 
ans = (high + low) / 2 

while abs(ans**2 - x) >= epsilon:
    print(f"low = {low}, high = {high}, ans = {ans}")
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2

print(f"number of guesses = {num_guesses}")
print(f"{ans} is to square root of {x}")

# Approximate square root using binary search covering negative numbers

x = float(input("Enter a number: "))
x_absolute = abs(x)
epsilon = 0.01
num_guesses = 0
low = 0 
high = max(1, x_absolute) 
ans = (high + low) / 2 

while abs(ans**2 - x_absolute) >= epsilon:
    print(f"low = {low}, high = {high}, ans = {ans}")
    num_guesses += 1
    if ans**2 < x_absolute:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
    
if x < 0:
    ans *= -1

print(f"number of guesses = {num_guesses}")
print(f"{ans} is to square root of {x}")


# OR

x = float(input("Enter a number: "))
epsilon = 0.01
num_guesses = 0
low = min(0, x)
high = max(1, x) 
ans = (high + low) / 2
x_sign = 1 if x > 0 else -1

while abs((ans**2) * x_sign - x) >= epsilon:
    print(f"low = {low}, high = {high}, ans = {ans}")
    num_guesses += 1
   
    if (ans**2)*x_sign < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2

print(f"number of guesses = {num_guesses}")
print(f"{ans} is to square root of {x}")