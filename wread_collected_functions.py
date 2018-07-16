"""Wread"""

__version__ = '1.0'

import pickle
import csv
from pathlib import Path

def save_pickle(output_file, variable):
    '''Saves variable as pickle file.'''
    with open(output_file, 'wb') as f:
        pickle.dump(variable, f)

def read_pickle(input_file):
    '''Loads pickle file variable'''
    with open(input_file, "rb") as f:
        return pickle.load(f)

def append_txt_line(input_file, content):
    '''Append a line to a text file, creates if doesnt exist.'''
    with open(f'{input_file}.txt', '+a') as out:
        out.write(content + '\n')

def write_2_txt(input_file, content):
    '''Checks if file exists, if not, writes content to new text file.'''
    q = Path(f'{input_file}.txt')
    if q.is_dir() == True:
        with open(f'{input_file}.txt', '+w') as out:
            out.write(content)
    else:
        print(f'Warning: {input_file} already exists')

def csv_list_rows(input_file):
    '''Load csv and output row content as lists in list of rows.'''
    with open(input_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        list1 = []
        for line in readCSV:
            list1.append(line)
        return list1

def get_csv_row(input_file, line_number):
    '''Load csv and output individual row as list.'''
    with open(input_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        list1 = []
        for line in readCSV:
            list1.append(line)
        return list1[line_number]

def csv_append(input_file, input_list):
    '''Appends items in list to new line of csv file. Makes file if does't exist'''
    csvfile = input_file + ".csv"
    with open(csvfile, "+a") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(input_list)
        print(f'{input_list} appended to {input_file}')