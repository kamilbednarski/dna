import csv
import pandas as pd
from sys import argv
from re import search

# Check for unwanted program usage.
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit()


# Open database file. Check number of columns. Save first line of file.
with open(argv[1]) as database_file:
    database_reader = csv.reader(database_file, delimiter=",")
    first_line = next(database_reader)
    number_of_columns = len(first_line)


# Save sequence types from first line of file.
dna_sequences = {}
for i in range(1, len(first_line)):
    dna_sequences[first_line[i]] = 0


# Open file with DNA sample. Save sample for comparison in memory.
with open(argv[2]) as dna_file:
    dna_sample = dna_file.read()


# Count repetitions of each sequence in DNA sample.
counter = 0
# For each sequence:
for sequence in dna_sequences:
    i = 1
    # While found sequence of repetition times 'i'(if methon 'find' result is -1, than its not there):
    while dna_sample.find(sequence * i) != -1:
        counter = i
        i += 1
    # At the end save highest number of repetitions for each sequence:
    dna_sequences[sequence] = counter


# Open database file. Save first line of file.
with open(argv[1]) as database_file:
    database_reader = csv.reader(database_file, delimiter=",")
    line = next(database_reader)
    number_of_columns = len(line)

    # Save sequence types from first line of file.
    temporary_sequences = {}
    for i in range(1, len(line)):
        temporary_sequences[line[i]] = 0

    # Search every row of database file.
    for row in database_reader:
        i = 1
        for sequence in temporary_sequences:
            temporary_sequences[sequence] = int(row[i])
            i += 1
        # If found exact same dictionary, print name and stop the program.
        if dna_sequences == temporary_sequences:
            print(row[0])
            exit()
    print("No match")