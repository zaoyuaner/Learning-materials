import  csv

#1.从列表写入数据
def writeCsv1(path):
    infoList = [['username', 'password', 'age', 'address'],['zhangsan', 'abc123', '17', 'china'],['lisi', 'aaabbb', '10', 'england']]

    #1.打开文件
    #注意：如果不设置newline，每一行会自动有一个空行
    csvFile = open(path,"w",newline="")

    #2.将文件对象封装成一个可迭代对象
    writer = csv.writer(csvFile)

    #3.写入数据
    for i in range(len(infoList)):
        writer.writerow(infoList[i])

    #4.关闭文件
    csvFile.close()

writeCsv1("file3.csv")

#2.从字典写入文件
def writeCsv2(path):
    dic = {"张三":123,"李四":456,"王麻子":789}
    csvFile = open(path, "w", newline="")
    writer = csv.writer(csvFile)

    for key in dic:
        writer.writerow([key,dic[key]])

    csvFile.close()

#3.简写形式
def writeCsv3(path):
    infoList = [['username', 'password', 'age', 'address'], ['zhangsan', 'abc123', '17', 'china'],
                ['lisi', 'aaabbb', '10', 'england']]
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)

        for rowData in infoList:
            writer.writerow(rowData)