# Input a number which
# 1 < pwr < 6
# root**pwr == number
# Example: input = 25; root = 5, pwr = 2
# Example input 27, root = 3, pwr = 3
number = int(input("Enter a number: "))
pwr = None
root = None

for i in range(2, 6):
    root = 2;
    
    while(root**i < number):
        root += 1
    if root ** i == number:
        pwr = i
        break
    
if root == None or pwr == None:
    print("Provided number has no found root and power")
else:
    print(f"Given number has root = {root} with power = {pwr}")