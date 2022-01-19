# The Empire State Building is 102 stories high. Aman wanted to know t
# he highest floor from which he could drop anegg without the egg breaking. 
# He proposed to drop an egg from thetop floor. If it broke, he would go 
# down a floor, and try it again. Hewould do  this  until  the  egg  did 
# not  break. At  worst, this  methodrequires 102  eggs. 
# Implement  a  method that  at  worst uses  seveneggs.


total_num_of_floors = 102
floor_of_no_break = 13
num_guesses = 0
low = 0
high = total_num_of_floors
ans = (high + low) / 2 

while (ans != floor_of_no_break):
    print(f"low = {low}, high = {high}, ans = {ans}")
    num_guesses += 1
    if(ans < floor_of_no_break):
        low = ans
    else:
        high = ans
    
    ans = round((high + low)/2)

print(f"number of guesses = {num_guesses}")
print(f"found answer = {ans} which is the same as {floor_of_no_break} ")