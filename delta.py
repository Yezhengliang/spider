#!usr/bin/env python  
# -*- coding:utf-8 _*-
# @author:Torres Ye
# @file: delta.py
# @version:
# @time: 2018/12/10 
# @email:yzlview@163.com
"""
达美航空
"""
import requests, json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF-8')
sess = requests.Session()
heaser = {
    'Host': 'zh.delta.com',
    'Connection': 'keep-alive',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": 'gzip, deflate, br',
    "Accept-Language": 'zh-CN,zh;q=0.9',
    "Origin": "https://zh.delta.com"
}
url1 = 'https://zh.delta.com/cn/zh'
res1 = sess.get(url1, headers=heaser, verify=False)
print(res1.text)
heaser['Referer'] = url1
url2 = 'https://zh.delta.com/flight-search/search?action=findFlights&tripType=ONE_WAY&priceSchedule=PRICE&originCity=PVG&destinationCity=LAX&departureDate=12/20/2019&departureTime=AT&returnDate=&returnTime=&paxCount=1&searchByCabin=true&cabinFareClass=BE&deltaOnlySearch=False&deltaOnly=off&Go=Find%20Flights&meetingEventCode=&refundableFlightsOnly=False&compareAirport=False&awardTravel=False&datesFlexible=False&flexAirport=False&paxCounts[0]=1'
res2 = sess.get(url2, headers=heaser, verify=False)
print(res2.text)
heaser['Referer'] = url2
heaser['Accept'] = 'application/json'
heaser['X-APP-CHANNEL'] = 'sl-sho'
heaser['Content-Type'] = 'application/json; charset=UTF-8'

url25 = 'https://zh.delta.com/shop/metasearch'
data = {
    "action": "findFlights",
    "tripType": "ONE_WAY",
    "priceSchedule": "PRICE",
    "originCity": "PVG",
    "destinationCity": "LAX",
    "departureDate": "12/20/2019",
    "departureTime": "AT",
    "returnDate": "",
    "returnTime": "",
    "paxCount": "1",
    "searchByCabin": "true",
    "cabinFareClass": "BE",
    "deltaOnlySearch": "false",
    "deltaOnly": "off",
    "Go": "Find Flights",
    "meetingEventCode": "",
    "refundableFlightsOnly": "false",
    "compareAirport": "false",
    "awardTravel": "false",
    "datesFlexible": "false",
    "flexAirport": "false",
    "paxCounts[0]": "1"
}
res25 = sess.post(url25, data=json.dumps(data), headers=heaser, verify=False)
print(res25.text)
res25_txt = json.loads(res25.text)

cacheKey = res25_txt['request']['cacheKey']
heaser['Referer'] = url25
url3 = 'https://zh.delta.com/shop/ow/search'
data = {
    "bestFare": "BE",
    "action": "findFlights",
    "destinationAirportRadius": {
        "unit": "MI",
        "measure": 100
    },
    "deltaOnlySearch": False,
    "meetingEventCode": "",
    "originAirportRadius": {
        "unit": "MI",
        "measure": 100
    },
    "passengers": [
        {
            "type": "ADT",
            "count": 1
        }
    ],
    "searchType": "search",
    "segments": [
        {
            "departureDate": "2019-12-20",
            "destination": "LAX",
            "origin": "PVG"
        }
    ],
    "shopType": "MONEY",
    "tripType": "ONE_WAY",
    "priceType": "Revenue",
    "priceSchedule": "PRICE",
    "awardTravel": False,
    "refundableFlightsOnly": False,
    "nonstopFlightsOnly": False,
    "datesFlexible": False,
    "flexCalendar": False,
    "flexAirport": False,
    "upgradeRequest": False,
    "cacheKey": cacheKey,
    "actionType": "search",
    "vendorDetails": {},
    "initialSearchBy": {
        "fareFamily": "BE",
        "cabinFareClass": None,
        "meetingEventCode": "",
        "refundable": False,
        "flexAirport": False,
        "flexDate": False,
        "flexDaysWeeks": None
    },
    "pageName": "FLIGHT_SEARCH",
    "requestPageNum": "1"
}
res3 = sess.post(url3, data=json.dumps(data), headers=heaser, verify=False)
print(res3.text)
