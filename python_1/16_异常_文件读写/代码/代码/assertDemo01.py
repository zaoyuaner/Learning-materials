def func(num,divNum):

    #语法：assert 表达式，当出现异常时的信息描述
    #assert关键字的作用：预测表达式是否成立，如果成立，则执行后面的代码；如果不成立，则将异常的描述信息打印出来
    assert (divNum != 0),"被除数不能为0"

    return  num / divNum

print(func(10,20))
print(func(10,0))