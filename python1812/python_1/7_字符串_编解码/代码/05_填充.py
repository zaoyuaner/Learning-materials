# 填充

# center()  让字符串居中,左右填充指定字符
str1 = "hello"
print(str1.center(10))       # center（width[,fillchar])
# 字符串总共10位,str1需要居中,左右默认填充空格
print(str1.center(10,"*"))   # **hello***填充的字符只能是一个! "*",如果是**或者3* 会报错

# ljust()  left左对齐,右填充
print(str1.ljust(10,"*"))    # hello*****  一共10个字符

# rjust()  right右对齐,左侧填充
print(str1.rjust(10,"*"))    # *****hello

# zfill()  zero只能填充0,右对齐,左侧填充0
print(str1.zfill(10))        # 00000hello

str3 = "helloworld"
# print(str3.ljust)

