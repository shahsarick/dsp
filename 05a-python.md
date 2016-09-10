# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples are comprised of entries that can have different meanings, lists are comprised of entries which have the same type. Tuples have structure, lists have order. Tuples are immutable as well while lists are mutable. This means that tuples can be used as keys in a dictionary. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are unordered while lists are ordered. Also the items in a set have to be hashable. Sets are way faster than lists if the goal is to see if a value is present in the set but sets are slower when it comes to iteration compared to lists. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda is an anonymous function rather than an arbitrary function and the parameter being accepted would be the variable you're working with, and the column in which you're sorting it on.

Ex: >>> (lambda y: y+10)(3)
13 

For sorted() here's an example:
 >>> sorted(['A', 'C', 'B', 'D'], key=lambda word: word.lower())
['A', 'B', 'C', 'D']




---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> x = [1, 9, 0, 4]

squares = [ e**2 for e in x]

print squares
# [ 1, 81, 0, 16 ]

The filter applies a predicate to the sequence and map modifies each member of a sequence. Ex:

>> map(lambda e: e**2, filter(lambda e: type(e) == types.IntType, x))

In the statement above, it calls to filter and map as well as type.  


Set comprehension:

>>> nums = set(n**2 for n in range(10))
>>> nums
{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

Dictioary comprehension layout is in the form:
{key: value for (key, value) in iterable}




---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





