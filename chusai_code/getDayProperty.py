import sys, urllib, json
import urllib.request
class getDate:
    def __init__(self):
        pass
    def get_day_type(self, query):
        """
        @query a single date: string eg."20160404"
        @return day_type: 0 workday -1 holiday

        20161001:2 20161002:2 20161003:2 20161004:1
        """

        url = 'http://tool.bitefu.net/jiari/?d=' + query
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        content = resp.read().decode()

        if(content):
            # "0"workday, "1"leave, "2"holiday
            if '0' in content:
                return 0
            else:
                if '1' in content:
                    return 1
                else:
                    return 2

if __name__ == '__main__':
    MyDate = getDate()
    print(MyDate.get_day_type("20180101"))
