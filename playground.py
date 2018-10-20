import constants
import parse_utils
from itertools import compress,groupby
import datetime

# # see a sample of what is in each file
# for fname in constants.fnames:
#     print(fname)
#     with open(fname) as f:
#         print(next(f), end='')
#         print(next(f), end='')
#         print(next(f), end='')
#     print()

# for fname in constants.fnames:
#     print(fname)
#     with open(fname) as f:
#         reader = csv.reader(f, delimiter=',', quotechar='"')
#         print(next(reader))
#         print(next(reader))
#     print()

# # header row (field names)
# for fname in constants.fnames:
#     print(fname)
#     reader = parse_utils.csv_parser(fname, include_header=True)
#     print(next(reader), end='\n')
#
# print('\n\n')
#
# # just the data
# for fname in constants.fnames:
#     print(fname)
#     reader = parse_utils.csv_parser(fname)
#     print(next(reader))
#     print(next(reader), end='\n')

# reader = parse_utils.csv_parser(constants.fname_update_status)
# for _ in range(5):
#     record = next(reader)
#     record = [str(record[0]), parse_utils.parse_date(record[1]), parse_utils.parse_date(record[2])]
#     print(record)

#for fname, class_name, parser in zip(constants.fnames, constants.class_names, constants.parsers):
 #   file_iter = parse_utils.iter_file(fname, class_name, parser)
    #print(fname)
  #  for _ in range(3):
   #     print(next(file_iter))
    #print()


#iter_personal = parse_utils.iter_file(constants.fname_personal, constants.personal_class_name, constants.personal_parser)
#iter_vehicles = parse_utils.iter_file(constants.fname_vehicles, constants.vehicle_class_name, constants.vehicle_parser)
iter_update_status = parse_utils.iter_file(constants.fname_update_status, constants.update_status_class_name, constants.update_status_parser)
#iter_employement = parse_utils.iter_file(constants.fname_employment, constants.employment_class_name, constants.employment_parser)


#iter_personal_sorted=sorted(iter_personal,key=lambda x:x[0])
#iter_vehicles_sorted=sorted(iter_vehicles,key=lambda x:x[0])
#iter_update_status_sorted=sorted(iter_update_status,key=lambda x:x[0])
#iter_employement_sorted=sorted(iter_employement,key=lambda x:x[3])

#def compress(data, selectors):
#    # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
#    return (d for d, s in zip(data, selectors) if s)
#for i in range(5):
#    data=next(zip(iter_personal,iter_employement))
#    cmp=compress(data,([1,1,0,0,0],[1,1,0,0]))
#    print(list(cmp))

gen=(parse_utils.iter_combined(constants.fnames,constants.class_names,constants.parsers,constants.compress_fields))
gen_iter=((row.vehicle_make,row.gender) for row in gen)
gen_iter_sorted_1=sorted(gen_iter,key=lambda x:x[0])

#groups=groupby(gen_iter_sorted_1,key=lambda x:x[0])
#groups_list = [(key,len(list(items))) for key, items in groups]
#print((groups_list))

gen_iter_sorted_2=sorted(gen_iter_sorted_1,key=lambda x:x[1])
groups=groupby(gen_iter_sorted_2,key=lambda x:x[0])
groups_list = [(key,len(list(items))) for key, items in groups]
print((groups_list))



#groups = []
#uniquekeys = []
#data = sorted(data, key=keyfunc)
#for k, g in groupby(data, keyfunc):
 #   groups.append(list(g))      # Store group iterator as a list
  #  uniquekeys.append(k)