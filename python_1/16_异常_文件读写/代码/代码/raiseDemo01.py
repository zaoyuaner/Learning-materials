#raise的使用主要体现在自定义异常中

#1.raise表示直接抛出一个异常对象【异常是肯定存在的】
#创建对象的时候，参数表示对异常信息的描述
try:
    raise NameError("hjafhfja")
except NameError as e:
    print(e)

print("over")

"""
总结：
通过raise抛出的异常，最终还是需要通过try-except处理
"""

#2.如果通过raise抛出的异常在try中不想被处理，则可以通过raise直接向上抛出
try:
    raise NameError("hjafhfja")
except NameError as e:
    print(e)
    raise
