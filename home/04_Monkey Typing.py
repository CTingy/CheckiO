def count_words(text: str, words: set) -> int:
    count = 0
    for word in words:
        if word in text.lower():
            count += 1
    return count
    # return len([word for word in words if text.lower().count(word) > 0])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

'''
def count_words(text, words):
    return sum(w in text.lower() for w in words)
----------------------------------------------------
def count_words(text, words):
    return len([word for word in words if text.lower().find(word) >= 0])
----------------------------------------------------
def count_words(text, words):
    bools = [w in text.lower() for w in words]
    return bools.count(True)
-----------------------------------------
import re
def count_words(text, words):
    return len(set(re.findall('|'.join(words), text, re.IGNORECASE)))
-------------------------------------------------
def count_words(text, words):
    return sum([word in text.casefold() for word in words])
---------------------------------------------
def count_words(text, words):
    import functools, operator
    return sum(map(functools.partial(operator.contains, text.lower()), words))
-------------------------------------------------------------
count_words=lambda str,words: sum(str.lower().find(e)>=0 for e in words)

'''






