import os
import re
import csv
import collections as cd
d_dict=cd.defaultdict(list)

def ll():
    with open(r"C:\Users\gur29899\Downloads\17-Grouping\cars_2014.csv","r") as file_read:
        yield from csv.reader(file_read)
    

reader=ll()
print(next(reader))
print(next(reader))
print(next(reader))
print(next(reader))
print(next(reader))
#for data in reader:
 #   print(data)