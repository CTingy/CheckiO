def checkio(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)

if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

'''
return 'Fizz'*(not n%3)+' '*(not n%15)+'Buzz'*(not n%5) or str(n)
-------------------------------------------------------------------
f, s = not number % 3, not number % 5        
return {
        (True, True): "Fizz Buzz",
        (True, False): "Fizz",
        (False, True): "Buzz",
        (False, False): str(number),
    }[(f, s)]
'''
