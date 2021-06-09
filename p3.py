#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sergio Munguia 

Homework 3 - Problem 3. LeBron Worship

1.) open the file
    bb_file = open('lb-james.csv', 'r')
2.) unload the raw data by calling the function get_csv_data(bb_file) 
2.1) passing in bb_file
    cols_lst, data_lst = get_csv_data(bb_file)
3.) collect cols_lst and data_lst 
    : first row of columns in the csv file table and the data filling in the table
4.) pass in 3 "strings" of into the parameter of get_columns() this was to find 
    : the columns labeled as such and return them in a nested list
4.1)- selected_cols_lst has a column list in each index that was searched for

    selected_cols_lst = get_columns(cols_lst, data_lst, ["Season", "Age", "PTS"])
5.) concatenated the two lists to make 1 data list
    data_lst = cols_lst + data_lst
6.) passed that data list to be printed elegantly using .format for each cell in 
    - the 17 x 29 matrix of data procured
    bb_lst_print(data_lst)
7.) There is a seciton for converting any number to floats, as neceassary for 
    calculations, we needed to create one for the plotting of the data in this case
8.) Imported pylab and then created 3 graphs with red plot points and a blue line
    connecting them, in 3 cases (3P, 2P, FT%) over the span of 14 years
    - using different ranges for each

