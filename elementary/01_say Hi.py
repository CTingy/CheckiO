# 1. on CheckiO your solution should be a function
# 2. the function should return the right answer, not print it.

def say_hi(name: str, age: int) -> str:
    return "Hi. My name is {name} and I'm {age} years old"
    return "Hi. My name is {} and I'm {} years old".format(name, age)
    return "Hi. My name is %s and I'm %d years old" % (name, age)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')





def say_hi(name, age):

    '''Hi. My name is checkio and I'm 5 years old'''

    return say_hi.__doc__.replace('checkio', name).replace('5', str(age))
