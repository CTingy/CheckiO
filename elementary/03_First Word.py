def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    return text.replace('.', ' ').split()[0].rstrip(',')


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")

'''
import re
word = re.compile(r"[\w']+")
first_word = lambda text: word.search(text).group()
--------------------------------------------------------

def first_word(text: str) -> str:
  
    text = text.replace('.',' ').replace(',',' ').split(' ')
    for i in text:
        if i != '' and i != ' ':
            return i
            break
        else:
            continue
    
    return text.replace(",", " ").replace(".", " ").split()[0]
--------------------------------------------------------    
    import re
    return re.search("([\w']+)", text).group(1)

'''