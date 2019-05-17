import  os
#需求：实现文件内容的拷贝
"""
思路：
1.判断原文件是否存在，是否是文件
2.判断目标文件是否存在
3.读取原文件中的内容
4.将读取出来的内容写入到目标文件中
5.关闭文件
"""
def myCopy(srcPath,desPath):
    #判断
    if not os.path.exists(srcPath):
        print("原文件不存在")
        return
    if not os.path.isfile(srcPath):
        print("原文件不是文件，是文件夹")
        return

    #打开文件
    srcFile = open(srcPath,"rb")
    desFile = open(desPath,"wb")

    #获取原文件的大小
    size = os.path.getsize(srcPath)

    #循环读取
    while size > 0:
        #读取
        content = srcFile.read(1024)
        #写入
        desFile.write(content)

        size -= 1024

    #关闭文件
    srcFile.close()
    desFile.close()

myCopy("","")

