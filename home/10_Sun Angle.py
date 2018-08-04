def sun_angle(time):
    time = int(time.split(':')[0]) + int(time.split(':')[1])/60
    if time > 18 or time < 6:
        return "I don't see the sun!"
    return (time-6) / 12 * 180

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"

'''
def sun_angle(time):
    h, m = list(map(int, time.split(':')))
    angle = 15 * h + m / 4 - 90
    return angle if 0 <= angle <= 180 else "I don't see the sun!"
--------------------------------------------------------
from datetime import datetime
from scipy.interpolate import interp1d

solutions = {'06:00': 0, '12:00': 90, '18:00': 180}
stamp = lambda time: datetime.strptime(time, '%H:%M').timestamp()
line = interp1d([*map(stamp, solutions)], [*solutions.values()])

def sun_angle(time):
    try: return line(stamp(time))[()]
    except ValueError: return "I don't see the sun!"
-----------------------------------------------------------
def sun_angle(time):
    t = int(time[:2]) * 15 + int(time[3:]) / 4 - 90
    return t if 0 <= t <= 180 else "I don't see the sun!"
'''


