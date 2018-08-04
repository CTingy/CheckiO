def checkio(str_number: str, radix: int) -> int:
    s = str_number[::-1]
    sum = 0
    for i in range(len(s)):
        if s[i].isalpha() and radix > (ord(s[i])-55):
            sum += pow(radix, i) * (ord(s[i])-55)
        elif s[i].isdigit() and radix > int(s[i]):
            sum += pow(radix, i) * int(s[i])
        else:
            return -1
    return sum
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

'''
def checkio(*a):
    try: return int(*a)
    except ValueError: return -1
-----------------------------------
def checkio(str_number,radix):
    try:
        return int(str_number,radix)
    except ValueError:
        return -1
'''

