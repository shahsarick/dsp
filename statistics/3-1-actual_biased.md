[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```python

import thinkstats2
import chap01soln
resp = chap01soln.ReadFemResp()
actual = thinkstats2.Pmf(resp.numkdhh)
import thinkplot
thinkplot.Pmf(actual)
actual.Mean() #1.0242051550438309



def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf
    
biased = BiasPmf(actual, label='observed')
thinkplot.PrePlot(2)
thinkplot.Pmfs([biased])

biased.Mean() #2.4036791006642821
```
