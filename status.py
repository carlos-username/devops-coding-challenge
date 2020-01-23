#!/usr/bin/env python
import requests
from collections import namedtuple
from sys import argv
from termcolor import colored
import json
import time
import datetime
#from datetime import datetime

def CheckStatus(url):
    ServiceStatus = namedtuple('ServiceStatus', ['status_code', 'reason'])
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        reason = response.reason
        if status_code != 200:
            status_code = colored(str(status_code)+" "+reason, 'red')
        else:
            time1 = json.loads(response.content)
            print(time1)
            time_flask = time1['current_time']
            unix_timestamp = datetime.datetime.strptime(time_flask, "%H:%M:%S").timestamp()
            print(unix_timestamp)
            now = datetime.datetime.now()
            print(now.strftime("%H:%M:%S"))
            time_today = datetime.datetime.strptime(now.strftime("%H:%M:%S"),"%H:%M:%S").timestamp()
            print(time_today)
            if time_today == unix_timestamp:
                print("same time")
            if time_today > unix_timestamp:
                print("today time is greater")
            if time_today < unix_timestamp:
                print("time from web service is greater than current one")
    except requests.exceptions.ConnectionError:
        status_code = '000'
        reason = 'ConnectionError'
    website_status = ServiceStatus(status_code, reason)
    return website_status

def main():
    url = argv[1]
    status = CheckStatus(url)
    print("{0:30} {1:10}"
          .format(url, status.status_code))    

if __name__ == '__main__':
    main()
    
