#encoding: utf-8

from bs4 import BeautifulSoup

html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tbody>
        <tr class="h">
            <td class="l" width="374">职位名称</td>
            <td>职位类别</td>
            <td>人数</td>
            <td>地点</td>
            <td>发布时间</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=33824&keywords=python&tid=87&lid=2218">22989-金融云区块链高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=29938&keywords=python&tid=87&lid=2218">22989-金融云高级后台开发</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31236&keywords=python&tid=87&lid=2218">SNG16-腾讯音乐运营开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31235&keywords=python&tid=87&lid=2218">SNG16-腾讯音乐业务运维工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34531&keywords=python&tid=87&lid=2218">TEG03-高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34532&keywords=python&tid=87&lid=2218">TEG03-高级图像算法研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31648&keywords=python&tid=87&lid=2218" id="test" class="test">TEG11-高级AI开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>4</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=32218&keywords=python&tid=87&lid=2218">15851-后台开发工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=32217&keywords=python&tid=87&lid=2218">15851-后台开发工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34511&keywords=python&tid=87&lid=2218">SNG11-高级业务运维工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
    </tbody>
</table>
"""

#获取所有的tr标签
#获取第2个tr标签
#获取所有class 为even的tr标签
#获取所有a标签的 href属性
#获取所有的职位信息  要求纯文本

#获取所有的tr标签

soup = BeautifulSoup(html,'lxml')
# 1
# trs = soup.select('tr')
# for tr in  trs:
#     print(tr)
#     print('*'*30)
#     break

# tr = soup.select('tr')[1]
# print(tr)

#获取所有class 为even的 tr标签
# trs = soup.select(".even")
# for tr in trs:
#     print(tr)

# trs = soup.select("tr[class='even']")
# for tr in trs:
#     print(tr)

# aList = soup.select('a')
# for a in aList:
#     print(a['href'])

trs = soup.select('tr')
for tr in trs:
    infos = list(tr.stripped_strings)
    print(infos)