# Print the integer cube root, if it exists, of an integer provided via input
# Solution is from the book and is present for learning purposes

number = int(input("Enter an ineteger: "))
ans = 0

while(ans**3 < abs(number)): 
    ans += 1;
    
if ans**3 != abs(number):
    print(f"{number} is not a perfect cube")
else:
    if number < 0:
        ans = -ans
    print(f"Cube root of {number} is {ans}")

    