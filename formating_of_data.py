from collections import defaultdict,namedtuple

raw_data = [['2018-08-20', '123', 's', 'ds', 'geearora1'], ['2018-08-20', '345', 'fd', 'fd', 'geearora3'], ['2018-08-19', '567', 'gfh', 'tt', 'geearora2']]
column_names=["DATE","ACTIVITY_ID","STATUS","STATUS_REMARK","DE"]
tuple_data=namedtuple("tuple_data",column_names)
print(tuple_data._fields)
for data in raw_data:
    tuple_data(*data)
print(tuple_data.ACTIVITY_ID)




