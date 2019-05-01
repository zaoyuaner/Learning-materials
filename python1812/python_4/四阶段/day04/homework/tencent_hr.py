import re
import requests
from bs4 import BeautifulSoup
import pymysql

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}

#获取岗位总页数
def getPageNum(url):
    response = requests.get(url,headers=headers)
    #print(response.text)
    soup=BeautifulSoup(response.text,'lxml')
    pageNum = soup.select('.pagenav a')[-2].text
    return int(pageNum)
#获取每一页的岗位
#总页数  每一页的url
def getJobList(totalPage,url):
    qq_job_list=[] #用来保存每一个的岗位列表
    for i in range(totalPage):
        url = url+"&start=%d" % (i*10)
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        job_list =soup.select('.tablelist tr')[1:-1]
        #soup.select('.tablelist').find_all('tr',attrs=['even','odd'])
        for job in job_list:
            job_url = job.td.a['href']
            job_url = "https://hr.tencent.com/" +job_url
            #拿到url 我们开始获取岗位的详情
            getJobInfo(job_url,qq_job_list)

#获取每个岗位的详情况
def getJobInfo(url,qq_job_list):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    #岗位名称
    job_name = soup.select('#sharetitle')[0].text
    print(job_name)
    # 工作地点
    job_address = soup.select('.bottomline td')[0].span.next_sibling

    # 职位类别
    job_type = soup.select('.bottomline td')[1].span.next_sibling

    # 招聘人数
    job_num = soup.select('.bottomline td')[2].span.next_sibling
    job_num = re.findall(r'(\d+).*?',job_num)[0]

   #工作职责

    job_duty = soup.select('.squareli')[0].text
    print(job_duty)
    # 工作职责

    job_require = soup.select('.squareli')[1].text
    print(job_require)

    job_dict = {
        "name":job_name,
        "address":job_address,
        "type":job_type,
        "num":int(job_num),
        "duty":job_duty,
        "require":job_require

    }
    qq_job_list.append(job_dict)
    save(qq_job_list)


#保存到数据库
def save(qq_job_list):
    db = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='qq_hr',charset='utf8')
    cursor = db.cursor()
    for job in qq_job_list:
        name=job['name']
        address=job['address']
        type=job['type']
        num=job['num']
        duty=job['duty']
        require=job['require']

        sql = """insert into job(name,address,type,num,duty,reqire1) value('%s','%s','%s','%d','%s','%s')""" % (name,address,type,num,duty,require)
        cursor.execute(sql)
        db.commit()
    cursor.close()
    db.close()


if __name__ == "__main__":
    startUrl = "https://hr.tencent.com/position.php?keywords=python&lid=0&tid=0"

    #先爬取总页数
    totalPage = getPageNum(startUrl)
    #抓取每一页的岗位数据
    getJobList(totalPage,startUrl)