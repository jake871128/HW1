#!/usr/bin/env python
# coding: utf-8

# In[37]:


# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106060012.csv'
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

#先把WDSD這行裡面值為-99和-999的濾掉
data = list(filter(lambda item: item['WDSD'] != '-99.000', data))
data = list(filter(lambda item: item['WDSD'] != '-999.000', data))

#設一個list存answer
ans_list=[]

#挑出WDSD=C0A880
target_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))
if len(target_data)==0 or len(target_data)==1:
    tmp_list=['C0A880','None']
else:
    min_val = min(target_data,key=lambda item: item['WDSD'])
    max_val = max(target_data,key=lambda item: item['WDSD'])
    tmp_list=['C0A880',abs(float(max_val['WDSD'])-float(min_val['WDSD']))]
ans_list.append(tmp_list)

#挑出WDSD=C0F9A0
target_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
if len(target_data)==0 or len(target_data)==1:
    tmp_list=['C0F9A0','None']
else:
    min_val = min(target_data,key=lambda item: item['WDSD'])
    max_val = max(target_data,key=lambda item: item['WDSD'])
    tmp_list=['C0F9A0',abs(float(max_val['WDSD'])-float(min_val['WDSD']))]
ans_list.append(tmp_list)

#挑出WDSD=C0G640
target_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))
if len(target_data)==0 or len(target_data)==1:
    tmp_list=['C0G640','None']
else:
    min_val = min(target_data,key=lambda item: item['WDSD'])
    max_val = max(target_data,key=lambda item: item['WDSD'])
    tmp_list=['C0G640',abs(float(max_val['WDSD'])-float(min_val['WDSD']))]
ans_list.append(tmp_list)


#挑出WDSD=C0R190
target_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))
if len(target_data)==0 or len(target_data)==1:
    tmp_list=['C0R190','None']
else:
    min_val = min(target_data,key=lambda item: item['WDSD'])
    max_val = max(target_data,key=lambda item: item['WDSD'])
    tmp_list=['C0R190',abs(float(max_val['WDSD'])-float(min_val['WDSD']))]
ans_list.append(tmp_list)


#挑出WDSD=C0X260.
target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
if len(target_data)==0 or len(target_data)==1:
    tmp_list=['C0X260','None']
else:
    min_val = min(target_data,key=lambda item: item['WDSD'])
    max_val = max(target_data,key=lambda item: item['WDSD'])
    tmp_list=['C0X260',abs(float(max_val['WDSD'])-float(min_val['WDSD']))]
ans_list.append(tmp_list)


#=======================================

# Part. 4
#=======================================
# Print result

print(ans_list)
#========================================


# In[ ]:




