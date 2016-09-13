'''
Find out different degrees and list their frequency
'''
import string
import pandas as pd

with open('faculty.csv', 'rb') as f:
    reader = csv.reader(f)
    facultylist = list(reader)   
degrees = [y[1] for y in facultylist]

def remove_punctuation_and_split(word):
    return word.translate(None, string.punctuation) 
degrees_no_punctuation = []

for text in degrees:
    degrees_no_punctuation.append(remove_punctuation_and_split(text))    
degrees_lower = []
[degrees_lower.append(z.lower().split()) for z in degrees_no_punctuation]  

   
flattened  = [val for sublist in degrees_lower for val in sublist]
flattened.pop(0)
df = pd.DataFrame(flattened)
df.groupby(df[0]).size()


'''
Find out different titles and list their frequencies
'''

titles = [y[2] for y in facultylist]
titles.pop(0)
df2 = pd.DataFrame(titles)
df2.groupby(df2[0]).size()
