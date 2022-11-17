#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import libraries
from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
import pandas as pd
from collections import OrderedDict
from datetime import date


# In[188]:


#connect to website
import re
URL = 'https://www.walmart.ca/ce/black-friday/1539158293147?icid=homepage_HP_TopCategory_BlackFriday_WM'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
page = requests.get(URL, headers = headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
import json
for script in soup2(text=re.compile(r'productIds' )):
    data = (script.parent.get_text())
print(data.rfind('productIds'))
print(data.rfind('productsToFetch'))
idlist = data[121429:121684]
#print(idlist)

import ast
idlist = ast.literal_eval(idlist)
idlist = [n.strip() for n in idlist]
print(idlist)



 
    







# In[201]:


#connect to website
URL = 'https://www.walmart.ca/ce/black-friday/1539158293147?icid=homepage_HP_TopCategory_BlackFriday_WM'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
page = requests.get(URL, headers = headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
pages = soup2.find("div", {"class": "css-1dtknsi ed60zyg3"})


#to get number of pages
pagenumbers = []
for option in pages.find_all('option'):
    pagenumbers.append(option['value'])
pages = len(pagenumbers) + 1

#to get all the links of the pages
plist = []
for i in range(pages):
    path = 'https://www.walmart.ca/ce/black-friday/1539158293147?icid=homepage_HP_TopCategory_BlackFriday_WM&p=' + str(i)
    #print(path)
    plist.append(path)
    
#to get the names and links of all the products    
names = []
links = []
for path in plist:
    sub_page = requests.get(path, headers = headers)
    sub_soup1 = BeautifulSoup(page.content, "html.parser")
    sub_soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    body = soup2.find("div", {"class": "css-459x84 e1pmil1x3"})
    for a in body.find_all('a', href=True):
        names.append(a['aria-label'])
        links.append(a['href'])

#final list with names, and links        
#zip function allows us to stitch the lists together
final = list (zip(names, links))

#creating a dataframe 
items_df = pd.DataFrame(final, columns = ['name', 'link'])
items_df.head()


    
    





# In[203]:


#exporting dataframe to excel
items_df.to_excel(r'/Users/alisha/Desktop/walmart_data.xlsx', index=False)


# In[ ]:





# 
