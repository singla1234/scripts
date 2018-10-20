import numpy as np
import collections

data_read=[data.strip().lower() for data in open("words")]
data_dict={}
for data in data_read:
    if len(data) not in data_dict.keys():
        data_dict[len(data)]=[]
    data_dict[len(data)].append(data)
print(collections.co)