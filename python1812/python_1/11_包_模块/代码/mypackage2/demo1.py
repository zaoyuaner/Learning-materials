import os,math,time,datetime   # 同时导入多个模块

import mypackage2.demo2         # 通过包名.模块名导入别的模块
								# 当模块被导入时,模块内部的代码会被执行一次

mypackage2.demo2.show()