from lxml import etree

def parse_lagou_file():
    parser = etree.HTMLParser(encoding='utf-8') #先将html 解析成 utf-8
    htmls = etree.parse("tencent.html",parser=parser) # 再将文件加载过来 然后解析成html文档
    print(etree.tostring(htmls,encoding='utf-8').decode('utf-8'))#序列化成字符串

if __name__ == "__main__":
    parse_lagou_file()