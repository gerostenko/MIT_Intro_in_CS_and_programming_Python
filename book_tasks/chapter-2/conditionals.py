# Write a program that examines three variables—x, y, and z—and prints the largest odd number 
# among them. If noneof them are odd, it should print the smallest value of the three. 
# Solution: 

x = 1
y = 5 
z = 3

largestOddNumberOrSmallestNumber = min(x, y, z) 
if x%2 != 0: 
    largestOddNumberOrSmallestNumber = x 
if y%2 != 0 and y > largestOddNumberOrSmallestNumber: 
    largestOddNumberOrSmallestNumber = y 
if z%2 != 0 and z > largestOddNumberOrSmallestNumber: 
    largestOddNumberOrSmallestNumber = z 
print(largestOddNumberOrSmallestNumber) 
