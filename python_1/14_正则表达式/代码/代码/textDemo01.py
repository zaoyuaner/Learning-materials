import  re     #regular  Expession   regex
#需求：判断一个qq号是否是合法的
"""
分析：
1.全数字
2.第一位数字不能为0
3.位数：5~11
"""
def checkQQ(str):
    #不管str是否合法，假设合法
    result = True

    #寻找条件推翻假设
    try:
        #判断是否是全数字
        num = int(str)

        #判断位数
        if len(str) >= 5 and len(str) <= 11:

            #判断开头是否为0
            if str[0] == "0":
                result = False

        else:
            result = False
    except ValueError as e:
        result = False

    return  result


print(checkQQ("6725675785678657"))

#使用正则表达式实现上面的需求
result = re.match(r"[1-9]\d{4,10}","6725675786574657")
print(result)
