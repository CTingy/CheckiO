import re

def checkio(data):
    
    a = False
    b = False
    c = False
    d = False
        
    if len(data) >= 10:
        a = True
    for s in data:
        if s.isupper():
            b = True
        if s.islower():
            c = True
        if s.isdigit():
            d = True
    return a and b and c and d
    #return not(len(data)<10 or data.isupper() or data.islower() or data.isdigit() or data.isalpha())


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    checkio('A1213pokl') #== False, "1st example"
    checkio('bAse730onE4') #== True, "2nd example"
    checkio('asasasasasasasaas') #== False, "3rd example"
    checkio('QWERTYqwerty') #== False, "4th example"
    checkio('123456123456') #== False, "5th example"
    checkio('QwErTy911poqqqq') #== True, "6th example"
    #print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


'''
checkio = lambda s: not(
        len(s) < 10
        or s.isdigit()
        or s.isalpha()
        or s.islower()
        or s.isupper()
    )
------------------------------------
def checkio(data):
    import re
    if len(data)<10:
        return False
    if not re.search('[0-9]', data):
        return False
    if not re.search('[a-z]', data):
        return False
    if not re.search('[A-Z]', data):
        return False
    return True
-----------------------------------
import re

def checkio(data):
    return bool(re.search(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{10,}$', data))
'''