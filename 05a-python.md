# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists are mutable objects, whereas tuples are immutable. 
Lists and tuples can both be indexed.
Tuples will work as keys in dictionaries because they're immutable. Dictionary keys have to be be immutable objects. Dictionary keys need to be hashable (dictionaries = hash tables). 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Python lists and sets are similar in that they can be iterated over, but they differ in that sets cannot be indexed, since they are unordered.

>> sentence = "Today is a nice day for a walk"

>> words = sentence.split()  # this is a list

>> unique_words = set(words) # this is a set whose elements are the unique tokens of the sentence defined above

>> Performance of sets for finding an element is faster  -- sets only contain each element once. 



---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is an anonymous function than can be used without explicitly definining it. For example, it can be used to sort words (tokens) in a sentence:

>> sentence = "My name is Laura del Mar and I had a birthday yesterday. I am 33 years old"

>> words = sentence.split()

>> sorted(words, key = lambda word: word.lower()) , 

>> rather than defining a function and calling it on the key argument.

>> Lambdas are super useful when using filter, map or reduce. 



---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions can be used to easily construct lists in Python. 

>> example #1: 

>> evens_to_100 = [i for i in range(101) if i % 2 == 0] is equivalent to:

evens_to_100 = filter(lambda x: x % 2 == 0, range(101))

>> example #2: 

>> squares = [x\*\*2 for x in [0,0,1,2,3,4]] is equivalent to:

squares = map(lambda x: x\*\*2, [0,0,1,2,3,4])

>> * List comprehensions probably perform faster than equivalent statements using map or filter because no variables are kept after being used. 
	* When you run something like: squares = map(lambda x: x\*\*2, range(5)), the last value assigned to x is kept. 
	* When you run squares = [x**2 for x in range(5)], x is not kept in memory. 

>> Set comprehensions: 

>> example #1: 

>> squares_set = {x\*\*2 for 3x in set([0,0,1,2,3,4])}

>> Dictionary comprehensions:

>> example:  *WORK HERE!*

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

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





