# -*- coding: utf-8 -*-
"""
Created on Sat May 21 21:25:49 2016

@author: π
"""


print("\nThis program was made by PI in April 23, 2016. \n(c) 2016 PI. \
All rights reserved.\n")

#------------------------------------THE COORDINATED UNIVERSAL TIME FROM THE INTERNET------------------------------------
import ntplib, datetime
utctime1 = ntplib.NTPClient()
utc_time = datetime.datetime.utcfromtimestamp(utctime1.request('time.windows.com').tx_time)
print("The UTC from the Internet is: {:}.".format(utc_time))
#------------------------------------END------------------------------------

#------------------------------------LOCAL TIME FROM THE INTERNET------------------------------------
import ntplib
from time import ctime
LOCAL = ntplib.NTPClient()
response = LOCAL.request('time.windows.com', version=3)
local_time = ctime(response.tx_time)
time_offset = response.offset
print("Local time from the Internet is: {:}.".format(local_time))
print("The time offset between your local OS time and the Internet time \
is: {:} seconds.".format(response.offset))
#------------------------------------END------------------------------------

#------------------------------------COMPUTER TIME------------------------------------
import time
ISOTIMEFORMAT = '%Y-%m-%d %X'
computer_time = time.strftime(ISOTIMEFORMAT, time.gmtime( time.time()))
print("Computer time is: {:}.".format(computer_time))
#------------------------------------END------------------------------------

"""
"time.windows.com" is one of NTP servers. Here is a list of NTP servers:
01. time.windows.com
02. time.nist.gov
03. time-c.nist.gov
04. time-nw.nist.gov
05. time.apple.com
06. time3.google.com
07. time1.google.com
08. time2.google.com
09: europe.pool.ntp.org
10. time4.google.com
11. pool.ntp.org
12. 210.72.145.39
"""