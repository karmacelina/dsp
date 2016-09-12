#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


""" I interpreted this question as asking for the minimum of the absolute value of the 
difference between the two values. Otherwise, the team with the smallest difference 
in for and against goals is Leicester, with 34 more goals against than for. To get this, 
the same process applies, except that the absolute value is not calculated. (line 23) """

import pandas as pd 
import math as m 

football = pd.read_csv('football.csv')

football['Goal difference'] = football['Goals'] - football['Goals Allowed']

football['Goal difference'] = football['Goal difference'].apply(m.fabs)

# to get actual minimal difference between the two numbers
#print min(football['Goal difference']) 

# to obtain the index of the team that has the minimum difference
#print football['Goal difference'].argmin()

print ("The team with the smallest difference in 'for' and 'against' goals is" 
	 " %s." % football['Team'][football['Goal difference'].argmin()])