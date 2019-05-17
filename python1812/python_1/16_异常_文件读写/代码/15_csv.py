
# CSV文件读取

import csv
with open(r'csv\winequality-red.csv') as fp:  #1.打开文件
    #delimiter指定分隔符
    csv_reader = csv.reader(fp,delimiter=';')  #2.获取csv读取器
    header = next(csv_reader) #获取第一行的标题
    print(header)
    for line in csv_reader: #3.遍历所有的行
        print(line)

# 3.2 写入csv

import csv
l1 = [[1,2,3],[4,5,6],[7,8,9]]
#打开文件时，要添加newline=''参数，否则会多一个空行
with open('1.csv','w',newline='') as fp: #1.打开文件
    #delimiter='\t'指定数据分隔符
    csv_writer = csv.writer(fp,delimiter='\t')  #2.获取writer
    for line in l1:
        csv_writer.writerow(line)  #3.写入文件