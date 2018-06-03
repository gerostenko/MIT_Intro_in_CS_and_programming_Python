# -*- coding: utf-8 -*-
"""
Created on Sat May 12 19:24:24 2018

@author: Galina
"""

#Part C
#house and salary related vars
portion_down_payment = 0.25
r = 0.04
salary_raise = 0.07
total_house_cost = 1000000
goal = total_house_cost * portion_down_payment
raise_time = False
initial_anual_salary = float(input('Enter your annual salary: '))
able_to_pay_in_3_months = True

#bisection search related vars
low = 0
high = 10000
portion_saved = (low + high) // 2 
epsilon = 100
bisection_steps = 0

#so bad there's no do...while, huh...
while True:
	bisection_steps += 1
	#resetting house and salary related vars
	current_savings = 0
	months_of_saving = 0
	annual_salary = initial_anual_salary
	#calculate the current_savings
	while months_of_saving <= 36:
		if raise_time == True:
			annual_salary += annual_salary*salary_raise
		
		current_savings += current_savings*(r/12)
		current_savings += annual_salary/12 * (portion_saved/ 10000)
		months_of_saving += 1
		
		if months_of_saving %6 == 0:
			raise_time = True
		else:
			raise_time = False
	
	#check if we reached required amount or amount close to required
	if abs(current_savings - goal) <= epsilon:
		break
	
	#reset the high and low (bisection search tricks)
	if current_savings < goal:
		low = portion_saved
	else:
		high = portion_saved
	portion_saved = (low + high) // 2
	
	#check if possible to pay out in 36 months
	if high >= 10000:
		able_to_pay_in_3_months = False
		break

#output depends on whether it's possible to pay the house in 36 months or not
if able_to_pay_in_3_months:
	print('Portion to save: ', portion_saved / 10000)
	print('Steps: ', bisection_steps)
else:
	print('It is not possible to pay the down payment in three years.')


