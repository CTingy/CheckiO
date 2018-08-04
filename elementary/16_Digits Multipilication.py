def checkio(number: int) -> int:
    strn = list(str(number).replace('0',''))
    ans = 1
    for i in range(len(strn)):
        ans *= strn.pop()    
    return ans

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

'''
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res
---------------------------------------------------
def checkio(number):
    total = 1
    for i in str(number).replace('0', '1'):
        total *= int(i)
    return total
'''

