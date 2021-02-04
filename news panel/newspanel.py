"""
Author: Mingchen Li
Occupation: CITICS Investment
Email:lmc9781@outlook.com
Abstract:
    this is some script that dedicates for news feed for CITICS investment internal useage
"""
import csv
import openpyxl
import os
def write(path='./1.22-23'):
    loc =os.path.join(path, "整理稿.xlsx")
    wb= openpyxl.workbook.workbook()


def newsfeed(path='./1.22-23'):
    """
    生成关键词的dictionary，然后进行文件path 里面的筛选
    :param path:需要筛选的原稿
    :return:
    """

    #dictionary buildup
    investmentEntityKeywordShort = []
    investmentEntityKeywordLong=[]
    investedEntityKeywordShort  =[]
    investedEntityKeywordLong =[]
    historicalKeyword=[]
    keyword = investmentEntityKeywordShort+investedEntityKeywordShort
    with open('筛选词典.csv') as dictcsv:
        dictreader = csv.reader(dictcsv, delimiter = ',')
        for row in dictreader:
            # print(row)
            if(row[-1]=="历史信息关键词"):
                continue
            if(row[0]!=''):
                investmentEntityKeywordShort.append(row[0])
            if(row[1]!=''):
                investmentEntityKeywordLong.append(row[1])
            if (row[2] != ''):
                investedEntityKeywordShort.append(row[2])
            if (row[3] != ''):
                investedEntityKeywordLong.append(row[3])
            if (row[4] != ''):
                historicalKeyword.append(row[4])
    print(investmentEntityKeywordLong)

    #filter
    for basefile in os.listdir(path):
        with open(os.path.join(path, basefile)) as basecsv:
            basereader = csv.reader(basecsv, delimiter = ',')
            basedata = list(basereader)
            for row in basedata:
                for key in keyword:
                    if (key not in row[6]):
                        basedata.remove(row)
                for hist in historicalKeyword:
                    if (hist in row[6]):
                        basedata.remove(row)
            print(len(basedata))




    '''
    base data header顺序如下：
    被投企业名称0
    资讯标题	1
    简要2
    发布日期3
    SENTIMENT4
    来源5	
    详细资讯6	
    BUSI_TYPE7	
    被投企业id8
    '''

newsfeed()
