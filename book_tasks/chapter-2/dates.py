import calendar as cal
from datetime import date

def find_thanksgiving(year):    
    month = cal.monthcalendar(year, 11)   
    if month[0][cal.THURSDAY] != 0:        
        thanksgiving = month[3][cal.THURSDAY]    
    else:        
        thanksgiving = month[4][cal.THURSDAY]
    return date(year, 11, thanksgiving)

def shopping_days(year):    
    """year a number >= 1941      
    returns the number of days between U.S. Thanksgiving
    and Christmas in year"""

    thankgiving_date = find_thanksgiving(year)
    chrimstmas_date = date(year, 12, 25)
    return chrimstmas_date - thankgiving_date
print(shopping_days(2022))

import calendar as cal
from datetime import date

def find_canadian_thanksgiving(year):    
    month = cal.monthcalendar(year, 10) 
    if month[0][cal.MONDAY] != 0:        
        thanksgiving = month[1][cal.MONDAY]    
    else:        
        thanksgiving = month[2][cal.MONDAY]
    return date(year, 10, thanksgiving)

def shopping_days_canadian(year):    
    """year a number >= 1942    
    returns the number of days between Canadian Thanksgiving
    and Christmas in year"""

    thankgiving_date = find_canadian_thanksgiving(year)
    chrimstmas_date = date(year, 12, 25)
    return chrimstmas_date - thankgiving_date
print(shopping_days_canadian(2022))
