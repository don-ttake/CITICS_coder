"""
Author: Mingchen Li
Occupation: CITICS Investment
Email:lmc9781@outlook.com
Abstract:
    this is some script that dedicates for news feed for comparing two csv sheets based on investment entities
"""

import csv
import os

def equalPrice(a, b):
    if(a==0 and b =='-'):
        return True
    if(a==0 and b =='-'):
        return True
    return(str(a)==str(b))


def buildAB(path='./'):
    loc = os.path.join(path, "对比A.csv")
    Anames =[]
    Aprices = []
    with open(loc) as csv_file:
        csv_reader = csv.reader(csv_file)
        linecountA = 0
        for row in csv_reader:
            Anames.append(row[0])
            Aprices.append(row[1])
            linecountA +=1

    loc  = os.path.join(path, "对比B.csv")
    Bnames =[]
    Bprices = []
    with open(loc) as csv_file:
        csv_reader = csv.reader(csv_file)
        linecountB = 0
        for row in csv_reader:
            Bnames.append(row[0])
            Bprices.append(row[1])
            linecountB +=1
    print(linecountB)
    found_counter = 0
    print(type(Aprices[4]))
    for i in range(0,linecountA):
        for j in range(0, linecountB):
            if ((Anames[i] in Bnames[j]) or (Bnames[j] in Anames[i])):
                print("发现对应名字", Anames[i], Bnames[j])
                print("测试投资金额", Aprices[i]==Bprices[j],Aprices[i], Bprices[j])
                found_counter+=1

    print("对应数有" ,found_counter, " A 表有", linecountA, " B 表有", linecountB)
buildAB()
