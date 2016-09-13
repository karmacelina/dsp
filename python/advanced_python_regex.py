#Q1. 
#Find how many different degrees there are, and their frequency.

import pandas as pd
import re 

# Read in the file using pandas
path = 'faculty.csv'
faculty = pd.read_csv(path)

# Define a function to remove space and points from string elements of a list. 
def remove_space_and_points(degrees):

    degrees_no_points = []
    for d in degrees:
        degrees_no_points.append(re.sub(r"[.]", "", d))

    degrees_no_points_no_spaces = []
    for d in degrees_no_points:
        if d[0] == " ":
            #strip removes specified character from start/end of string
            degrees_no_points_no_spaces.append(d.strip(" "))
        else:
        	degrees_no_points_no_spaces.append(d)

    return degrees_no_points_no_spaces

# Create list of degrees
degrees = faculty[u' degree'].tolist() 

# Apply function to the newly created list
degrees_list = remove_space_and_points(degrees)

# Split degrees that have spaces
all_degrees = [] 
for degree in degrees_list:
    if " " in degree:
        for d in degree.split(" "):
            all_degrees.append(d)
    else:
        all_degrees.append(degree)

# Create dictionary to list and count frequency of different degrees.
degrees_dict = {}
for d in all_degrees:
    if d != '0': # add this to eliminate degree '0' from consideration
        v = all_degrees.count(d)
        degrees_dict[d] = v


print "There are %d different degrees." % len(degrees_dict.keys())
print "\n"
for (k,v) in degrees_dict.items():
    print "%s : %d" % (k, v)
print "\n"


# # # 

#Q2. 
#Find how many different titles there are, and their frequencies:

titles = faculty[u' title'].tolist()

title_list = ["Professor", "Assistant Professor", "Associate Professor"]

d = {}
for title in title_list:
	v = len( [s for s in titles if s[:len(title)] == title])
	d[title] = v

for (k, v) in d.items():
	print "There are %d %ss" % (v, k)

print "\n"

# # # 

#Q3.
#Search for email address and put them in a list. 
#Print the list of email addresses

emails = faculty[u' email'].tolist()

print "The list of emails is:" 
print emails
print "\n"

# # # 

#Q4.
#Find how many different email domains there are.
#Print the list of unique email domains.

email_domains = [] 
for email in emails:
    email_domains.append(re.search("@[\w.]+", email).group())

print "\nThere are %d email domains." % len(set(email_domains))

for email in set(email_domains):
	print "\ndomain: %s" % email

