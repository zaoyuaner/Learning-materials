import  itertools

list = list(itertools.product("0123456789qwertyuioplkjhgfdsazxcvbnm",repeat=3))
print(list)
print(len(list))

