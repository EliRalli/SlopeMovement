# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:11:19 2020

@author: bofoi
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np


dfData=pd.read_excel('C:/Users/bofoi/PythonScript/Week_05_Slope_Movement_Prism.xlsx', Sheet_name='Sheet 1')
dfData.sort_values(by=['Date'], inplace=True)

#aData= dfData.to_numpy()
#dfData= pd.DataFrame({'Date': aData[:,0],'Ynorth': aData[:,1],'Xeast': aData[:,2],'Zelev': aData[:,3],'SlopeDist': aData[:,4],'Discontinuity': aData[:,5]})
dfDataResampled=dfData.resample('60min',on='Date').mean()
dfDataResampled=dfDataResampled.reset_index()
dfDataResampled=dfDataResampled.fillna(dfDataResampled.interpolate())

DateTime=dfDataResampled['Date']
SlopeDist=dfDataResampled['SlopeDist'].rolling(window=50).mean()

TimeDifference=DateTime.diff()
TimeDifference=TimeDifference.dt.total_seconds().div(60)

counter =len(TimeDifference)-1
while counter >=0:
     if np.isnan(TimeDifference[counter])==True:
        
         TimeDifference=TimeDifference.drop(TimeDifference.index[counter])
         counter=counter-1
     else:
         counter=counter-1
        

plt.plot(DateTime,dfDataResampled['SlopeDist'])
        
plt.plot(DateTime,SlopeDist.shift)

