def checkio(data):
    table = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD') ,(100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    s = ''
    for a, b in table:
        s += b * (data//a)
        data = data % a
    return s

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')


def checkio(data):
    symbols = [(1000, "M"), (500, "D"), (100, "C"), (50, "L"),(10, "X"), (5, "V"), (1, "I")]
    roman = []

    for n, c in symbols:
        while data - n >= 0:
            data -= n
            roman.append(c)

    return "".join(roman).replace("CCCC", "CD").replace("XXXX", "XL").replace("IIII", "IV")\
        .replace("DCD", "CM").replace("LXL", "XC").replace("VIV", "IX")
--------------------------------------------------------------------------------
def checkio(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result
-----------------------------------------
defdef  checkiocheckio((datadata))::
        onesones  ==  [["""",,"I""I",,"II""II",,"III""III",,"IV""IV",,"V""V",,"VI""VI",,"VII""VII",,"VIII""VIII",,"IX""IX"]]
        tenstens  ==  [["""",,"X""X",,"XX""XX",,"XXX""XXX",,"XL""XL",,"L""L",,"LX""LX",,"LXX""LXX",,"LXXX""LXXX",,"XC""XC"]]
        hundshunds  ==  [["""",,"C""C",,"CC""CC",,"CCC""CCC",,"CD""CD",,"D""D",,"DC""DC",,"DCC""DCC",,"DCCC""DCCC",,"CM""CM"]]
        thousthous  ==  [["""",,"M""M",,"MM""MM",,"MMM""MMM",,"MMMM""MMMM"]]
        
        tt  ==  thousthous[[datadata  ////  10001000]]
        hh  ==  hundshunds[[datadata  ////  100100  %%  1010]]
        tete  ==  tenstens[[datadata  ////  1010  %%  1010]]
        oo  ==    onesones[[datadata  %%  1010]]
        
        returnreturn  tt++hh++tete++oo
'''