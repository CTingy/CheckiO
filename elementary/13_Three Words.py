def checkio(words):
    count = 0
    for word in words.split():
        if word.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False
    
   
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

'''
def checkio(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False
------------------------------------------
import re
def checkio(words):
    return bool(re.compile("([a-zA-Z]+ ){2}[a-zA-Z]+").search(words))
-----------------------------------------------
import re
def checkio(words):
    return bool(re.search('\D+ \D+ \D+', words))
----------------------------------------------------
def checkio(x):
    x = x.split()
    x = ''.join([str(0) if i.isdigit() else str(1) for i in x])
    return True if "111" in x else False
----------------------------------------------------
def checkio(s):
    l = [x.isalpha() for x in s.split()]
    return [True]*3 in [l[i:i+3] for i in range(len(l)-2)]
    # if [True, True, True] in l
-----------------------------------------------------------
checkio = lambda words: True if "True, True, True" in "".join(str([x.isalpha() for x in words.split()])) else False
----------------------------------------------------------------
def checkio(words):
    words = words.split()
    for num in range(len(words) - 2):
        if all(elem.isalpha() for elem in words[num: num + 3]):
            return True
    return False
    # all() function
'''




