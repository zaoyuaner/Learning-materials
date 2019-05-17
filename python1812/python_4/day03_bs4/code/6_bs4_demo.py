from bs4 import BeautifulSoup
doc_html = '''
<!DOCTYPE html>
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title">adsfadf<b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>


'''


#fp = open('index.html',encoding='utf-8')

#soup = BeautifulSoup(fp.read(),'lxml')
soup = BeautifulSoup(doc_html,'lxml')
# print(type(soup))
# print(soup.prettify()) #格式化代码
# print("="*30)
# print(soup.head) #获取head标签  返回的是标签及里边的所有内容
# print(soup.head.title) #获取标签的子标签
# print(soup.head.name) #仅仅返回标签名字

#属性

# print(soup.p.attrs) #获取第一个p标签的属性{'class': ['title']}
# print(soup.a.attrs)#{'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}
# print(soup.a.attrs['class'])#只查a标签的class属性['sister']
# print(soup.a.attrs.get('href'))#http://example.com/elsie
# print(soup.a['href'])#http://example.com/elsie

## 文本
# print(soup.p.string) #string：获取某个标签下的非标签字符串。返回来的是个字符串。如果这个标签下有多行字符，那么就不能获取到了。
# print(soup.p.b.string)

## 获取节点内部的文本内容  text get_text()
# print(soup.p.text) #节点内部的所有文本内容
# print(soup.p.b.get_text())

## 兄弟节点
print(soup.a.next_sibling) #下一个节点  包含文本节点 换行 空白都算文本节点

print(soup.a.next_sibling.next_sibling)#弟弟的弟弟
print(soup.a.previous_sibling)#上一个文本节点