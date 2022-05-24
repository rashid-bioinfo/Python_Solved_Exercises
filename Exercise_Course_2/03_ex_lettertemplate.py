'''
Write a letter template
'''
from datetime import date

name = 'Rashid'
today = date.today()
print( '''Dear %s
you are selected!
%s''' %(name, today))