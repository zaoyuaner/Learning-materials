# 判断字符串 str.
# .isalpha()  如果字符串全部为字母,并且至少有一个字符,则返回真,其余返回假.
print("hello".isalpha())        # True
print("123J".isalpha())         # False
print("".isalpha())             # False

# .isalnum()  如果字符串是由字母数字组成,并且为一个以上,返回真,否则返回假
print("".isalnum())             # False
print("123sad".isalnum())       # True
print("123".isalnum())          # True
print("##HD&&".isalnum())       # False

# .isupper()  字符串至少包含一个字符出现大写,还可以有非小写字母,返回真
# 如果有小写字母  就返回假
print("s".isupper())            # False
print("#@A1".isupper())         # True

# .islower()   除了大写字母,都返回真
print("sz123".islower())        # True
print("A".islower())            # False

# .istitle()   每个单词的首字母必须全部大写才返回Ture
print("Hello World".istitle())  # True
print("Hello world".istitle())  # False

# .isdigit()   全部由数字组成,返回真
print("12341".isdigit())        # True
print("asd12".isdigit())        # False

