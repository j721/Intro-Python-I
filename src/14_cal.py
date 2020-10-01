"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

#Program should print calendar for current month and current year
now =datetime.now()

# def set_cal(month =int(currentMonth), year =int(currentYear)):

if len(sys.argv) ==1: 
#Returns current date if no input is specified
  calendar.prmonth(now.year, now.month)
elif len(sys.argv) ==2:
   #Renders the calendar for month input specified and current year
  calendar.prmonth(now.year, int(sys.argv[1]))
elif len(sys.argv) ==3:
  calendar.prmonth(int(sys.argv[2]), int(sys.argv[1]))
   #Renders calendar to month and year inputs that are specified
else:
  print("Usage: 14_cal.py [month] [year]")


#2nd Method that works

# now = datetime.now()
# month, year = now.month, now.year

# cal = calendar.TextCalendar(firstweekday=6)

# if len (sys.argv) ==1:
#   cal.prmonth(year,month)
# elif len(sys.argv) ==2:
#   cal.prmonth(year, int(sys.argv[1]))
# elif len(sys.argv) ==3:
#   cal.prmonth(int(sys.argv[2]),int(sys.argv[1]))
# else:
#   print("usage: filename month year")
#   sys.exit(1)

#3rd method

#receive user input as argument input (not going to user input function)
#sys.argv is a list of args that the user provides at the start of the program
# num_args = len(sys.argv)

# #init an instance of the text calendar class
# cal = calendar.TextCalendar()

# month = datetime.now().month
# year = datetime.now().year

# #if user specified no args:
# if num_args == 1:  #length of 1, always get name of the program (i.e. the file 14_cal.py)
#   #print current month and year 
#   pass
#   #we want to print out the month with the calendar

# #if user specified one args:
# elif num_args ==2:
#   #assume that args is the month
#   month =int(sys.argv[1])
#   #print that month of the current year

# #if user specified two args:
# elif num_args ==3:
#   #print that month of that year
#   month = int(sys.argv[1])
#   year = int(sys.argv[2])
# #otherwise
# else
# #print a usage statement
#   print("usage: cal.py [month] [year]")
#   sys.exit(1) # provides exit status

# cal.prmonth(year,month)