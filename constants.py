from parse_utils import parse_date
import re

# Files
fname_personal = r'C:\Users\gur29899\Downloads\Project-Description\personal_info.csv'
fname_employment = r'C:\Users\gur29899\Downloads\Project-Description\employment.csv'
fname_vehicles = r'C:\Users\gur29899\Downloads\Project-Description\vehicles.csv'
fname_update_status = r'C:\Users\gur29899\Downloads\Project-Description\update_status.csv'
fnames = fname_personal, fname_employment, fname_vehicles, fname_update_status

# Parsers
personal_parser = (str, str, str, str, str)
employment_parser = (str, str, str, str)
vehicle_parser = (str, str, str, int)
update_status_parser = (str, parse_date, parse_date)
parsers = personal_parser, employment_parser, vehicle_parser, update_status_parser

# Named Tuple Names
personal_class_name = 'Personal'
employment_class_name = 'Employment'
vehicle_class_name = 'Vehicle'
update_status_class_name = 'UpdateStatus'
class_names = personal_class_name, employment_class_name, vehicle_class_name, update_status_class_name

#field inclusion/exclusion
personal_fields_compress=[True,True,True,True,True]
employment_fields_compress=[True,True,True,False]
vehicles_fields_compress=[False,True,True,True]
update_status_fields_compress=[False,True,True]
compress_fields=personal_fields_compress,employment_fields_compress,vehicles_fields_compress,update_status_fields_compress
