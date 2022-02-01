

from datetime import datetime



# Create Date ==================================================================
# Write a function that creates and returns a new datetime given the components

def create_date(month, day, year):
    ...
print(create_date(4, 20, 2021)) # 2021-04-20 00:00:00


# Get Year =====================================================================
# Write a function that returns the year of a given datetime

def get_year(dt):
    ...
print(get_year(datetime(2021, 4, 20))) # 2021


# Parse Date ===================================================================
# Write a function that converts the given string into a datetime

def parse_date(date_string):
    ...
print(parse_date('April 20, 2021')) # 2021-04-20 00:00:00


# Parse Datetime ===============================================================
# Write a function that converts a given string into a datetime
def parse_datetime(date_string):
    ...
print(parse_datetime('April 20, 2021 09:30 AM')) # 2021-04-20 09:30:00

# Format Datetime ==============================================================
# Write a function that converts the given datetime into a string
def format_datetime(dt):
    ...
print(format_datetime(datetime(2021, 4, 20, 9, 30)))
