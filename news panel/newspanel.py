"""
Author: Mingchen Li
Occupation: CITICS Investment
Email:lmc9781@outlook.com
Abstract:
    this is some script that dedicates for news feed for CITICS investment internal useage
"""
import csv

def newsfeed(path='./1.22-23'):
    """
    生成关键词的dictionary，然后进行文件path 里面的筛选
    :param path:需要筛选的原稿
    :return:
    """
    investmentEntityKeyword = {}
    investedEntityKeyword  ={}
    with open('筛选词典.csv') as dictcsv:
        dictreader = csv.reader(dictcsv,)