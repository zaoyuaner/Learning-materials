import re

#模式修正
"""
re.I:忽略大小写模式【ignorecase】
re.M：视为多行模式【more】
re.S：视为单行模式【single】
"""
pattern = re.compile(r"^love",re.M)
string = """
alove you
love her
love he
"""
result1 = pattern.search(string)
print(result1.group())


pattern = re.compile(r"[a-z]+",re.I)
result1 = pattern.search("LLLLLLlove")
print(result1.group())
