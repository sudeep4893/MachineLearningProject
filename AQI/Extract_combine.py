# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:05:12 2019

@author: Sudeep
"""

import os
import sys
import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup

from Plot_AQI import avg_data

def met_data(month, year):
    
    file_html = open('Data/Html_data/{}/{}.html'.format(year, month), 'rb')
    plain_text = file_html.read()
    
    tempD = []
    finalD = []
    
    soup = BeautifulSoup(plain_text, 'lxml')
    for table in soup.find_all('table', {'class': 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)
                
    rows = len(tempD)/15
    
    for times in range(round(rows)):
        newTempD = []
        for i in range(15):
            newTempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newTempD)
    
    length = len(finalD)
    
    finalD.pop(length - 1)
    finalD.pop(0)
    
    for a in range(len(finalD)):
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)

    return finalD


if __name__ == "__main__":
    if not os.path.exists("Data/Real-Data"):
        os.makedirs("Data/Real-Data")
        
    for year in range(2013, 2017):
        final_data = []
        with open('Data/Real-Data/real_' + str(year) + '.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
            
        for month in range(1, 13):
            temp = met_data(month, year)
            final_data = final_data + temp
            
        pm = getattr(sys.modules[__name__], 'avg_data')()
        
        if len(pm) == 364:
            pm.insert(364, '-')
            
        for i in range(len(final_data)-1):
            final_data[i].insert(8, pm[i])
            
        
            
        

    