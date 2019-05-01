'''
封装开放数据类
'''
import  time
import re
class Person:
    def __init__(self,person_list):
        self.name = person_list[0]
        self.idcard = person_list[1]
        self.gender = person_list[2]
        self.birthday = person_list[3]
        if person_list[3].isdigit():
            self.age = time.localtime()[0] - int(person_list[3][:4])
        else:
            self.age = 0
        self.address = person_list[5]
        self.zipcode = person_list[6]
        self.phone = person_list[7]
        self.tel1 = person_list[8]
        self.tel2 = person_list[9]
        self.email = person_list[10]
    def __str__(self):
        return "{} {} {} {}".format(self.name,self.sex,self.idcard,self.phone)
    @property
    def sex(self):
        if self.gender == 'M':
            return  '男'
        return '女'
    @sex.setter
    def sex(self,value):
        self.gender = value

class KaiFang:
    def __init__(self,file_name):
        self.data = []  #保存开放数据
        self.file_name = file_name
        self.__read_file()  #读取文件数据

    def display_all(self):
        for person in self.data:
            print(person)

    # 搜索
    def search(self,name):
        result = []
        for person in self.data:
            if re.search(r'{}'.format(name),person.name,re.I):
                result.append(person)
        return  result

    # 排序
    def sort_by_age(self):
        self.data.sort(key=lambda person:person.age)

    #辅助方法
    def __read_file(self):
        '''
        功能：读取文件数据，分隔字符串创建对象，将对象加入到data中
        :return:
        '''
        with  open(self.file_name,encoding='utf-8') as fp:
            content = fp.readlines()  #得到所有行的列表

            # 遍历content
            for line in content:
                line = line.rstrip().split(',')
                # 将值为-或空的设置为无
                line = [ value if value !='-' and value !='' else '无'  for value in line]
                # 不足11列的添加“无”到line，补满11列
                if len(line) < 11:
                    for i in range(11-len(line)):
                        line.append("无")
                self.data.append(Person(line))  #将对象添加到列表


if __name__ == '__main__':
    kf = KaiFang(r'kaifang.txt')
    kf.sort_by_age()
    kf.display_all()
    name = input('请输入一个姓名：')
    res = kf.search(name)
    if res:
        for person in res:
            print(person)
