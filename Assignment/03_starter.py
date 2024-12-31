"""
Rush Sanghrajka
DS2500
Starter code for Lecture 3
"""
import csv

FILENAME = "../data/loan_data_2019.csv"

def read_file(filename):
    '''Reads the CSV file and returns
    a list of lists.'''
    data = [] 
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        for row in csvfile:
            data.append(row)
    return data

def main():
    loan_data = read_file(FILENAME)
    print(loan_data)

if __name__ == "__main__":
    main()


