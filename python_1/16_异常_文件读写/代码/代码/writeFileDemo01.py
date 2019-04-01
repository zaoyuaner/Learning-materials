path = "file1.txt"

#1.打开文件
#注意：写入文件的时候，文件可以不存在，当open的时候会自动创建文件
#读取文件的时候，文件必须先存在，才能open
f = open(path,"w",encoding="utf-8")

#2.写入数据
#注意：将数据写入文件的时候，默认是没有换行的，如果向换行，则可以手动添加\n
f.write("Python1805高薪就业，走上人生巅峰")

#3.刷新数据缓冲区
#作用：加速数据的流动，保证缓冲区的流畅
f.flush()

#4.关闭文件
f.close()

#简写形式
with open(path,"w",encoding="utf-8") as f1:
    f1.write("hello")
    f.flush()