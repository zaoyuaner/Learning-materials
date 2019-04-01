# .strip() 移除,删除两头指定的字符,不能是字符串
str1 = "*****hello******world****"
print(str1.strip("*"))

str2 = "     hello   world     "
print(str2.strip(" "))         # 移除两端的空格
print(str1.lstrip("*"))        # 删除左侧的*
print(str1.rstrip("*"))        # 删除右侧的*



