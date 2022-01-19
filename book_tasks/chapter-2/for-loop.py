# Write a program that prints the sum of the prime umbers greater than 2 and less than 1000. 
# Hint: you probably want to use a for loop that is a primality test nested inside a for 
# loop that iterates over the odd integers between 3 and 999

total = 0
for number in range(3, 999, 2):
    if number%3 == 0 and number != 3:
        continue
    base = 5
    isPrime = True
    #Algorithm below is borrowed from https://en.wikipedia.org/wiki/Primality_test
    while (base**2 <= number):
        if(number % base == 0 or (number % (base + 2)) == 0):
            isPrime = False
            break
        base += 6
    if(isPrime):
        total += number

print(total)