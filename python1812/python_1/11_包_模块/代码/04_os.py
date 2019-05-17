# os : operate system 操作系统

import os
print(os.name)
#nt----->Windows(windows内核)   posix------>Linux,Mac os(unix内核)

# 打印当前系统的环境变量
print(os.environ)

# 获取指定项环境变量的值. 多个环境值之间以分号隔开
print(os.environ.get("UTF-8"))

# 获取指定路径下,所有的文件夹或者文件
filelist = os.listdir()

# make dir 创建一个目录(文件夹)
os.mkdir("路径")

# remove dir 删除一个目录
os.rmdir(r"C:\Users\Administrator\Desktop\SZ-Python1812")

# 移除一个文件
os.remove(r"C:\Users\Administrator\Desktop\SZ-Python1812\day1.txt")

# 查看文件状态属性
os.stat()

# 给文件或文件夹重命名 os.rename(old,new)
os.rename(r"C:\Users\Administrator\Desktop\SZ-Python1812\day1.txt",r"C:\Users\Administrator\Desktop\SZ-Python1812\day12.txt")

# 绝对路径: 以盘符开头的路径
# 相对路径: 以本py文件为基准去寻找的文件路径

# 修改当前目录下的test.py的文件名为aaa.py   ./
os.rename(r"test.py",r"aaa.py")      # 不要./也可以修改成功
# ./     当前目录
# ../    上一级目录
os.rename(r"./aaa.py",r"./test.py")      # 修改成功

# 拆分路径,只会拆出最后一个文件夹
os.path.split("path")
# 拼接  os.path.join()

# 拆分路径.获取指定路径对应的文件扩展名(后缀名)
os.path.splitext("path")

# 判断指定路径是不是文件夹
os.path.isdir()

# 判断指定路径是不是文件
os.path.isfile()

# 判断指定路径是否存在
os.path.exists()

# 获取文件的大小[字节]
os.path.getsize()

# 获取指定文件夹的父路径
os.path.dirname()

# 获取当前文件夹的名称
os.path.basename()



# 练习：获取指定目录下所有的py文件或者txt文件
# > """
# > 思路：
# > 1.判断指定的目录是否存在
# > 2.获取指定目录下所有的文件以及文件夹
# > 3.拼接路径
# > 4.判断拼接之后的路径是否是文件
# > 5.判断文件名称的后缀
# > """
def getFile(path):
    #1.
    if os.path.exists(path):
        #2
        fileList = os.listdir(path)
        #3.
        for fileName in fileList:
            filePath = os.path.join(path,fileName)
            #4
            if os.path.isfile(filePath):
                #5
                if fileName.endswith("py") or fileName.endswith("txt"):
                    print(fileName)
            else:
                print(fileName,"不是文件")
    else:
        print("指定的路径不存在")