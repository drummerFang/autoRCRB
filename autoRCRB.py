# -*- coding: utf-8 -*-
import cookielib
import re
import sys
import urllib
import urllib2

cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)

url='http://www.yikeoa.com/accounts/login/?next=/ereport/'
request=urllib2.Request(url)
response=urllib2.urlopen(request)
webpage=response.read()
csrfmiddlewaretoken=re.search("<input type='hidden' name='csrfmiddlewaretoken' value='(\w*)' />", webpage).group(1)

loginUrl='http://www.yikeoa.com/accounts/login/'
username='username'
password='password'
loginParams={'username':username,'password':password,'csrfmiddlewaretoken':csrfmiddlewaretoken}
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36','Host':'www.yikeoa.com','Origin':'http://www.yikeoa.com','Referer':'http://www.yikeoa.com/accounts/login/?next=/ereport/'}
req=urllib2.Request(loginUrl,urllib.urlencode(loginParams),headers=headers)
#html = opener.open(req).read()
resp=urllib2.urlopen(req)
#for index, cookie in enumerate(cj):
        #print '[',index, ']',cookie


planUrl='http://www.yikeoa.com/plan/load/form/add/'
content='日程123'
user=14471
level=3
title='哈哈哈哈'
start_time='2016-06-23 18:18'
rel_pk=''
types=1
planFile=''
files=''
planParams={'content':content,'user':user,'level':level,'title':title,'start_time':start_time,'rel_pk':rel_pk,'types':types,'file':planFile,'files':files,'csrfmiddlewaretoken':csrfmiddlewaretoken}
planHeaders={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36','Host':'www.yikeoa.com','Origin':'http://www.yikeoa.com','Referer':'http://www.yikeoa.com/plan/','X-Requested-With':'XMLHttpRequest'}
req=urllib2.Request(planUrl, urllib.urlencode(planParams),headers=planHeaders)
resp=urllib2.urlopen(req)
print resp.read()






