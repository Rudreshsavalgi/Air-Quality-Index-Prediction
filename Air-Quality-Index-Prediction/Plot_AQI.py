# -*- coding: utf-8 -*-
"""

@author: Rudresh

"""

import pandas as pd
import matplotlib.pyplot as plt

#this function returns the respone variable .i.e., PM2.5 of entire year i.e, 365 values 
def avg_data_year(year=2013):
    avg_365_days = [] #list which contains average PM2.5 of 365 days
    invalid_strings = ['NoData','PwrFail','---','InVld']
    csv_file_path = 'Data/AQI/aqi{}.csv'.format(year)
    for rows in pd.read_csv(csv_file_path,chunksize = 24):
        hour_sum = 0 #sum of 24 hours values
        day_avg = 0 #1 day's average value i.e., sum/24
        data = [] #list which contains 24 hours values
        df = pd.DataFrame(data = rows)
        
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if(type(i) is int or type(i) is float):
                hour_sum += i
            elif(type(i) is str):
                #if(i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld')
                if i not in invalid_strings:
                    hour_sum += float(i)
                    
        day_avg = hour_sum/24
        avg_365_days.append(day_avg)
        
    return avg_365_days

if __name__=="__main__":
    # lst2013=avg_data_year(2013)
    # lst2014=avg_data_year(2014)
    # lst2015=avg_data_year(2015)
    # lst2016=avg_data_year(2016)
    # lst2017=avg_data_year(2017)
    # lst2018=avg_data_year(2018)
    # plt.plot(range(len(lst2013)),lst2013,label="2013 data")
    # plt.plot(range(len(lst2014)),lst2014,label="2014 data")
    # plt.plot(range(len(lst2015)),lst2015,label="2015 data")
    # plt.plot(range(len(lst2016)),lst2016,label="2016 data")
    # plt.xlabel('Day')
    # plt.ylabel('PM 2.5')
    # plt.legend(loc='upper right')
    # plt.show()

    lst_year = []
    for i in range(2013,2019):
        lst_year.append(avg_data_year(i))
    #for visualizing some of the results
    year_lab = 2013
    for i in range(3):
        plt.plot(range(len(lst_year[i])),lst_year[i],label="{} data".format(year_lab))
        year_lab += 1
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()

