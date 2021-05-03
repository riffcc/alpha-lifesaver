#!/usr/bin/python3
# Script to throw a lifesaver at Riff! :)
import csv
with open('ring.csv') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)
