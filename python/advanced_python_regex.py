#Q1. 
#Find how many different degrees there are, and their frequency.

import pandas as pd
import re 

path = 'faculty.csv'

faculty = pd.read_csv(path)

degrees = faculty[u' degree'].tolist()

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

degrees_list = remove_space_and_points(degrees)

# attempt to split degrees that have spaces
for degree in degrees_list:
	if " " in degree:
		degree.split(" ")

degrees_dict = {}
for d in degrees_list :
    v = degrees_list.count(d)
    degrees_dict[d] = v  

print degrees_dict
print "\n"

# I need to improve this one.  
# Is there a way I can take the degrees that have multiple degrees in them 
# and split them by " " space?

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

