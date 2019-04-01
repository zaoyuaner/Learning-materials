import pymysql
from settings import database

"""
SELECT {fields} FROM {table} {where} {groupby} {having} {orderby} {limit}.format(table='stduent',fields='sno,sname')
"""
class Manager:
    def __init__(self,tableName):
        self.tableName = tableName  # 表名
        self.conn = self.__connect(**database)   # 链接数据库
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)  #游标
        self.options = self.__initOptions()  # 初始化查询参数

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def __connect(self,**kwargs):
        """
        自定义的链接数据库方法
        :param kwargs: 数据库链接参数字典
        :return: 链接对象
        """
        return pymysql.Connect(**kwargs)
    def __initOptions(self,**kwargs):
        """
        初始化查询参数字典
        :param kwargs: 字典，保存查询参数
        :return:
        """
        return {
            'fields':'*',
            'table':self.tableName,
            'where' :' where ssex="男"',
            'groupby':'',
            'having' : '',
            'orderby':'',
            'limit'  :''
        }
    def where(self,**kwargs):
        """"
        {'user':'root','password':'123}
        where user='root' and password='123
        """
        # print(kwargs)
        if len(kwargs) <= 0:  # 如果不传任何参数，直接返回
            return self
        if not self.options['where']:  # 没有where条件
            self.options['where'] = " where "
        else:
            self.options['where'] += ' and '

        for key in kwargs:
            if isinstance(kwargs[key],str):
                self.options['where'] += key + " = '" + kwargs[key]+"'" + ' and '
            else:
                self.options['where'] += key + " = " + str(kwargs[key])  + ' and '
        self.options['where'] = self.options['where'].rstrip('and ') # 去除最后的and
        # print(self.options)
        return self

    def limit(self,*args):
        """
        (10,20)
        :param args:
        :return:
        """
        self.options['limit'] = ' limit '
        for value in args:
            self.options['limit'] +=  str(value) + ' , '
        self.options['limit'] = self.options['limit'].rstrip(', ')
        return self

    def select(self):
        sql = "SELECT {fields} FROM {table} {where} {groupby} {having} {orderby} {limit}".format(**self.options)
        print(sql)


if __name__ == "__main__":
    db = Manager('student')
    # sql ="SELECT {fields} FROM {table} {where} {groupby} {having} {orderby} {limit}".format(**db.options)
    # print(db.options)
    # print(sql)
    db.where(username='root',password=123).limit(10,20).select()