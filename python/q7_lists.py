# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """ 
    Given a list of strings, return the count of the number of 
    strings where the string length is 2 or more and the first and 
    last chars of the string are the same 
    """
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[len(word)-1]:
            count += 1
    return count
    raise NotImplementedError


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
    """
    new_list = []
    list_x = []
    for word in words:
        if word[0] == "x":
            list_x.append(word)
        else:
            new_list.append(word)
    
    list_x = sorted(list_x)
    new_list = sorted(new_list)
    
    list_x.extend(new_list)
    
    return list_x

    raise NotImplementedError


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].
    """
    reversed_tuple =[]
    for tuple in tuples:
        reversed_tuple.append(tuple[::-1])

    new_list = []
    for tuple in sorted(reversed_tuple):
        new_list.append(tuple[::-1])
    
    return new_list

    raise NotImplementedError


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.
    """
    nums2 = list(nums) # copy the list

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]: 
            nums2[i] = ""
    
    while "" in nums2:
        nums2.remove("")
    
    return nums2

    raise NotImplementedError



def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    
    
    ## Not linear in time:
    # list3 = list1 + list2
    # return sorted(list3)
    
    ## Importing a module that called the merge algorithm:
    # from heapq import merge 
    # list3 = list(merge(list1, list2))
    # return list3

    list3 = []
    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            list3.append(list1.pop(0))
        else:
            list3.append(list2.pop(0))
    list3.extend(list1)
    list3.extend(list2)

    return list3

    raise NotImplementedError
