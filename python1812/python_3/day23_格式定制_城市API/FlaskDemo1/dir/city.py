import json
import pymysql

# 连接数据库
# def __init__(self, host=None, user=None, password="",
#                  database=None, port=0, unix_socket=None,
#                  charset=''
db = pymysql.Connect(host='127.0.0.1', user='root', password='123456', database='python18120327', port=3306, charset='utf8')
# 游标
cursor = db.cursor()

# 打开文件
with open('citydata.json', 'r') as fp:
    # 加载json
    city_collection = json.load(fp)

    # 具体数据
    returnValue = city_collection['returnValue']

    # 获取returnValue中所有key
    letters = returnValue.keys()

    # 插入数据库中
    for letter in letters:
        # 插入字母表
        # INSERT INTO letter(name) VALUES('A');
        db.begin()
        cursor.execute("INSERT INTO letter(name) VALUES('{}');".format(letter))
        db.commit()

        # 后续添加城市时，需要字母ID
        # SELECT id FROM letter where letter.name='B'
        db.begin()
        cursor.execute("SELECT id FROM letter where letter.name='{}'".format(letter))
        db.commit()
        # 取出这条记录中的ID 【字母ID】
        letter_result = cursor.fetchone()
        letter_id = letter_result[0]

        # 根据字母 获取 对应城市列表
        city_list = returnValue[letter]

        # 遍历每个城市
        for city in city_list:
            # 插入城市表
            # 难点: 需要城市 对应 字母ID
            # INSERT INTO city VALUES(100, 0, '深圳', 56789, 'shenzhen', 1)
            db.begin()
            cursor.execute("INSERT INTO city VALUES({}, {}, '{}', {}, '{}', {})".format(city['id'], city['parentId'], city['regionName'], city['cityCode'], city['pinYin'], letter_id))
            db.commit()
