#!usr/bin/env python  
# -*- coding:utf-8 _*-
# @author:Torres Ye
# @file':'gloabl.py
# @version:
# @time':'2019/06/28
# @email:yzlview@163.com


"""
达美航空航班价格查询
"""
import requests
import time

s = requests.Session()
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'us.ceair.com',
    'Referer': 'https://tw.ceair.com/hk/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}


def getlogin():
    url = 'https://tw.ceair.com/hk/'
    header1={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
#'Cookie: global_site_flag=en_US; waistAd=true; s_fid=17193BDC73F42878-228A597449D90494; s_cc=true; _ga=GA1.3.1248282327.1561735604; _gid=GA1.3.1604490494.1561735604; userId=614020096366; user_papers=612527199310130016; es_login_user=YE%252FZHENGLIANG; s_sq=%5B%5BB%5D%5D; _Jo0OQK=2C08A99FB6A04158E002B7E6FB9632E4394D465B77CD3F65F31861B88D418015C96403106162C6AAA9A56963335B3F2D3FC514FAA1A1587840F09CD82446958DAB968AEA12936BC96DEA1F53DAFB7DC1CA3456DBA6E53605C499F0A9BB224101663F4B175A75934293AGJ1Z1KQ==; SESSION=227bb8c8-9980-4757-b8d9-0e9e93d61754; es_login_status=non-logined; pt_71d4c6a5=uid=vMuC25chkYhIUPV/XqJJzg&nid=0&vid=FYLLKdg4Dx/74PhxCpkHRw&vn=1&pvn=5&sact=1561735807411&to_flag=0&pl=1SyKCjlf49i6D/ct6Zw3CA*pt*1561735807411; pt_s_71d4c6a5=vt=1561735807411&cad=
'Host':'tw.ceair.com',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
'Cookie': 'global_site_flag=hk_TW; waistAd=true; es_login_status=non-logined; s_fid=4347E9AD65B9AC42-3C3105B455DFBFB2; s_cc=true; _ga=GA1.3.634406524.1561995007; _gid=GA1.3.1449089511.1561995007'
    }
    res = s.get(url, headers=header1, verify=False)
    print(res.cookies)
    url1 = 'https://tw.ceair.com/hk/login.html'
    res1 = s.get(url1, headers=header1, verify=False)
    print(res1.cookies)
    getimg()
    login()


def getimg():
    url = 'https://tw.ceair.com/mub2c/portal/jcaptcha.servlet?2'
    res_img = s.get(url, headers=header, verify=False)
    with open('img.jpg', 'wb') as f:
        f.write(res_img.content)


def login():
    code = input('please input code')
    header = {
        'Host': 'tw.ceair.com',
        'Connection': 'keep-alive',
        # Shakehand: effaa0fe18ede9ea3f1d148d1d6fd88f',
        'Accept': 'application/json,text/javascript,*/*;q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json;charset=utf-8',
        'Referer': 'https://tw.ceair.com/hk/login.html',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Shakehand':'4b82424152795ad77a3c5252eef15db0',
        # 'X-Tingyun-Id':'Lm0q0Wx4_8Y;r=35622021',
        'Shakehand':'c98fafc69c5d8257a330bf6db8638eff',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Cookie':'global_site_flag=hk_TW; waistAd=true; es_login_status=non-logined; s_fid=4347E9AD65B9AC42-3C3105B455DFBFB2; s_cc=true; _ga=GA1.3.634406524.1561995007; _gid=GA1.3.1449089511.1561995007; _gat_UA-84818153-12=1; _gat_UA-84818153-1=1; s_sq=cea-global-prd%3D%2526c.%2526a.%2526activitymap.%2526page%253Dtw.ceair.com%25252Fhk%25252Flogin.html%2526link%253D%2525E7%252599%2525BB%2525E5%252585%2525A5%2526region%253DloginForm%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dtw.ceair.com%25252Fhk%25252Flogin.html%2526pidt%253D1%2526oid%253D%2525E7%252599%2525BB%2525E5%252585%2525A5%2526oidt%253D3%2526ot%253DSUBMIT'
    }
    url = 'https://tw.ceair.com/mub2c/portal/member/loginWithFFP?loginType=0&username=612527199310130016&password=12345679&verifyCode={}&_={}'.format(
        code,'1561993840465')#str(int(time.time()*1000)))
    res = s.get(url, headers=header, verify=False)
    print(res.text)


getlogin()
# print(str(int(time.time()*1000)))
