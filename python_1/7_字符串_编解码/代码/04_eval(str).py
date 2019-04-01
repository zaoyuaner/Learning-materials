# eval(str)  将参数字符串当做代码(表达式)来执行

print(type(eval("123")))     # 返回一个数字  效果相当于int

print(eval("-100"))          # -100
print(eval("12+3"))          # 15   用int会报错!
print(eval("12-3"))          # 9    用int会报错!

# print(int("abc123"))       # 错误
# print(eval("abc123"))      # 错误,变量未定义

