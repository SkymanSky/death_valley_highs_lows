import csv
from email import header

filename='data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
print(header_row)
