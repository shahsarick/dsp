'''
write emails to a new csv file
'''
import string
import pandas as pd

with open('faculty.csv', 'rb') as f:
    reader = csv.reader(f)
    facultylist = list(reader)   
emails = [y[3] for y in facultylist]
df3 = pd.DataFrame(emails)
header = ["email"]
df3.to_csv('output.csv', cols = header, index = False)
