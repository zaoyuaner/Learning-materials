#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
内置模块   不需要安装，不需要自己定义，直接导入即可调用
自定义模块  需要自己定义，导入可使用
第三方模块  需要安装，不需要自己定义，导入可以使用。
'''

'''
如何安装第三方模块？
使用pycharm安装第三方模块
1.file --》settings --》project  --》project interpreter --》+
-->搜索安装的模块名---》 install --》apply

2.打开终端  cmd --》 
pip install  模块名 
1》网络不通
2》pip没有升级  pip install --upgrade pip
'''
from PIL import Image

img = Image.open("img1.jpg")

print(img.size,img.mode,img.format)
img.thumbnail((300,200))
img.save("test.png")