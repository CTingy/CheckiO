def between_markers(text, begin, end):
    """
        returns substring between two given markers
    """
    t = text
    if begin in text:
        t = text.split(begin)[1]
        if end in text.split(begin)[0]:
            return ""
    if end in t:
        t = t.split(end)[0]
        return t
    return t
    #text = text.split(begin)[1] if begin in text else text
    #text = text.split(end)[0] if end in text else text
    #return text

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'

'''
def between_markers(text: str, begin: str, end: str) -> str:
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]
---------------------------------------------------------
import re
def between_markers(text: str, begin: str, end: str) -> str:
    if re.search(f"{re.escape(end)}.*{re.escape(begin)}", text):
        return ""
    return text.split(begin)[-1].split(end)[0]
--------------------------------------------------
def between_markers(text: str, begin: str, end: str) -> str:
    if text.count(begin)*text.count(end)>0 and text.index(begin)>text.index(end):
        return ""
    else:
        return text.split(begin)[-1].split(end)[0]
---------------------------------------------------------



