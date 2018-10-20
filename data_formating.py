from itertools import groupby

func_response = [['2018-08-20', '123', 's', 'ds', 'geearora'], ['2018-08-20', '345', 'fd', 'fd', 'geearora'], ['2018-08-19', '567', 'gfh', 'tt', 'geearora'],
                 ['2018-08-20', '123', 's', 'ds', 'geearora1'], ['2018-08-20', '345', 'fd', 'fd', 'geearora1'],['2018-08-19', '567', 'gfh', 'tt', 'geearora1'],
                 ['2018-08-20', '123', 's', 'ds', 'geearora2'], ['2018-08-20', '345', 'fd', 'fd', 'geearora2'],['2018-08-19', '567', 'gfh', 'tt', 'geearora2']]
data_iter=(data for data in func_response)
groups=groupby(data_iter,key=lambda x:x[4])#key_used_person_name
groups_list=[(key,list(data)) for key,data in groups]
print(groups_list)
