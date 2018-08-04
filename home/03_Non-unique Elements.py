def checkio(data: list) -> list:
    new = []
    for d in data:
        if data.count(d) >= 2:
            new.append(d)
            
    return new

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")

'''
return [i for i in data if data.count(i) > 1]
--------------------------------------------
    for item in data:
        if data.count(item) > 1:
            yield item
'''
