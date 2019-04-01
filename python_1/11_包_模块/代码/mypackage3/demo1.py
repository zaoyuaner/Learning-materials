from mypackage3.demo2 import *

# 默认会执行demo1的代码



show()          #666  如果被__name__ == "__main__"标记,那么代表导入时,默认不会执行
							# 手动强制调用,还是会被执行