from datetime import datetime

def date_time(time: str) -> str:
    t = datetime.strptime(time, "%d.%m.%Y %H:%M")
    h = '' if t.strftime('%-H') == '1' else 's'
    m = '' if t.strftime('%-M') == '1' else 's'
    return t.strftime('%-d %B %Y year %-H hour{} %-M minute{}'.format(h, m))

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"

'''
from datetime import datetime

def checkio(time):
    dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
    hour = 'hour' if dt.hour == 1 else 'hours'    
    minute = 'minute' if dt.minute == 1 else 'minutes'
    return dt.strftime(f'%-d %B %Y year %-H {hour} %-M {minute}')    
----------------------------------------------------------------
    dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
    p = lambda attr: attr + 's' * (getattr(dt, attr) != 1)
    return dt.strftime(f'%-d %B %Y year %-H {p("hour")} %-M {p("minute")}')
-------------------------------------------------------------------
def date_time(time):
    t = datetime.strptime(time, '%d.%m.%Y %H:%M')
    y, m, d, h, mi =  t.year, datetime.strftime(t, '%B'), t.day, t.hour, t.minute
    suffix = lambda n: 's' if n != 1 else ''

    return f'{d} {m} {y} year {h} hour{suffix(h)} {mi} minute{suffix(mi)}'
--------------------------------------------------------------------
def date_time(date):
    output_fmt = '%-d %B %Y year %-H hour{h} %-M minute{m}'
    date = datetime.strptime(date, '%d.%m.%Y %H:%M')
    return datetime.strftime(
        date,
        output_fmt.format(
            h=('s', '')[date.hour == 1], 
            m=('s', '')[date.minute == 1]
            )
        )
-----------------------------------------------
def date_time(time):
    dt = datetime.datetime.strptime(time, "%d.%m.%Y %H:%M")
    s = '' if dt.hour == 1 or dt.minute == 1 else 's'
    return dt.strftime(f"{dt.day} %B %Y year {dt.hour} hour{s} {dt.minute} minute{s}")        
'''


