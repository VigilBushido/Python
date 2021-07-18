#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 1 Top Movies & Actors 

Sergio Munguia

"""
import csv
import string

top_5_directors = []

def add_word(word, a_dict):
    if word in a_dict: 
        a_dict[word] += 1
    else:
        a_dict[word] = 1

def pretty_print(a_dict):
    value_key_list=[]
    for key,val in a_dict.items():
        value_key_list.append((val,key))
        
    value_key_list.sort(reverse=True)
    
    print('{:11s}{:11s}'.format('Word', 'Count'))
    print('_'*21)
    for val, key in value_key_list:
        print('{:12s} {:<3d}'.format(key,val))
    
    top_5 = value_key_list[0:5]
    print(top_5)


def process_line(line, a_dict):
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        
        if word != ",":
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            add_word(word, a_dict)
            

def read_table1(a_file, a_dict):
    infile = open(a_file, 'r', encoding='utf8')
    reader = csv.reader(infile, delimiter = ',')
    header = next(infile)
    print(header)

    for row in reader:
        directors = row[2]
        process_line(directors, a_dict)
    
    print('Leghth of the dictionary:', len(a_dict))
    pretty_print(a_dict)
# =============================================================================
    
def read_table2(a_file, a_dict):
    infile = open('a_file', 'r', encoding='utf8')
    reader = csv.reader(infile, delimiter = ',')
    header = next(infile)
    print(header)    


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
    top_directors = {}
    read_table1('imdb-top-casts.csv', top_directors)
    
main()

#read_table2('imdb-top-rated.csv')