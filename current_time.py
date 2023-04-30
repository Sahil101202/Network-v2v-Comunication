
import ntplib
from datetime import datetime, timezone


def print_time():
    c = ntplib.NTPClient()
    response = c.request('it.pool.ntp.org', version=3)
    response.offset
    t = str(datetime.fromtimestamp(response.tx_time, timezone.utc))
    return t[:24]


def time_differece(list):
    hour1 = int(list[0][0:2])
    hour2 = int(list[1][0:2])
    minute1 = int(list[0][3:5])
    minute2 = int(list[1][3:5])
    second1 = float(list[0][6:14])
    second2 = float(list[1][6:14])
    second = 0

    if hour1==hour2:
        if minute1==minute2:
            second = second2 - second1 
        else:
            second = second2 - second1 + 60
    else:
        second = second2 - second1 + 60
        
    return str('%.4f'%second)
 

