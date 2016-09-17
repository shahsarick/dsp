[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```python
a = [int(100*random.random()) for i in xrange(1000)]
b = thinkstats2.Pmf(a)
thinkplot.Pmf(b)
```


