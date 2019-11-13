# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 09:19:29 2019

@author: s533488
"""

from bs4 import BeautifulSoup
import requests


getPage = requests.get("Ad World Masters _ Worldwide agency ranking powered by AI.html")
getPage.raise_for_status()
page = BeautifulSoup(getPage.text, 'html.parser')
listOfAgencies = page.find_all('li',class_="views-row")
#print(listOfAgencies)
links = []  
count = 0
for agencies in listOfAgencies:
        try:
            
            count = count + 1
            
            
            
            print(agencies.find('a')['href'])
            #print(agencies.find('h3',class_="title").text)
            
            #count = count + 1;
            #print(count)
        except:
                pass


