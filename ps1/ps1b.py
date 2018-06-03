# -*- coding: utf-8 -*-
"""
Created on Sat May 12 19:24:24 2018

@author: Galina
"""
#Part B
# =============================================================================
portion_down_payment = 0.25
current_savings = 0
r = 0.04
number_of_months = 0
raise_time = False

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save,as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
salary_raise=float(input('Enter the semi­annual raise, as a decimal: '))

while current_savings <= total_cost*portion_down_payment :
    if raise_time == True:
        annual_salary += annual_salary*salary_raise
        
    current_savings += current_savings*r/12
    current_savings += annual_salary/12*portion_saved
    number_of_months += 1
    
    if number_of_months%6 == 0:
        raise_time = True
    else:
        raise_time = False
        
print('Number of months: ', number_of_months)
# =============================================================================