# Q7.

import pandas as pd 

# Create pandas dataframe from csv
path = 'faculty.csv'
faculty = pd.read_csv(path)

# Create lists using series of dataframe
names = faculty[u'name'].tolist()
degrees = faculty[u' degree'].tolist()
titles = faculty[u' title'].tolist()
emails = faculty[u' email'].tolist()

# Make lists of the names
names_list = [] 
for name in names:
	names_list.append(name.split(" "))

# Iterate over lists in names_list to get first and last names
first_names = []
last_names = []
for name in names_list:
	first_names.append(name[0])
	last_names.append(name[-1])

# Create list of tuple with first and last name of each faculty member
name_zip = zip(first_names, last_names)

# Creare list with each faculty member's degree, title, email info
faculty_info = [[a, b, c] for (a, b, c) in zip(degrees, titles, emails)]

# Create list of tuples with (first, last) names and (degree, title, email) info
zipped_list = zip(name_zip,faculty_info)

# Define dictionary
faculty_dict = {k:v for (k,v) in zipped_list}

# Print three key-value pairs
# It doesn't make sense to ask for the "first" three elements of a dictionary, because
# dictionaries do not have order.

for k in faculty_dict.keys()[:3]:
	print k, ":", faculty_dict[k]




