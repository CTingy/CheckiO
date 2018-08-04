from typing import List, Any
from collections import Counter


def all_the_same(elements: List[Any]) -> bool:
    if len(Counter(elements)) < 2:
        return True
    return False

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

'''
return elements[1:] == elements[:-1]
-----------------------------------------
return len(set(elements)) <= 1
-----------------------------------
return elements == elements[1:] + elements[:1]
----------------------------------------
all_the_same = lambda elements: not elements or [elements[0]] * len(elements) == elements
---------------------------------------------
return all(x == y for x, y in zip(elements, elements[1:]))
-----------------------------------------------
from itertools import groupby
def all_the_same(elements):
    return sum(1 for _ in groupby(elements)) < 2
'''

