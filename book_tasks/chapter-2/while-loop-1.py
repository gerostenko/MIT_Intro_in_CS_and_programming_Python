# num_x = int(input('How many times should I print the letterX? ')) 
# to_print = '' 
#concatenate X to to_print num_x times 
# print(to_print 
# Make this code work with while loop. 

num_x = int(input('How many times should I print the letterX? '))  
iterator = 0 
result = "" 
while(iterator < abs(num_x)): 
    result = result + "X" 
    iterator = iterator + 1 
print(result) 