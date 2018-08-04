def checkio(expression):
    exp_list = []
    result = []
    dic = {')': '(', ']': '[', '}': '{'}
    for exp in expression:
        if exp in ['(', '[', '{']:
            exp_list.append(exp)
        elif exp in [')', ']', '}']:
            try:
                result.append(exp_list.pop() == dic[exp])
            except:
                return False
    return all(result) & (not exp_list)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"

'''
def checkio(data):
    stack=[""]
    brackets={"(":")","[":"]","{":"}"}
    for c in data:
        if c in brackets:
            stack.append(brackets[c])
        elif c in brackets.values() and c!=stack.pop():
            return False
    return stack==[""]
---------------------------------------------------------
def checkio(expression):
    s = ''.join(c for c in expression if c in '([{}])')
    while s:
        s0, s = s, s.replace('()', '').replace('[]', '').replace('{}', '')
        if s == s0:
            return False
    return True
---------------------------------------------------------
def checkio(str):
    str = ''.join([c for c in str if c in '()[]{}'])

    while any(b in str for b in ('()', '[]', '{}')):
        str = str.replace('()', '').replace('[]', '').replace('{}', '')
    return not str
'''

