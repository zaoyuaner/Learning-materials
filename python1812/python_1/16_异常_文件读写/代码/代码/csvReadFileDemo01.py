#C:\Users\Administrator\Desktop\SZ-Python1805\Day15\笔记\text.csv
import  csv


#方式一：三部曲
def readCsv1(path):
    #1.打开文件
    csvFile = open(path,"r")

    #2.将文件对象封装成可迭代对象
    reader= csv.reader(csvFile)

    #3.读取文件内容
    #遍历出来的结果为列表
    for item in reader:
        print(item)

    #4.关闭文件
    csvFile.close()

readCsv1(r"C:\Users\Administrator\Desktop\SZ-Python1805\Day15\笔记\text.csv")

#方式二：简写
def readCsv2(path):
    with open(path,"r") as f:
        reader = csv.reader(f)
        for item in reader:
            print(item)

readCsv2(r"C:\Users\Administrator\Desktop\SZ-Python1805\Day15\笔记\text.csv")
