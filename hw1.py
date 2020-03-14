# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '106061271.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))


# Retrive ten data points from the beginning.

# target_data = data[:10]

j = 0
k = len(data)
data1 = []
target_data = []

for i in range(k):
    if (data[i]['PRES'] != '-99.000' and data[i]['PRES'] != '-999.000'):
        data1.append(data[i])

k = len(data1)
sum = 0
mean = 0

################################################

for i in range(k):
    if (data1[i]['station_id'] == 'C0A880'):
        sum = sum + eval(data1[i]['PRES'])
        j = j + 1
if (j == 0):
    target_data.append(['C0A880', 'None'])
else:
    mean = sum/j
    target_data.append(['C0A880', round(mean, 2)])

sum = 0
j = 0
################################################

for i in range(k):
    if (data1[i]['station_id'] == 'C0F9A0'):
        sum = sum + eval(data1[i]['PRES'])
        j = j + 1
if (j == 0):
    target_data.append(['C0F9A0', 'None'])
else:
    mean = sum/j
    target_data.append(['C0F9A0', round(mean, 2)])

sum = 0
j = 0
################################################

for i in range(k):
    if (data1[i]['station_id'] == 'C0G640'):
        sum = sum + eval(data1[i]['PRES'])
        j = j + 1
if (j == 0):
    target_data.append(['C0G640', 'None'])
else:
    mean = sum/j
    target_data.append(['C0G640', round(mean, 2)])

sum = 0
j = 0
################################################

for i in range(k):
    if (data1[i]['station_id'] == 'C0R190'):
        sum = sum + eval(data1[i]['PRES'])
        j = j + 1
if (j == 0):
    target_data.append(['C0R190', 'None'])
else:
    mean = sum/j
    target_data.append(['C0R190', round(mean, 2)])

sum = 0
j = 0
################################################

for i in range(k):
    if (data1[i]['station_id'] == 'C0X260'):
        sum = sum + eval(data1[i]['PRES'])
        j = j + 1
if (j == 0):
    target_data.append(['C0X260', 'None'])
else:
    mean = sum/j
    target_data.append(['C0X260', round(mean, 2)])

sum = 0
j = 0

#=======================================


# Part. 4

#=======================================

# Print result

print(target_data)

#========================================