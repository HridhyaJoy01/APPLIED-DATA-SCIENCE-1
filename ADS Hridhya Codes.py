# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:34:09 2023

@author: hridh
"""
#importing pandas and matplotlib 
import pandas as pd
import matplotlib.pyplot as plt

#read and print csv file of us crime rates(1960-2014)
us_crime1=pd.read_csv(r"C:\Users\hridh\Desktop\Assignment\archive (2)\US_Crime_Rates_1960_2014.csv")
print(us_crime1)

#extracting the last 10 rows of each column for clear visualization of recent years 
us_crime=us_crime1[-10:]

#taking the values for plotting
years=us_crime['Year']
rape=us_crime['Forcible_Rape']
murd=us_crime['Murder']
index=range(len(years))

'''plotting bargraph using the values for comparing the count of 
                         crimes:forced rape and murder'''
def plot_bargraph(index,rape,murd):
    fig,a=plt.subplots(figsize=(10,8))
    plt.figure(1)
    bar_width=0.45
    opacity=0.9
    plt.bar(index,rape,bar_width,alpha=opacity,color='y',label='Forced Rape')
    plt.bar([i+bar_width for i in index],murd,bar_width,alpha=opacity,
            color='r',label='Murder')
    plt.title('Forcible rape Vs Murder(2005-2014')
    plt.xlabel('Years')
    plt.ylabel('Count of Crimes')
    plt.xticks([i+bar_width/2 for i in index],years)
    plt.legend()
    plt.show()

#extracting the last 10 rows of vehicle_theft and aggravated assault
v_theft=us_crime['Vehicle_Theft']
assault=us_crime['Aggravated_assault']

'''plotting linegraph using the values for comparing the count of 
                         crimes:vehicle theft and aggrevated assault'''

def plot_linegraph(years,v_theft,assault):
    plt.figure(2,figsize=(12,6))
    plt.plot(years,v_theft,marker='o',label='Vehicle_Theft',color='b')
    plt.plot(years,assault,marker='o',label='Aggravated_assault',color='g')
    plt.title('Vehicle theft Vs Aggravated assault(2005-2014)')
    plt.xlabel('Years')
    plt.ylabel('count')
    plt.legend()
    plt.grid()
    plt.show()
#extracting last 10 rows of property crime for drawing the scatter plot
prop=us_crime['Property']

'''plotting scatter_plot using the data property_crime(2005-2014)'''
def scatter_plot(years,prop):
    plt.figure(3,figsize=(12,8))
    plt.scatter(years,prop,color='r')
    plt.xlabel('Years')
    plt.ylabel('property crime count')
    plt.title('2005-2014 yearly Property crimes')
    plt.grid()
    plt.show()
#calling functions
plot_bargraph(index,rape,murd)
plot_linegraph(years,v_theft,assault)
scatter_plot(years,prop)