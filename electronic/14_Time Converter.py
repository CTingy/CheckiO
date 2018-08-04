from datetime import datetime

def time_converter(time):
    time = time.upper().replace('.', '')
    return datetime.strptime(time, '%I:%M %p').strftime('%H:%M')
    #return time.strftime('%H:%M', time.strptime(now.replace('.', ''), '%I:%M %p'))

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")


'''
    regex = re.compile(r"(\d+):(\d+)")
    hh = int(regex.search(time).group(1))
    mm = int(regex.search(time).group(2))
    if ("p.m." in time) and (hh < 12):
        hh+=12
    elif ("a.m." in time and (hh == 12)):
        hh-=12
    time_string = "{hours:02d}:{mins:02d}".format(hours=hh, mins=mm)
    return time_string 
'''
