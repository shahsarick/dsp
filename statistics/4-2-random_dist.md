[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```python
import numpy as np
a = [int(100*random.random()) for i in xrange(1000)]
pmf = thinkstats2.Pmf(a)
thinkplot.Pmf(pmf)

cdf = thinkstats2.Cdf(a)
sample = np.random.choice(a, 100, replace=True)
ranks = [cdf.PercentileRank(j) for j in sample]
rank_cdf = thinkstats2.Cdf(ranks)
thinkplot.Cdf(rank_cdf)
```


