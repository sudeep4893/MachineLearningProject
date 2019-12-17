# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:12:12 2019

@author: Sudeep
"""
import requests
import time
import os
import sys

# https://en.tutiempo.net/climate/01-2010/ws-421820.html

def retrive_html():
    for year in range(2013, 2019):
        for month in range(1, 13):
            if (month<10):
                url = "https://en.tutiempo.net/climate/0{}-{}/ws-421820.html".format(month, year)
            else:
                url = "https://en.tutiempo.net/climate/{}-{}/ws-421820.html".format(month, year)
                
            texts = requests.get(url)
            text_utf = texts.text.encode('utf-8')
            
            
            if not os.path.exists("Data/Html_data/{}".format(year)):
                os.makedirs("Data/Html_data/{}".format(year))
            with open("Data/Html_data/{}/{}.html".format(year, month), "wb") as output:
                output.write(text_utf)
                
        sys.stdout.flush()
    
                
    
if __name__ == "__main__":
    start_time = time.time()
    retrive_html()
    stop_time = time.time()
    print("Time taken is {}".format(stop_time - start_time))