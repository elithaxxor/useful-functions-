import subprocess
import re
import csv
import os
import time
import shutil
from datetime import datetime
from datetime import time


#time = time.time()
# today = datetime.date()
now = datetime.now()
date_2 = datetime(year = 2021, month = 10, day = 7)
# future = (now + date_2)
time_delta = (now - date_2)
total_seconds = time_delta.total_seconds()
minutes = total_seconds/60

print('now', now)
print(now.hour, now.min)
print('date 2', date_2)
#print('future', future)
print('time_delta', time_delta)
print('total_seconds', total_seconds)
print('total minutes', minutes)

print(),print(),print()

print(type(now))
now = str(now)
print(type(now))
print(now)

print(),print(),print()
print('***************')

# 2021-10-05 09:26:33.538829
time_pattern = re.compile(r"[:\d:]")

#time_match = time_pattern.finditer(now)
time_list = time_pattern.findall(now)
min_str = ''
print(time_list)
min_list = time_list[11:13]
print('Min List:', min_list)
min_list = min_list[0:2]
print('min list 2', min_list)
min_str = min_str.join(min_list[0:2])

# min_str.join(time_list[3:5])
print(type(min_str))
print(min_str)


print('********')
for time_l in time_list:
    print(time_l)

for time_p in time_match:
    print(time_p)

print(),print(),print()

with open ('regex_data.txt', 'r') as f: 
    contents = f.read()

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d')
pattern00 = re.compile(r'[a-zA-Z]')               ## to find any charicter a-z or A-Z
pattern01 = re.compile(r'[^a-zA-Z]')       ## to find anything that starts with a-z (( ^ ))
pattern02 = re.compile(r'^\d') ## print anything that does starts with a digit
pattern03 = re.compile(r'^\D') ## print anything that does not start with a digit

match = pattern.finditer(contents)
matches00 = pattern00.finditer(contents)
matches01 = pattern01.finditer(contents)
matches02 = pattern02.finditer(contents)
matches03 = pattern03.finditer(contents)

for match00 in matches01:
    print(match00)

    


# matches = pattern.finditer(phone_number)
# print (pattern)
# print(matches)

# ##### BASIC USAGE #####
# phone_number = '908-392-2030'
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d') ## to find phone number using - or . as deliminter
#
# for match in matches:
# 	print(match)
#
###########################

### loading re from .txt

