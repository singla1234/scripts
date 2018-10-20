import re
data_csv=open(r"C:\Users\gur29899\Downloads\Ex_Files_Python_Gen\Ex_Files_Python_Gen\Exercise Files\Ch1\01_07\names.txt","r")

longest_name=max(((len(name),name) for name in (data.strip() for data in data_csv)))
print(longest_name)