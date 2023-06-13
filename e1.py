"""
Exercise #1

Reverse the list below in-place using an in-place algorithm.
For extra credit: Reverse the strings at the same time.
"""


words = ['this' , 'is', 'a', 'sentence', '.']

def e1(e_list, a, b, c, d, e):
    e_list[a], e_list[b], e_list[c], e_list[d], e_list[e] = e_list[e], e_list[d], e_list[c], e_list[b], e_list[a]
    
e1(words, 0, 1, 2, 3, 4)
print(words)