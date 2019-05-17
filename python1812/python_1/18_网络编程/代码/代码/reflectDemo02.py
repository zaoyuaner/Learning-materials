import  textDemo
#from textDemo import  music,image

str = input("请输入对应的操作指令：")
"""
if str == "home":
    textDemo.home()
elif str == "music":
    textDemo.music()
elif str == "image":
    textDemo.image()
"""

#使用反射解决
#判断模块中是否有对应的功能
res = hasattr(textDemo,str)
if res:
    #获取出来
    f = getattr(textDemo,str)
    print(f)
    print(f())

else:
    print("没有指定的功能")