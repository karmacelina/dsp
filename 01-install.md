# Install software on your computer


### Install [git](http://git-scm.com/).

You have it installed if you can run `git --version` at the command
line and get output like `git version 2.3.5`.


### Install [Anaconda](http://continuum.io/downloads).

There are two things you can verify to check your install.

First, from the command line, all of the following should start up
some kind of Python interpreter:

```bash
python
ipython
ipython notebook
spyder
```

Second, inside any of those Python interpreters, you should be able to
do all of these without error:

```python
import numpy
import scipy
import matplotlib
import pandas
import statsmodels
import sklearn
```

### Install [Homebrew](http://brew.sh/) on Mac

If you use a Mac, install Homebrew if you don't
have it yet. You could use Homebrew to manage your `git` and `python`
installs as well, but the methods given above are very good and more
cross-platform.

---

###Q1. Python Version 2 or 3

**Course material for the bootcamp is currently based on Python version 2.7. Students have the option of using either version 2 or 3 during the bootcamp, but should be aware of some differences in code between the two versions.**  

Did you install Python 2 or 3? Why?  

>> I am using Python 2.7 as installed thru Anaconda; I have an environment with Python 3.5 so I have access to that kernel. Python 3.5 doesn't have unicode text issues, so might be better for natural language applications?

###Q2. Which Python Version Installed   

How can you check the version of Python installed if you happen to be on an unfamiliar computer?

>> At the Terminal (assuming computer is a Mac), type which python, i.e. $ which python
If interested in seeing other versions of python available, type $ which -a python 

 


