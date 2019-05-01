#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import *
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

'''
解析pdf文件，获取文件中包含的各种对象
'''



# 解析pdf文件函数
def parse(pdf_path,toPath):
    fp = open(pdf_path, 'rb')  # 以二进制读模式打开
    # 用文件对象来创建一个pdf文档分析器
    parser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器 与文档对象
    parser.set_document(doc)
    doc.set_parser(parser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # 循环遍历列表，每次处理一个page的内容
        for page in doc.get_pages(): # doc.get_pages() 获取page列表

            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):  # 获取文本内容
                    # 保存文本内容
                    with open(toPath, 'a',encoding="utf-8") as f:
                        results = x.get_text()
                        f.write(results + '\n')


if __name__ == '__main__':
    pdf_path = r'C:\Users\Administrator\Desktop\00001.pdf'
    topath = r'C:\Users\Administrator\Desktop\new3.txt'
    parse(pdf_path,topath)

