[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>-0.069049861392
```python
import nsfg
import pandas as pd
from statistics import mean, stdev
from math import sqrt
df = nsfg.ReadFemPreg()
df.dropna
df1 = df[['pregordr', 'totalwgt_lb']]
df1.dropna
df2 = df1[df1.pregordr.notnull()]
df2 = df1[df1.totalwgt_lb.notnull()]
list1 = df2.values.tolist()
#x = first order, y = 2nd order
x, y = [],[]
for i in list1:
    if i[0] == 1:
        x.append(i[1])
    else:
        y.append(i[1])
cohens_d = (mean(x) - mean(y)) / sqrt((stdev(x) ** 2 + stdev(y) ** 2) / 2.0)
```
