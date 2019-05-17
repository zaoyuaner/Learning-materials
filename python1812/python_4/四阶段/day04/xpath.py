# 使用 lxml 的 etree 库
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
     </ul>
 </div>
'''

#利用etree.HTML，将字符串解析为HTML文档
html = etree.HTML(text)
#urls = html.xpath("//ul")
urls = html.xpath("//a/@href")
for url in urls:
    print(etree.toString(url,encoding='utf-8').decode('utf-8'))
# 按字符串序列化HTML文档
result = etree.tostring(html)
print(result)