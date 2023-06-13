import re
"""
Exercise #2

Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
Should output:
{'a': 5, <-pay attention to this. needs to include the capital A
'abstract': 1,
'an': 3,
'array': 2, ... etc...
"""

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def e3(alist):
    w_count = {}
    split = re.split(r'\W+', alist)
    
    for word in split:
        w_count[word.lower()] = w_count.get(word.lower(), 0) + 1

    return w_count

print(e3(a_text))