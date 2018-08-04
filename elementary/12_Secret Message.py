def find_message(text: str) -> str:
    """Find a secret message"""
    return ''.join(t for t in text if t.isupper())

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

'''
    find_message = ''.join(filter(str.isupper, text))
    return find_message 
--------------------------------------------------
return ''.join(filter(str.istitle, text))
--------------------------------------------------
return ''.join(x * x.isupper() for x in text)
'''