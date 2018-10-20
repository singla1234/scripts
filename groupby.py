from itertools import groupby
func_response = [['2018-08-20', '123', 's', 'ds', 'geearora'], ['2018-08-20', '345', 'fd', 'fd', 'geearora'], ['2018-08-19', '567', 'gfh', 'tt', 'geearora']]
for key,group in groupby(func_response,lambda x:x[4]):
    print(key,group)

