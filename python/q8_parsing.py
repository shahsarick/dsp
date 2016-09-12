# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

#'aston_villa' and -1 is the min difference
with open('football.csv', 'rb') as f:
    reader = csv.reader(f)
    list1 = list(reader)
    
list1.pop(0)
goals = [x[5] for x in list1]
goals_allowed = [x[6]for x in list1]
values = [int(a) - int(b) for a, b in zip(goals, goals_allowed)]
min([abs(number) for number in values])
print values.index(min(values))
print min(values)
teamlist = [x[0] for x in list1]
print teamlist[values.index(-1)]
