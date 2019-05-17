from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("tencent.html",parser=parser)

# 获取所有的tr标签

#xpath返回的是 一个列表
# trs = html.xpath("//tr")
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# #获取第二个tr标签
# tr = html.xpath("//tr[2]")[0]
# print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

#获取所有class 为even 的  tr标签
# trs = html.xpath("//tr[@class='even']")
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

#获取所有a标签的href属性 获取属性的值
# aList = html.xpath("//a/@href")
# for a in aList:
#     print("http://hr.tencent.com/"+a)

#获取所有的职位信息 positon()从1开始  而不是从0开始
trs = html.xpath("//tr[position()>1]")
#在标签下面 要继续执行xpath函数  获取它的子孙元素
positions = []
for tr in trs:
    href = tr.xpath(".//a/@href")[0]
    fullurl = "http://hr.tencent.com/"+href
    title = tr.xpath("./td[1]//text()")[0]
    catrgory = tr.xpath("./td[2]//text()")[0]
    nums = tr.xpath("./td[3]//text()")[0]
    address = tr.xpath("./td[4]//text()")[0]
    pub_time = tr.xpath("./td[5]//text()")[0]
    position = {
        'url':fullurl,
        'title':title,
        'catrgory':catrgory,
        'nums':nums,
        'address':address,
        'pub_time':pub_time,
        
    }
    positions.append(position)

print(positions)