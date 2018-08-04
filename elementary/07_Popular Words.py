def popular_words(text: str, words: list) -> dict:
    text = ' ' + text.lower().replace('\n', ' ') + ' '
    return {word: text.count(' '+word+' ') for word in words}


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")

'''
def popular_words(text, words):
    lower_count = text.lower().split().count
    return {word: lower_count(word) for word in words}
---------------------------------------------------------
import re
return dict([[word, len(re.findall('\\b' + word + '\\b', text, re.I))] for word in words])
---------------------------------------------------------
return dict(zip(words, map(text.lower().split().count, words)))
-----------------------------------------------------------
'''