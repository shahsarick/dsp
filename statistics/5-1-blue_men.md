[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```python
from scipy.stats import norm
normal = norm(loc = 178, scale = 7.7)
print normal.cdf(185.4) - normal.cdf(177.8)
#0.342094682946
```
