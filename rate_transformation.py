import os
import csv
from collections import defaultdict
keys = ["index"]
d = dict.fromkeys(keys)

sos_d={}
sos_d['index'] = list()
sos_d['utility']=list()
sos_d['most_recent_month']=list()
sos_d['twelve_months_out']=list()
sos_d['months_missing']=list()

os.chdir('C:\\Users\\samantha.ettinger\\Dropbox (Arcadia)\\Arcadia Power Team Folder\\Arcadia Power\\26. Product\\Brokerage Ops SQL\\Sam\\Think Analytics\\SOS Rate Exchange')
csvpath = os.path.join(os.getcwd(),'SOS_Data.csv')
print(csvpath)
sos_list=[]
index_list=[]
utility_list=[]
most_recent_month_list=[]
twelve_months_out_list=[]
months_missing_list=[]
utility_months_missing_list=[]
c=1

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    csv_header = next(csvreader)
    for cs in csvreader:
       index_list.append(cs[0])
       utility_list.append(cs[1])
       most_recent_month_list.append(cs[2])
       twelve_months_out_list.append(cs[3])
       months_missing_list.append(cs[4])

    sos_d['index'].extend(index_list)
    sos_d['utility'].extend(utility_list)
    sos_d['most_recent_month'].extend(most_recent_month_list)
    sos_d['twelve_months_out'].extend(twelve_months_out_list)
    sos_d['months_missing'].extend(months_missing_list)

    # print(sos_d)
    # for k, v in sos_d.items():
    #     print (k,v[0])
    # print(sos_d.get("months_missing")[0])
k=0

if k<38:
    for i in range(0,38):

        for i in range(0,int(sos_d.get("months_missing")[k])):
#     print(i)
            if int(sos_d.get("months_missing")[k])>0:
                sos_d['index'].append( 38 +k)
                sos_d['utility'].append(sos_d.get("utility")[k])
                sos_d['most_recent_month'].append(sos_d.get("most_recent_month")[k])
                sos_d['twelve_months_out'].append(sos_d.get("twelve_months_out")[k])
                sos_d['months_missing'].append(sos_d.get("months_missing")[k])
            else:
                k=k+1
  
    
            k=k+1
            i=i+1 

print(sos_d)
    