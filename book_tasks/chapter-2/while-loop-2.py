# Write a program that asks the user to input 10integers, and then prints the largest 
# odd number that was entered. If no odd number was entered, it should print a message to that effect. 

NUM_OF_INPUTS = 10; 
iterator = 0; 
result = "No odd number given" 

while (iterator < NUM_OF_INPUTS): 
    num = int(input("Input a number: ")) 
    iterator = iterator + 1 
    if num%2 != 0: 
        if type(result) == str or num > result: 
            result = num         
print(result) 