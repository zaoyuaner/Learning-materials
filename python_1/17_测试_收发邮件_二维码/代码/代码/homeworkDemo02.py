import  os
#1.读取文件
def loadFile(path):
    f = open(path,"r",encoding="utf-8")
    #返回值为一个列表
    list = f.readlines()
    print(list)

    f.close()

    return list

#2.查询
def search(list,name):
    #作用;保存查找到的人的信息
    subList = []

    #遍历list，获取每一条信息
    for line in list:
       infoList =  line.split(",")
       #查询
       if name == infoList[0]:
           #将查询到的信息保存到subList中
           subList.append(line)

    """
    如果查询到数据，则返回一个有元素的列表
    如果未查询到数据，则返回一个空列表
    """
    return  subList

if __name__ == "__main__":
    path = "kaifanglist.txt"
    #调用读取数据的函数,返回的是所有的信息
    allList = loadFile(path)

    while True:
        name = input("请输入要查找的人的姓名【输入q退出】：")
        if name == "q":
            break
        else:
            #调用查找的函数
            singleList = search(allList,name)

            if singleList:
                #将相关的信息写入到一个新的文件中
                print(name + "果然去开房了")

                #将singleList中的数据写入到一个新的文件中
                #newPath = os.path.join("",name)
                f = open(name + ".txt","w",encoding="utf-8")

                #遍历列表，将查询到的额数据分条写入
                for row in singleList:
                    f.write(row)

                #关闭文件
                f.close()

                print("数据提取成功")
            else:
                print("他是个好男人，好好珍惜吧")