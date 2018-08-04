from collections import Counter
def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    #return max(Counter(data), key=lambda i: Counter(data)[i])
    return max(data, key=data.count)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]))
    
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')

'''
most_frequent = lambda seq: max(seq, key=seq.count)
----------------------------------
from statistics import mode as most_frequent
---------------------------------------------
return Counter(data).most_common(1)[0][0]
--------------------------------------------
    counter = Counter(data)
    elem, count = counter.most_common(1)[0]
    return elem

a=[1,2,4,4,6,4,5,6]
>>> Counter(a).most_common(3)
[(4, 3), (6, 2), (1, 1)]
>>> Counter(a).most_common(1)
[(4, 3)]
'''