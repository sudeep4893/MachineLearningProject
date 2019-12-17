# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:47:15 2019

@author: Sudeep
"""

import pandas as pd
import matplotlib.pyplot as plt

def avg_data(year):
    temp_i = 0
    average = []
    for rows in pd.read_csv("Data/AQI/aqi{}.csv".format(year), chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
            elif type(i) is str:
                if i != "NoData" and i != "PwrFail" and i != "---" and i != "InVld":
                    temp = float(i)
                    add_var = add_var + temp
                    
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    return average
            
if __name__ == "__main__":
    lst2013=avg_data(2013)
    lst2014=avg_data(2014)
    lst2015=avg_data(2015)
    lst2016=avg_data(2016)
    lst2017=avg_data(2017)
    lst2018=avg_data(2018)
    print(len(lst2013))
    print(len(lst2014))
    print(len(lst2015))
    print(len(lst2016))
    print(len(lst2017))
    print(len(lst2018))
    plt.plot(range(0,365),lst2013)
    plt.plot(range(0,364),lst2014)
    plt.plot(range(0,365),lst2015)
    plt.xlabel("Days")
    plt.ylabel("PM2.5")
    plt.legend(loc='upper right')
    plt.show()