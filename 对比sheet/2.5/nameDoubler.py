"""
Author: Mingchen Li
Occupation: CITICS Investment
Email:lmc9781@outlook.com
Abstract:
    this is some script that dedicates for news feed for comparing two csv sheets based on investment entities
"""

import csv
import os
import difflib
from openpyxl import Workbook

def equalPrice(a, b):
    """
    自己定义的equal price，主要还是得input的时候strip一下空格才会准， 原稿中0.00和‘-’的问题目前只想到这个方法做
    :param a:
    :param b:
    :return:
    """
    if (a == '0.00' and b == '-'):
        return True
    if (b == '0.00' and a == '-'):
        return True
    return (str(a) == str(b))



def longestSubstringFinder(string1, string2):
    """
    找出最长mutual substring， 中英文都好使， 就是得AB互换run一下
    :param string1:
    :param string2:
    :return:
    """
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    if (answer in ['上海', '金石', '科技', '生物', '股份', '公司','广州','江苏','新能源']):
        return ""
    return answer
# def similarStrings(string1, string2):
#     return ((string1 in string2) or (string2 in string1) or len(longestSubstringFinder(string1, string2)) > 1 or len(longestSubstringFinder(string2, string1)) > 1))


def InvestmentDictionaryBuilder(filename, path = './'):
    """
    用中证投底稿的顺序做一个名称的dictionary， 找到库务那边对应的然后写成一起
    :param path: 中证和库务对应的
    :return: 写出一个叫filename的excel
    """
    loc = os.path.join(path, "中证底稿.csv")
    Anames = []
    Aprices = []
    with open(loc) as csv_file:
        csv_reader = csv.reader(csv_file)
        linecountA = 0
        for row in csv_reader:
            Anames.append(row[0].strip())
            Aprices.append(row[1].strip())
            linecountA += 1
    loc = os.path.join(path, "库务底稿.csv")
    Bnames = []
    Bprices = []
    with open(loc) as csv_file:
        csv_reader = csv.reader(csv_file)
        linecountB = 0
        for row in csv_reader:
            Bnames.append(row[0].strip())
            Bprices.append(row[1].strip())
            linecountB += 1
    AnameTuples = []
    for i in range(0, linecountB):
        stupidCounter = 0
        for j in range(0, linecountA):
            if ((Anames[j] in Bnames[i]) or
                    (Bnames[i] in Anames[j]) or
                    len(longestSubstringFinder(Anames[j], Bnames[i])) > 1 or
                    len(longestSubstringFinder(Bnames[i], Anames[j])) > 1):
                AnameTuples.append([Anames[j], Bnames[i]])
                stupidCounter+=1
                continue

            elif(j+1==linecountB ):
                AnameTuples.append(['',Bnames[i]])
    poladWriter([AnameTuples], filename)

def poladWriter(ploadList, filename):
    dest = filename + '.xlsx'
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.append(['(A)中证表企业名称',  '(B)库务表企业名称'])
    for pload in ploadList:
        for row in pload:
            worksheet.append(row)
        worksheet.append(['', '', '', ''])
    workbook.save(dest)

InvestmentDictionaryBuilder('kuwu')

