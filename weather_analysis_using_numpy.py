import numpy as np
import matplotlib.pyplot as pt
import re
import os
data_read=[data.strip().split() for data in open("stations.txt")]
stations={}
for data in data_read:
    if "GSN" in data:
        stations[data[0]]=" ".join(data[4:])
def find_station(s):
    found={code:name for code,name in stations.items() if s in name}
    print(found)
st_list=['USW00022536',"USW00023188","RSM00030710","USW00014922"]

def parsefile(filename):
    return np.genfromtxt(filename,delimiter=dly_delimeter,usecols=dly_usecols,dtype=dly_type,names=dly_names)
dly_delimeter=[11,4,2,4]+[5,1,1,1]*31
dly_usecols=[1,2,3]+[4*i for i in range(1,32)]
dly_type=[np.int32,np.int32,(np.str_,4)]+[np.int32]*31
dly_names=["year","month","obs"]+[str(day) for day in range(1,31+1)]

def unroll(record):
    start_date=np.datetime64("{}-{:02}".format(record["year"],record["month"]))
    dates=np.arange(start_date,start_date+np.timedelta64(1,"M"),np.timedelta64(1,"D"))
    rows=[(date,record[str(i+1)]/10) for i,date in enumerate(dates)]
    return np.array(rows,dtype=[("date","M8[D]"),("value","d")])


def getobs(filename,obs):
    data= np.concatenate([unroll(row) for row in parsefile(filename) if row[2]==obs])
    data["value"][data["value"]==-999.9]=np.nan
    return data


lihue_max=(getobs("USW00022536.dly","TMAX"))
lihue_min=(getobs("USW00022536.dly","TMIN"))

