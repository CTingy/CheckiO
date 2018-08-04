def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    count = 1
    count_list = [0]
    for i in range(1, len(line)):
        if line[i] == line[i-1]:
            count += 1
        else:
            count = 1
        count_list.append(count)
    return max(count_list)
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')

'''
from itertools import groupby
def long_repeat(line):
    return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)
------------------------------------------------------------
import re

def long_repeat(line):
    longest = 0
    for letter in set(list(line)):
        new = max(len(i) for i in re.findall("{}+".format(letter), line))
        longest = new if new>longest else longest
    return longest
'''

