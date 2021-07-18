#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 1 Top Movies & Actors 

Sergio Munguia

"""
import csv

def read_table1(a_file, a_dict):
    infile = open(a_file, 'r', encoding='utf8')
    reader = csv.reader(infile, delimiter = ',')
    header = next(infile)
    print(header)


    for row in reader:
        directors = row[2]
        print(directors)

#     
     input_file = csv.DictReader(open(a_file))
     for row in input_file:
         rank = int(row["Rank"])
         title = str(row["Title"])
         year = int(row["Year"])
         rating = float(row["IMDb Rating"])
         print(rank, title, year, rating)
# =============================================================================
    
def read_table2(a_file, a_dict):
    infile = open('a_file', 'r', encoding='utf8')
    reader = csv.reader(infile, delimiter = ',')
    header = next(infile)
    print(header)
        
                            
# =============================================================================
#     data_reader = csv.reader(a_file, delimiter = ',')
#     
#     for row in data_reader:
#         if row[0].isdigit():
#             symbol_str = row[1]
#             a_dict[symbol_str] = row[1:3]
#             
#     print(a_dict)
# =============================================================================
    


def displayDirectors_with_MostTopRatedMovies():
    infile = open('imdb-top-rated.csv', 'r', encoding='utf8')
    reader = csv.reader(infile, delimiter = ',')
    for row in reader: 
        print(row)
#        print(row[0])
    
    infile.close()
    
def displayDirectors_with_MostGrossedMovies():
    pass
    
def displayTopActors_in_MostTopRatedMovies():
    pass
    
def displayBoxOfficePayout():
    pass

def main():
    word_count_dict= {}
    Top_rated = open(')

top_directors = {}
read_table1('imdb-top-casts.csv', top_directors)
#read_table2('imdb-top-rated.csv')