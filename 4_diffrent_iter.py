import csv
from collections import namedtuple,defaultdict
tickets_file="nyc_parking_tickets_extract.csv"#file_name#
#fetch colum names from file
with open(tickets_file,"r") as f:
    columns_name=next(f).strip().split(",")
#lower case and cleaned column names
column_names=[data.replace(" ","_").lower() for data in columns_name]
#print(column_names)
#declare tuple
tickets=namedtuple("tickets",column_names)
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

make_counts=defaultdict(int)
for data in data_reader():
    make_counts[data.vehicle_make]+=1
for cnt,make in sorted(make_counts.items(),key=lambda x:x[1],reverse=True):
    print(make,cnt)