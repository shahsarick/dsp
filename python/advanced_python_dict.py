import csv
with open('faculty.csv') as f:
    f.readline()
    reader=csv.reader(f,delimiter=',')
    mydict=dict((rows[0],[rows[1], rows[2], rows[3]]) for rows in reader)

#Very messy solution, definitely need more practice with dictionaries
from nameparser import HumanName
new_names = []
for i in facultynames:   
    name = HumanName(i)
    new_names.append([name.first, name.last])
name_df = pd.DataFrame(new_names)
rest = [y[1:4] for y in facultylist]
rest_df= pd.DataFrame(rest)
result = pd.concat([name_df, rest_df], axis=1, join_axes=[name_df.index])
result.columns = ['first', 'last', 'degree', 'department', 'email']
result = result.ix[1:]
result.to_csv('output2.csv', index = False)
with open('output2.csv') as f:
    f.readline()#ignore first line
    reader=csv.reader(f,delimiter=',')        
    mydict=dict([((rows[0],rows[1]), [rows[2], rows[3]]) for rows in reader])
#For the last part, switch the dict definiteion to have last names first
with open('output2.csv') as f:
    f.readline()#ignore first line
    reader=csv.reader(f,delimiter=',')        
    mydict=dict([((rows[1],rows[0]), [rows[2], rows[3], rows[4]]) for rows in reader])
#then order
import collections
ordered = collections.OrderedDict(sorted(mydict.items()))
