# Write  code that  asks  the  user  to  enter theirbirthday in the form mm/dd/yyyy, 
# and then prints a string of theform ‘You were born in the year yyyy.’

date = input("Enter your birthday in the form mm/dd/yyyy") 
year = date[-4:] 
print(f'You were born in the year {year}') 