from collections import Counter
def checkio(text):
    text = text.lower()
    for t in text:
        if not t.isalpha():
            text = text.replace(t,'')
    t = Counter(text)
    maxk = 'z'
    maxv = 0
    for key in t:
        if t[key] > maxv:
            maxv = t[key]
            maxk = key
        elif t[key] == maxv and maxk > key:
            maxk = key
    return maxk
            

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

'''
import string
def checkio(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

ex:
a = [(2, 3), (3, 1)] # We want to sort by second elements
a.sort(key=lambda x: x[1])
---------------------------------------------------------
from string import ascii_lowercase as letters
checkio = lambda text: max(letters, key=text.lower().count)
----------------------------------------------------------
from collections import Counter
def checkio(text):
    count = Counter([x for x in text.lower() if x.isalpha()])
    m = max(count.values())
    return sorted([x for (x, y) in count.items() if y == m])[0]
-----------------------------------------------------------
import collections
def checkio(text):
    freq_list = collections.Counter(filter(str.isalpha, text.lower())).most_common()
    most_freq_count = max(freq[1] for freq in freq_list)
    return sorted([freq[0] for freq in freq_list if freq[1] == most_freq_count])[0]
------------------------------------------------------------
def checkio(text):
    s = list(text.lower())
    letters = [s.count(chr(x)) for x in range(97,123)]
    return chr(97+letters.index(max(letters)))
------------------------------------------------------------
def checkio(text):
    letters = [ch for ch in text.lower() if ch.isalpha()]
    letter_count = {ch: letters.count(ch) for ch in set(letters)}
    return max(sorted(letter_count), key=letter_count.get)
'''



