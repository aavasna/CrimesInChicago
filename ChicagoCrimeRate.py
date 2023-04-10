#Aavasna Rupakheti
import csv
import random
import matplotlib.pyplot as plt
arrest_list=[]
type_list=[]
total_list=[]
location_list=[]
district_list=[]
ward_list=[]
color_list=[]
time_list=[]
update_list=[]
def arrest_graph():
    color_list=["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
       for j in range(2)]
    countF=arrest_list.count("FALSE")
    countT=len(arrest_list)-countF
    num=[countF,countT]
    arrest=["ARREST=TRUE","ARREST=FALSE"]
    plt.bar(arrest,num,color=color_list)
    plt.show()
def location_graph():
    count_location_list=[location_list.count('STREET'),location_list.count('RESIDENCE'),location_list.count('APARTMENT'),location_list.count('SIDEWALK'),location_list.count('OTHER')]
    label_location=['STREET','RESIDENCE','APARTMENT','SIDEWALK','OTHER']
    plt.pie(count_location_list,labels=label_location)
    plt.show()
def type_graph():
    color_list=["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
       for j in range(6)]
    count_type_list=[type_list.count('THEFT'),type_list.count('BATTERY'),type_list.count('CRIMINAL DAMAGE'),type_list.count('ASSAULT'),type_list.count('DECEPTIVE PRACTICE'),type_list.count('OTHER OFFENSE')]
    label_type=['  THEFT  ','  BATTERY  ','  CRIMINAL DAMAGE  ','ASSAULT','DECEPTIVE PRACTICE','OTHER OFFENSE']
    plt.bar(label_type,count_type_list,width=0.3,color=color_list)
    plt.show()
def district_graph():
    xt=[]
    district_int=[int(x) for x in district_list]
    for x in range(len(district_int)):
        if district_int[x] not in xt:
            xt.append(district_int[x]) 
    plt.xticks(xt, rotation=90)
    plt.hist(district_int,bins=25,fc='pink',ec='black')
    plt.ylabel('Freq')
    plt.xlabel('District')
    plt.show()
def ward_graph():
    xt=[]
    ward_int=[int(x) for x in ward_list if x !='']
    for x in range(len(ward_int)):
        if ward_int[x] not in xt:
            xt.append(ward_int[x])
    plt.xticks(xt, rotation=90)
    plt.ylabel('Freq')
    plt.xlabel('Ward')
    plt.hist(ward_int,bins=50,fc='green',ec='black')
    plt.show()
with open('crimes.csv') as file:
    line=csv.reader(file,delimiter=',')
    row_num=0
    for row in line:
        if row_num==0:
            row_num+=1
            continue
        col_num=0
        for col in row:
            if col_num==0:
                time_list.append(col)
                col_num+=1
            elif col_num==1:
                type_list.append(col)
                col_num+=1
            elif col_num==2:
                location_list.append(col)
                col_num+=1
            elif col_num==3:
                arrest_list.append(col)
                col_num+=1
            elif col_num==4:
                district_list.append(col)
                col_num+=1
            elif col_num==5:
                ward_list.append(col)
                col_num+=1
            else:
                update_list.append(col)
                col_num+=1
arrest_graph()
location_graph()
type_graph()
ward_graph()
district_graph()
