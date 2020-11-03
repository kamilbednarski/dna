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
    database_reader = csv.reader(database_file, delimiter = ",")
    first_line = next(database_reader)
    number_of_columns = len(first_line)


# Save sequence types from first line of file.
dictionary_size = number_of_columns - 1
dna_sequences = {}
i = 0
while i < dictionary_size:
    dna_sequences[i] = first_line[i + 1]
    i += 1


# Open file with DNA sample. Save sequence for comparison in memeowy.
with open(argv[2]) as dna_file:
    dna_sample = dna_file.read()
    
    
print(dna_sequences)

for key in dna_sequences:
    print(f"key: {dna_sequences[key]}")





#temp_counter = 0
#main_counter = 0
#start_index = 0
#end_index = start_index + len(dna_sequences[i])

#for i in dna_sequences:
 #   if








dna_part = dna_sequences[i]
start_index = 0
end_index = start_index + len(dna_part)
temporary_counter = 0
main_counter = 0


if dna_sample[start_index, end_index] == dna_part:
    





































# Check if input is valid (i.e. if there are 3 arguments); if not, print error message.
# Read the DNA sequence from the file
# Store the information in a string
# Create a dictionary to store the DNA sequences that are to be counted
# Extract the sequences from the database into a list
# Copy the list into a dictionary where the genes are the keys
# Iterate through the DNA sequence
# Add a counter — if repetitions of the values from sequence dictionaries are found, add them up
# Open the database (of people) file
# Iterate through and compare to the sequences dictionary
# If there is a match, print the name of the person; if not, no match.