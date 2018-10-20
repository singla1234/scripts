from collections import namedtuple,defaultdict
import re
import csv

veh=r"C:\Users\gur29899\Downloads\Project-Description\vehicles.csv"
emp=r"C:\Users\gur29899\Downloads\Project-Description\employment.csv"
status=r"C:\Users\gur29899\Downloads\Project-Description\update_status.csv"
info=r"C:\Users\gur29899\Downloads\Project-Description\personal_info.csv"
file_list=[veh,emp,status,info]
file_list1=["vehicles","employment","update_status","personal_info"]
#fetch colum names from file
for data,data1 in zip(file_list,file_list1):
    with open(data,"r") as f:
        columns_name=next(f).strip().split(",")
    column_names=[data.replace(" ","_").lower() for data in columns_name]
    #print(data1,column_names)
    data1= namedtuple(data1,column_names)
    print(type(data1._fields))
print(vehicles)
#print(personal_info._fields)















#to check the field types in namedtuple
#print(tickets._fields)
def gen_func():
    with open(tickets_file,"r") as f:
        next(f)
        yield from f
#validate int value
def int_check(value,default=None):
    try:
        return int(value)
    except ValueError:
        return default
#validate str value
def str_check(value,default=None):
    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        else:
            return cleaned
    except :
        return cleaned
#column data parser
columns_parser=(int_check,#'summons_number'
                str_check,#plate_id
                lambda x:str_check(x,default=""),#'registration_state'
                lambda x:str_check(x,default=""),#'plate_type'
                str_check,#'issue_date'
                int_check,#'violation code'
                lambda x:str_check(x,default=""),# 'violation_code'
                str_check,#'vehicle_body_type'#'vehicle_make'
                lambda x:str_check(x,default=""))#'violation_description'
def data_parse(row,default=None):
    fields=row.strip("\n").split(",")
    parsed_data=[(func(value)) for func,value in zip(columns_parser,fields)]
    if all(item is not None for item in parsed_data):
        return tickets(*parsed_data)
    else:
        return default
def data_reader():
    for row in gen_func():
        parsed_data=data_parse(row)
        if parsed_data:
            yield parsed_data
