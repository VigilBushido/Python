#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 01:58:30 2017

@author: sergiomac
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
#        print(cols_lst)

        filecontents = f.readlines()
        for line in filecontents:
            foo2 = line.strip('\n').split(',')
            data_lst.append(foo2)

#        print(data_lst[0][:5])
#        print(data_lst[15])
        #row 17 (last row), col 29 (last column) 
        #row 15 is a blank row "", "', ""
        #makes a 17 x 29 Matrix of data
        return cols_lst, data_lst

    
#data_lst: a list previously returned from a call to function get_csv_data()
#cols_lst: a list with the headings of columns to be returned


def get_columns(cols_lst, data_lst, selected_col):
    full_data = cols_lst + data_lst
    a = 30
    columns_lst = [[] for _ in range(a)]

    for j in range(0,30):
        for i in range(0,19):
            columns_lst[j].append(full_data[i][j])

#    for j in range(0,30):
#        for i in range(0,1):
#            columns_lst[j].append(full_data[i][j])
#    
#    for j in range(5,30):
#        for i in range(1,16):
#            columns_lst[j].append(float(full_data[i][j]))

    a = 30
    sel_return_lst = [[] for _ in range(a)]
#    print(len(selected_col))

    for i in range(len(selected_col)):
        for j in range(0,30):
            if selected_col[i] == columns_lst[j][0]:
#                print("selected_col: ",selected_col[i])
#                print("columns_lst: ",columns_lst[j])
                print("\nList: ",selected_col[i])
                print(columns_lst[j],"\n")
                sel_return_lst[j].append(columns_lst[j][0:19])

    return sel_return_lst
        
#get_columns() returns a nested list having as elements a list for each column 
#whose heading is indicated in parameter cols_lst. If cols_lst==[] then the function returns []. 
#If a column heading does not exist in data_lst[0], then that column is ignored.
    

def main():
    bb_file = open('lb-james.csv', 'r')
    cols_lst, data_lst = get_csv_data(bb_file)
    selected_cols_lst = get_columns(cols_lst, data_lst, ["Season", "Age", "PTS"])
    data_lst = cols_lst + data_lst
    
    for args in data_lst[:1]:
        print('{0:<7} {1:^3} {2:^3} {3:^3} {4:^3} {5:^4} {6:^4} {7:^6} {8:^5} {9:^4} {10:^7} {11:^4} {12:^4} {13:^6} {14:^4} {15:^4} {16:^5} {17:^5} {18:^6} {19:^5} {20:^5} {21:^6} {22:^5} {23:^5} {24:^5} {25:^6} {26:^5} {27:^5} {28:^5} {29:^5}'.format(*args))
    for args in data_lst[1:14]:
        print('{0:<6} {1:^3} {2:^3} {3:^3} {4:^3} {5:^4} {6:^4} {7:^6} {8:^5} {9:^4} {10:^7} {11:^4} {12:^4} {13:^6} {14:^4} {15:^4} {16:^5} {17:^5} {18:^6} {19:^5} {20:^5} {21:^6} {22:^5} {23:^5} {24:^5} {25:^6} {26:^5} {27:^5} {28:^5} {29:^5}'.format(*args))
    for args in data_lst[14:16]:
        print('{0:<6} {1:^4} {2:^3} {3:^3} {4:^3} {5:^3} {6:^3} {7:^3} {8:^3} {9:^3} {10:^7} {11:^2} {12:^4} {13:^4} {14:^4} {15:^4} {16:^4} {17:^4} {18:^5} {19:^6} {20:^5} {21:^5} {22:^6} {23:^5} {24:^5} {25:^5} {26:^5} {27:^6} {28:^4} {29:^5}'.format(*args))
    for args in data_lst[16:18]:
        print('{0:<10} {1:^0} {2:^0} {3:^4} {4:^3} {5:^4} {6:^4} {7:^5} {8:^5} {9:^4} {10:^7} {11:^4} {12:^4} {13:^6} {14:^6} {15:^6} {16:^4} {17:^5} {18:^5} {19:^6} {20:^5} {21:^5} {22:^5} {23:^5} {24:^4} {25:^4} {26:^4} {27:^4} {28:^4} {29:^5}'.format(*args))
#        print(data_lst)
        
    print("\n\n")    
    selected_cols_lst = [x for x in selected_cols_lst if x != []]
    print("Selected: ",selected_cols_lst)
    
    
#-------convert to float for processing of graph and calculations-------------#
#    for i in range(1,16): # 15
#       for j in range(5,30): # 29
#            data_lst[i][j] = float(data_lst[i][j])    
#    for i in range(17,19):    
#        for j in range(5,30):
#            data_lst[i][j] = float(data_lst[i][j])  
#    
    a = 30
    columns_lst_graph = [[] for _ in range(a)]
    for j in range(0,30):
        for i in range(0,1):
            columns_lst_graph[j].append(data_lst[i][j])
    
    for j in range(5,30):
        for i in range(1,16):
            columns_lst_graph[j].append(float(data_lst[i][j]))
#-----------------------------------------------------------------------------# 
    print("\n\n") 
    print((columns_lst_graph[20][1:14]))
    print(type(columns_lst_graph[11][1]))

#------------------------PLOT THE DATA & SHOW GRAPH---------------------------#
# =============================================================================
#     import matplotlib.pyplot as plt
#     pylab.title('Lebron Over the Years')
#     plt.figure(1)
#     plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13], columns_lst_graph[11][1:14], 'ro')
#     plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13], columns_lst_graph[11][1:14], 'b-')
#     pylab.xlabel('Years 2003 - 2017 (14 years)')
#     pylab.ylabel('3 pointers range 0-150')
#     plt.axis([0, 14, 0, 150])
#     plt.show()
# 
#     plt.figure(2)
#     pylab.title('Lebron Over the Years')
#     plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13], columns_lst_graph[14][1:14], 'ro')
#     plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13], columns_lst_graph[14][1:14], 'b-')
#     pylab.xlabel('Years 2003 - 2017 (14 years)')
#     pylab.ylabel('2 pointers range 475-700')
#     plt.axis([0, 14, 475, 800])
#     plt.show()
#     
#     plt.figure(3)
#     pylab.title('Lebron Over the Years')
#     plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13], columns_lst_graph[20][1:14], 'ro')
#     plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13], columns_lst_graph[20][1:14], 'b-')
#     pylab.xlabel('Years 2003 - 2017 (14 years)')
#     pylab.ylabel('Free Throw Percentage range 0.5-1.0')
#     plt.axis([0, 14, 0.5, 1.0])
#     plt.show()
# =============================================================================
#-----------------------------------------------------------------------------#
#    bb_lst = get_csv_data(bb_file, [0, 2, 3, 4], “,”)
#    
#    selected_cols_lst = get_columns(james_lst, [“Season”,”Age”,”PTS”])
#    
#    print(bb_lst)
    
    bb_file.close()
    
main()