"""
import pylab

def get_csv_data(bb_file):
    
    with bb_file as f:
        cols_lst = []
        data_lst = []
        heading = f.readline()
        for i in range(1):
            foo1 = heading.strip('\n').strip('\ufeff').split(',')
            cols_lst.append(foo1)

        filecontents = f.readlines()
        for line in filecontents:
            foo2 = line.strip('\n').split(',')
            data_lst.append(foo2)

    return cols_lst, data_lst

    
#data_lst: a list previously returned from a call to function get_csv_data()
#cols_lst: a list with the headings of columns to be returned
def get_columns(cols_lst, data_lst, selected_col):
    
    full_data = cols_lst + data_lst
    #creates an empty list of empty lists big enough for the entire data
    columns_lst = [[] for _ in range(30)]
    for j in range(0,30):
        for i in range(0,19):
            columns_lst[j].append(full_data[i][j])

    #searches for the list selected columns in the parameter of the function
    #returns a nested list of columnslist in a list
    sel_return_lst = []
    for i in range(len(selected_col)):
        for j in range(0,30):
            if selected_col[i] == columns_lst[j][0]:
                print("\nList: ",selected_col[i])
                print(columns_lst[j],"\n")
                sel_return_lst.append(columns_lst[j][0:19])
    return sel_return_lst
        
#get_columns() returns a nested list having as elements a list for each column 
#whose heading is indicated in parameter cols_lst.
    
def bb_lst_print(data_lst):  
    #formats & prints the data evenly and nicely for clean table look of the data for comparision & validation
    for args in data_lst[:1]:
        print('{0:<7} {1:^3} {2:^3} {3:^3} {4:^3} {5:^4} {6:^4} {7:^6} {8:^5} {9:^4} {10:^7} {11:^4} {12:^4} {13:^6} {14:^4} {15:^4} {16:^5} {17:^5} {18:^6} {19:^5} {20:^5} {21:^6} {22:^5} {23:^5} {24:^5} {25:^6} {26:^5} {27:^5} {28:^5} {29:^5}'.format(*args))
    for args in data_lst[1:15]:
        print('{0:<6} {1:^3} {2:^3} {3:^3} {4:^3} {5:^4} {6:^4} {7:^6} {8:^5} {9:^4} {10:^7} {11:^4} {12:^4} {13:^6} {14:^4} {15:^4} {16:^5} {17:^5} {18:^6} {19:^5} {20:^5} {21:^6} {22:^5} {23:^5} {24:^5} {25:^6} {26:^5} {27:^5} {28:^5} {29:^5}'.format(*args))
    for args in data_lst[15:16]:
        print('{0:<5} {1:^6} {2:^1} {3:^3} {4:^3} {5:^3} {6:^3} {7:^5} {8:^5} {9:^4} {10:^7} {11:^4} {12:^4} {13:^5} {14:^3} {15:^3} {16:^5} {17:^5} {18:^6} {19:^5} {20:^5} {21:^6} {22:^5} {23:^5} {24:^5} {25:^6} {26:^5} {27:^5} {28:^5} {29:^5}'.format(*args))
    for args in data_lst[16:19]:
        print('{0:<10} {1:^0} {2:^0} {3:^4} {4:^3} {5:^4} {6:^3} {7:^6} {8:^4} {9:^4} {10:^4} {11:^6} {12:^4} {13:^4} {14:^4} {15:^5} {16:^5} {17:^6} {18:^4} {19:^6} {20:^6} {21:^5} {22:^5} {23:^5} {24:^5} {25:^6} {26:^5} {27:^5} {28:^5} {29:^5}'.format(*args))
    return 0
    
def main():
    bb_file = open('lb-james.csv', 'r')
    cols_lst, data_lst = get_csv_data(bb_file)
    selected_cols_lst = get_columns(cols_lst, data_lst, ["Season", "Age", "PTS"])
    data_lst = cols_lst + data_lst
    bb_lst_print(data_lst)
        
    print("\n")    
    print("Selected Lists: ",selected_cols_lst)

    #removes the empty [] from the nested list of selected columns
#    selected_cols_lst = [x for x in selected_cols_lst if x != []]
#                           or
#    selected_cols_lst = filter(None, selected_cols_lst)
#    selected_cols_lst = list(selected_cols_lst)
     
#----------convert Chart Values float for processing of calculations----------#
#    for i in range(1,16): # 15
#       for j in range(5,30): # 29
#            data_lst[i][j] = float(data_lst[i][j])    
#    for i in range(17,19):    
#        for j in range(5,30):
#            data_lst[i][j] = float(data_lst[i][j])  
#   
#-------convert to float for processing of graph and calculations-------------#
    columns_lst_graph = [[] for _ in range(30)]
    for j in range(0,30):
        for i in range(0,1):
            columns_lst_graph[j].append(data_lst[i][j])
    
    for j in range(5,30):
        for i in range(1,16):
            columns_lst_graph[j].append(float(data_lst[i][j]))
#-----------------------------------------------------------------------------# 
    #Testing of Values
    print("\n\n") 
    print((columns_lst_graph[20][1:16]))
    print(type(columns_lst_graph[20][1]))

#------------------------PLOT THE DATA & SHOW GRAPH---------------------------#
    import matplotlib.pyplot as plt
    pylab.title('Lebron Over the Years')
    plt.figure(1)
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13], columns_lst_graph[11][1:14], 'ro')
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13], columns_lst_graph[11][1:14], 'b-')
    pylab.xlabel('Years 2003 - 2017 (14 years)')
    pylab.ylabel('3 pointers range 0-150')
    plt.axis([0, 14, 0, 150])
    plt.show()

    plt.figure(2)
    pylab.title('Lebron Over the Years')
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13], columns_lst_graph[14][1:14], 'ro')
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13], columns_lst_graph[14][1:14], 'b-')
    pylab.xlabel('Years 2003 - 2017 (14 years)')
    pylab.ylabel('2 pointers range 475-700')
    plt.axis([0, 14, 475, 800])
    plt.show()
    
    plt.figure(3)
    pylab.title('Lebron Over the Years')
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13], columns_lst_graph[20][1:14], 'ro')
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13], columns_lst_graph[20][1:14], 'b-')
    pylab.xlabel('Years 2003 - 2017 (14 years)')
    pylab.ylabel('Free Throw Percentage range 0.5-1.0')
    plt.axis([0, 14, 0.5, 1.0])
    plt.show()
#-----------------------------------------------------------------------------#
    
    bb_file.close()
    
main()