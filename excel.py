#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
根据部署文档，结合ansible部署应用
'''
import os
import sys
import xlrd
os.chdir('/home/')

if len(sys.argv) < 2:
    print 'please input the path of excel ......'
    sys.exit(1)

def read_excel():
    role_list = ['zookeeper', 'redis', 'pika', 'kafka', 'cassandra']
    zookeeper_play = r'ansible-playbook site.yaml -e "role=%s pl=%s"'
    redis_play = r'ansible-playbook site.yaml -e "role=%s pl=%s"'

    excelfile = xlrd.open_workbook(sys.argv[1])
    sheet =  excelfile.sheet_by_name('python')
    row = [sheet.row_values(i) for i in range(sheet.nrows)]

    for i in range(len(row)):
         if row[i][0] in role_list:
            if row[i][0] == 'zookeeper':
                os.system(zookeeper_play % tuple([row[i][j] for j in range(len(row[i]))]))
            elif row[i][0] == 'redis':
                os.system(redis_play % tuple([row[i][j] for j in range(len(row[i]))]))

if __name__ == '__main__':
    read_excel()