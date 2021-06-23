#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sergio Munguia 

Programming Languages : Dr. Shihong Huang
Python Assignment 2

"""
import numpy as np
import pandas as pd
#(1-2)
states = []
shows = []
viewers = []
#(3)        
arr = np.genfromtxt('show_results.txt', dtype='str', delimiter=',')
#(4) Raw Data
print(arr)
#(5-9)
states = arr[0::,0::3]
#states = [states[i] for i in sorted(np.unique(states, return_index=True)[1])]
#print(states)
print(states) #Unsorted 
states = np.unique(states) #Remove Duplicates
shows = arr[0::,1::3]
print(shows) #Unsorted
shows = np.unique(shows) #Remove Duplicates
viewers = arr[0::,2::3]
print(viewers)
#redundant print statements
#print(states) #Duplicates Removed
#print(shows) #Duplicates Removed
#print(viewers) #Viewers printed as strings
print("states list is now a: ", type(states)) #NumPy Array
print("shows list is now a: ", type(shows)) #NumPy Array
print("viewers list is now a: ", type(viewers)) #NumPy Array
#(10)
viewers_ints = viewers.astype(int) #Coverted to type int
#print(type(viewers_ints[0,0]))
#(11)
sum_of_viewers = np.sum(viewers_ints) #Sum up viewers
#(12)
print(states)
print(shows)
print(viewers_ints) #viewers list as ints
print(sum_of_viewers)
#(13)
# a. 
show_raw_stats = pd.DataFrame("0",index = shows, columns = states)
print(show_raw_stats)
print('\n')
# b.
show_agg_stats = pd.DataFrame(0 , index = shows, columns=['Max','Min','Totals','Percent'])
print(show_agg_stats)
print('\n')
#(14) Populated show_raw_stats with data from the Original Array injested from txt file            
for i in range (len(arr)):
    for j in range(0, 3):
        if j == 0:
#           print(arr[i][0])
            temp = show_raw_stats.loc[arr[i][1],arr[i][0]]
            newValue = int(temp) + int(arr[i][2])
            show_raw_stats.loc[arr[i][1],arr[i][0]] = newValue
           
#print(arr[0,0]) #state
#print(arr[0,1]) #show name
#print(arr[0,2]) #stats
#
#print(arr[1,0]) #state
#print(arr[1,1]) #show name
#print(arr[1,2]) #stats

#(15) 
max_show_raw_stats = show_raw_stats.max(axis=1)
#print(max_show_raw_stats)
#print('\n')
show_raw_stats['Sum'] = show_raw_stats.sum(axis=1)
#print(show_raw_stats)
#print('\n')
min_show_raw_stats = show_raw_stats.min(axis=1)
#print(min_show_raw_stats)
#print('\n')
show_agg_stats['Totals'] = show_raw_stats['Sum']
show_agg_stats['Max'] = max_show_raw_stats
show_agg_stats['Min'] = min_show_raw_stats
Total = show_agg_stats['Totals'].sum()
#print(Total)
show_agg_stats['Percent'] = show_agg_stats['Totals'] / Total * 100
#(16)
print(show_raw_stats)
print('\n')
print(show_agg_stats)

#Checked Total of Percents == 100% 
#PercentTotal = show_agg_stats['Percent'].sum()
#print(PercentTotal)

#(17) a. b. c. 
print('\n')
print("Game of Thrones has the highest Percent",\
      show_agg_stats.loc['Game of Thrones','Percent'])
print("Orange is the New Black has the lowest Percent",\
      show_agg_stats.loc['Orange is the New Black','Percent'])
print("Gotham is my favorite")
        

