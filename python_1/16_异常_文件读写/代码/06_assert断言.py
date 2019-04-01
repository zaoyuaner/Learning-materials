# 语法：asser 断言 。条件 [,异常描述字符串]  帮助调试的功能
#
# ​执行流程：如果条件为假，则抛出AssertionError，条件为真，就当assert不存在
#
# 作用：对于可能出问题的代码，加上断言，方便问题排查

print('start')
num = int(input('请输入一个1~9的整数:'))
assert 0 <num <9,'num不在1~9'         # 异常描述字符串
print('end')