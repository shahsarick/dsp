import csv
with open('faculty.csv') as f:
    f.readline()
    reader=csv.reader(f,delimiter=',')
    mydict=dict((rows[0],[rows[1], rows[2], rows[3]]) for rows in reader)
