#!/usr/bin/python3
# Script to throw a lifesaver at Riff! :)
import csv
with open('ring.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
