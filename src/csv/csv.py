
import csv
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