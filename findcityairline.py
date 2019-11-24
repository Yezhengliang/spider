#!usr/bin/env python  
# -*- coding:utf-8 _*-
# @author:Torres Ye
# @file: findcityairline.py 
# @version:
# @time: 2019/10/02 
# @email:yzlview@163.com
"""
航班搜索

通过输入出发城市exp :西安
    航司 exp：MU
    搜索该航司从该城市出发的所有航班
"""
import requests
from pyquery import PyQuery as pq

f = open("airline.txt", "a+")


class ctrip():
    def __init__(self):
        self.url = "https://flights.ctrip.com/schedule/"
        self.base_url = "https://flights.ctrip.com"
        self.start = None

    def get_headers(self):
        header = {
            "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 77.0.3865.90 Safari / 537.36"
        }
        return header

    def get_index(self):
        """
        获取主页信息
        :return:
        """
        res = requests.get(self.url, headers=self.get_headers(), verify=False)
        if res.status_code == 200:
            self.parse(res.text)
        else:
            return None

    def parse(self, txt):
        """
        主页信息解析
        :param txt:
        :return:
        """
        doc = pq(txt)
        for i in doc(".letter_list a").items():
            # print(i.text())
            # print(self.url[:-1] + i.attr("href"))
            city_name = i.text()
            if city_name[:-2] == self.start:
                print(city_name)
                f.write(city_name + "\n")
                city_url = self.base_url + i.attr("href")
                self.get_city(city_url)
                break

    def get_city(self, city_url):
        """
        获取城市列表
        :param city_url:
        :return:
        """
        res = requests.get(city_url, headers=self.get_headers(), verify=False)
        if res.status_code == 200:
            # print(res.text)
            self.parse_city(res.text)
        else:
            return None

    def parse_city(self, txt):
        """
        解析城市列表
        :param txt:
        :return:
        """
        doc = pq(txt)
        for i in doc("#ulD_Domestic a").items():
            # print(i.text())
            # print(i.attr("href"))
            airline_name = i.text()
            airline_url = i.attr("href")
            print(airline_name)
            f.write(airline_name + "\n")
            self.get_airline(airline_url)

    def get_airline(self, airline_url):
        """
        获取航线列表
        :param airline_url:
        :return:
        """
        res = requests.get(airline_url, headers=self.get_headers(), verify=False)
        if res.status_code == 200:
            self.parse_airline(res)
        else:
            return None

    def parse_airline(self, txt):
        """
        解析航线信息
        :param txt:
        :return:
        """
        doc = pq(txt.text)
        for i in doc("#flt1 tr").items():
            if self.flag and i.find(".flight_logo a").text()[:2] not in self.flag:
                continue
            print("航班号：", i.find(".flight_logo a").text())
            print("起飞时间：", i.find(".depart").text())
            print("到达时间：", i.find(".arrive").text())
            print("经停：", i.find(".stop").text())
            print("周期：", i.find(".weeks .blue").text())
            text = """
                航班号：{}
                起飞时间：{}
                到达时间：{}
                经停：{}
                周期：{}
            """.format(i.find(".flight_logo a").text(), i.find(".depart").text(), i.find(".arrive").text()
                       , i.find(".stop").text(), i.find(".weeks .blue").text())
            f.write(text + "\n")
        if doc(".schedule_page"):
            next_page_url = doc(".schedule_down").attr("href")
            last_page_url = doc(".schedule_page_list a").eq(-1).attr("href")
            if doc(".current").attr("href") == last_page_url:
                return
            else:
                self.get_airline(next_page_url)

    def run(self):
        self.start = input("请输入出发城市:")
        self.flag = input("航司代码:(exp:MU,FM)")
        self.get_index()


a = ctrip()
a.run()
f.close()
