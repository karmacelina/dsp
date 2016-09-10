# Hint:  use Google to find python function

import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

# Write down the format in which the dates are written
format = '%m-%d-%Y' 

# Put the dates in datetime object format using "format" string
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

date_start_dt= datetime.datetime.strptime(date_start, format)
date_stop_dt = datetime.datetime.strptime(date_stop, format)

print date_start_dt
print date_stop_dt

# now that the dates are in datetime object format, subtract them
print date_stop_dt - date_start_dt, "\n"


####b)  
date_start = '12312013'  
date_stop = '05282015'  

format =  '%m%d%Y'

date_start_dt= datetime.datetime.strptime(date_start, format)
date_stop_dt = datetime.datetime.strptime(date_stop, format)

print date_start_dt
print date_stop_dt

print date_stop_dt - date_start_dt, "\n"


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

format = '%d-%b-%Y'

date_start_dt= datetime.datetime.strptime(date_start, format)
date_stop_dt = datetime.datetime.strptime(date_stop, format)

print date_start_dt
print date_stop_dt

print date_stop_dt - date_start_dt, "\n"