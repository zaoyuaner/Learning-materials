#for实现9*9乘法表
#外层循环：控制行
for i in range(1,10):
#内层循环：控制列
    for j in range(1,i + 1):
       print("%dx%d=%d"%(j,i,i*j),end=" ")     # "%dx%d=%d"%(j,i,i*j)  格式
    print("")



print(False and True or True)
print(True and False and True)
print(False or True or False)
print(True or False and True)