def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    text = text.replace(symbol, '', 1)
    return text.index(symbol) + 1 if symbol in text else None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')

'''
    try:
        return text.index(symbol, text.index(symbol) + 1)
    except ValueError:
        return None
---------------------------------------
    count = 0
    for i, c in enumerate(text):
        if c == char:
            count = count + 1
            if count == 2:
                return i
    return None
--------------------------------------
    if text.count(symbol) < 2: 
        return None
    else:
        return text.find(symbol, text.find(symbol) + 1);
---------------------------------------
    num = text.find(symbol, text.find(symbol)+1)
    return num if num>-1 else None
-------------------------------------------
second_index = lambda t, s: ([i for i, c in enumerate(t) if c == s] + [None, None])[1]
'''






