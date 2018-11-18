#!usr/bin/env python  
# -*- coding:utf-8 _*-
# @author:Torres Ye
# @file: AAairlines.py 
# @version:
# @time: 2018/11/18 
# @email:yzlview@163.com
import requests, re

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
sess = requests.Session()
url1 = 'https://www.aa.com/intl/cn/index.jsp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.1'
                  '02 Safari/537.36',
}
res = sess.get(url1, headers=headers)
# print(res.cookies.get('JSESSIONID'))
data1 = {
    'REFRESH': '0',
    'DIRECT_NON_STOP': False,
    'SEVEN_DAY_SEARCH': True,
    'TRIP_FLOW': 'YES',
    'SO_SITE_UI_FLIFO_DISP_DOT': True,
    'SO_SITE_AIRLINE_LOC_WAIT': '30000',
    'SO_SITE_ALLOW_PROMO': False,
    'SO_SITE_ALLOW_LSA_INDICATOR': True,
    'SO_SITE_DISPLAY_NBR_OF_LSA': True,
    'SO_SITE_ALLOW_FLIFO_OTP_INFO': True,
    'SO_SITE_REFARE_TO_1TICKET': False,
    'BOOKING_FLOW': 'REVENUE',
    'DATE_RANGE_VALUE_1': '2',
    'DATE_RANGE_QUALIFIER_1': 'C',
    'DATE_RANGE_VALUE_2': '2',
    'DATE_RANGE_QUALIFIER_2': 'C',
    'SITE': 'BFJOANEW',
    'EXTERNAL_ID': 'CHINA',
    'LANGUAGE': 'CN',
    'SO_SITE_POINT_OF_SALE': 'BJS',
    'SO_SITE_MARKET_ID': 'CHINA',
    'MATRIX_CALENDAR': False,
    'SO_SITE_MIN_AVAIL_DATE_SPAN': 'H4',
    'SO_SITE_MINIMAL_TIME': 'H4',
    'SO_SITE_CURRENCY_FORMAT_JAVA': '0',
    'SO_SITE_CURRENCY_FORMAT': '%d',
    'SO_SITE_ALLOW_AUTOMATED_TKT': True,
    'SO_SITE_MOP_PAY_LATER': False,
    'SO_SITE_PREFERRED_CARRIER': 'AAYY',
    'SO_SITE_OFFICE_ID': 'BJSAA18AB',
    'SO_SITE_AMADEUS_OFFICE_ID': 'BJSAA18AB',
    'EMBEDDED_TRANSACTION': 'FlexPricerAvailability',
    'PRICING_TYPE': 'O',
    'FP_ERT_ACTIVATED': False,
    'SO_SITE_NAVIGATION_ENABLED': True,
    'B_LOCATION_1': 'LAX',
    'E_LOCATION_1': 'PVG',
    'B_LOCATION_2': 'PVG',
    'E_LOCATION_2': 'LAX',
    'B_DATE_1': '201811180000',
    'B_ANY_TIME_1': True,
    'B_DATE_2': '201811250000',
    'B_ANY_TIME_2': True,
    'TRIP_TYPE': 'R',
    'COMMERCIAL_FARE_FAMILY_1': 'LOWEST',
    'TRAVELLER_TYPE_1': 'ADT',
    'DISPLAY_TYPE': '2',
    'ARRANGE_BY': 'ND',
}
url2 = 'https://bookaa.amadeus.com/plnext/AADX/Override.action'
headers['Accept-Encoding'] = 'gzip, deflate, br'
headers['Accept-Language'] = 'zh-CN,zh;q=0.9'

res2 = sess.post(url2, data=data1, headers=headers)
# print(res2.text)
sessid = re.findall('sessionId = "(.*?)";', res2.text, re.S)
# print(sessid)
url3 = 'https://bookaa.amadeus.com/plnext/AADX/FlexPricerAvailability.action;jsessionid={}'.format(sessid[0])
data2 = {
    'MATRIX_CALENDAR': False,
    'SO_SITE_DISPLAY_NBR_OF_LSA': True,
    'B_LOCATION_2': 'PVG',
    'B_LOCATION_1': 'LAX',
    'DIRECT_NON_STOP': False,
    'DATE_RANGE_VALUE_2': '2',
    'DATE_RANGE_VALUE_1': '2',
    'E_LOCATION_2': 'LAX',
    'SO_SITE_ALLOW_AUTOMATED_TKT': True,
    'E_LOCATION_1': 'PVG',
    'TRAVELLER_TYPE_1': 'ADT',
    'SO_SITE_OFFICE_ID': 'BJSAA18AB',
    'SO_SITE_ALLOW_FLIFO_OTP_INFO': True,
    'DATE_RANGE_QUALIFIER_1': 'C',
    'FP_ERT_ACTIVATED': False,
    'SO_SITE_POINT_OF_SALE': 'BJS',
    'DATE_RANGE_QUALIFIER_2': 'C',
    'B_DATE_1': '201811180000',
    'B_DATE_2': '201811250000',
    'B_ANY_TIME_1': True,
    'SO_SITE_MINIMAL_TIME': 'H4',
    'SO_SITE_PREFERRED_CARRIER': 'AAYY',
    'ARRANGE_BY': 'ND',
    'SO_SITE_MARKET_ID': 'CHINA',
    'SO_SITE_CURRENCY_FORMAT': '%d',
    'SO_SITE_ALLOW_PROMO': False,
    'B_ANY_TIME_2': True,
    'SO_SITE_MOP_PAY_LATER': False,
    'BOOKING_FLOW': 'REVENUE',
    'REFRESH': '0',
    'SITE': 'BFJOANEW',
    'COUNTRY_SITE': 'GB',
    'DISPLAY_TYPE': '2',
    'SO_SITE_AMADEUS_OFFICE_ID': 'BJSAA18AB',
    'SEVEN_DAY_SEARCH': True,
    'TRIP_FLOW': 'YES',
    'SO_SITE_NAVIGATION_ENABLED': True,
    'TRIP_TYPE': 'R',
    'EXTERNAL_ID': 'CHINA',
    'SO_SITE_AIRLINE_LOC_WAIT': '30000',
    'COMMERCIAL_FARE_FAMILY_1': 'LOWEST',
    'PRICING_TYPE': 'O',
    'SO_SITE_ALLOW_LSA_INDICATOR': True,
    'LANGUAGE': 'CN',
    'SO_SITE_UI_FLIFO_DISP_DOT': True,
    'SO_SITE_REFARE_TO_1TICKET': False,
    'SO_SITE_MIN_AVAIL_DATE_SPAN': 'H4',
    'SO_SITE_CURRENCY_FORMAT_JAVA': '0',
    'isOverrideAction': True,
    'context': True,
    'DATA_TYPE': 'json',
    'EMBEDDED_TRANSACTION': 'FlexPricerAvailability',
}
res3 = sess.post(url3, data=data2, headers=headers)
print(res3.text)
