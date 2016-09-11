# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    """
    
    if count < 10:
        return "Number of donuts: %r" % count
    else:
        return "many"

    raise NotImplementedError


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
    """

    if len(s) >= 2:
        return s[:2] + s[-2:]
    else:
        return ""

    raise NotImplementedError


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.
    """

    
    S = s.replace(s[0], "*")
    S = s[0] + S[1:]

    return S

    raise NotImplementedError


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    return b[:2] + a[2:], a[:2] + b[2:]
    raise NotImplementedError


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) >= 3:
        if s[-3:] == 'ing':
            return s + "ly"
        else:
            return s + 'ing'
    else:
        return s
    raise NotImplementedError


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'
    """

    if "not" in s and "bad" in s:
        if s.find("bad") > s.find("not"):
            S = s.replace(s[s.find("not"):s.find("bad") + len("bad")], "good")
            return S
        else: 
            return s
    else:
        return s
        
    raise NotImplementedError


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
    """

    if len(a) % 2 == 0:
        a_front = a[:len(a)/2]
        a_back = a[len(a)/2:]
    else:
        a_front = a[:(len(a) + 1)/2]
        a_back = a[(len(a) + 1)/2:]
        
    if len(b) % 2 == 0:
        b_front = b[:len(b)/2]
        b_back = b[len(b)/2:]
    else:
        b_front = b[:(len(b) + 1)/2]
        b_back = b[(len(b) + 1)/2:]
    
    return a_front + b_front + a_back + b_back

    raise NotImplementedError
