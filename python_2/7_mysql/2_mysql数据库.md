#mysql数据库

## 一、高级

### 1.1 子查询

- 子查询嵌入到其他查询语句中查询语句，子查询只能出现在from，where中
- 子查询不要用select *,exists除外

~~~
select title 
from forum 
where uid in (select id from php_user where name='王琨' );


select * from blog_article where cid in (
    select cid from blog_category where name='心情'
);

select * from (select uid,username,gender from blog_user where gender='男') as user;
~~~

###1.2 多表查询(`*****`)

~~~
for category in blog_category:
   for article in blog_article:
       if category.cid == article.cid:
            #放到结果集中
~~~



- 多表连接必须**要有连接条件**，否则结果没有意义
- 多表连接有两种写法：隐式(标准sql)和显式内连接
- 隐式(标准sql)连接 ：  连接条件写到where字句中

 ~~~
select title,content,name,publish_time 
from user u,forum f  #给表起一个别名，方便书写
where u.id = f.uid; 在where写链接条件
			 
select title,content,name,publish_time 
from user u,forum f 
where u.id = f.uid and name='王琨';


select a.username,b.name ,c.title
    -> from bbs_user a,bbs_category b,bbs_forum c
    -> where b.cid = c.cid and c.uid = a.uid;

 ~~~

- 显示内连接（inner join）

 ~~~
mysql> select a.uid,username,title,content 
    -> from bbs_user a inner join bbs_forum b on a.uid =b.uid #关联条件
    -> where a.uid < 5;  #过滤条件
    
    select username,name,title
    -> from bbs_user a inner join bbs_forum c on c.uid =a.uid 
    -> inner join bbs_category b on c.cid = b.cid;

select title,remark,username from blog_remark r join blog_article a on r.aid = a.aid 
                                                join blog_user u on r.uid = u.uid;
select后的字段如果在多个表中都有，引用的时候必须加上表名.字段名
 ~~~

- 表的自身连接

 ~~~
select * from areainfo a,areainfo b where a.pid=b.code and  a.name='青河县';
+--------+-----------+--------+--------+-----------------+--------+
| code   | name      | pid    | code   | name            | pid    |
+--------+-----------+--------+--------+-----------------+--------+
| 654325 | 青河县    | 654300 | 654300 | 阿勒泰地区      | 650000 |
+--------+-----------+--------+--------+-----------------+--------+
1 row in set (0.01 sec)


//表的字段可以直接连接
select * from zzl_student where sno = monitor and class='95031';
 ~~~

### 1.3 外连接

两张表关联查询时，根据以那种表为主可以分为左外连接和右外连接

- 左外连接  

​      以左表为主，如果右边的表里没有匹配的记录，则添加一个万能记录（各个字段都为null)与之连接

    select username,r.* from blog_user u left join  blog_remark r on u.uid = r.uid
    +-----------+------+-------------+------+------+------------+-----------+
    | username  | rid  | remark      | aid  | uid  | remarktime | isdisplay |
    +-----------+------+-------------+------+------+------------+-----------+
    | 萧峰      |    1 | adsafd      |    1 |    1 | NULL       |         0 |
    | 慕容复    |    2 | kdkdkdkd    |    2 |    3 | NULL       |         0 |
    | 丁春秋    |    3 | ooooooooooo |    3 |    4 | NULL       |         0 |
    | 丁春秋    |    4 | ppppp       |    2 |    4 | NULL       |         0 |
    | 阿朱      | NULL | NULL        | NULL | NULL | NULL       |      NULL |
    | 阿碧      | NULL | NULL        | NULL | NULL | NULL       |      NULL |
    | 谢晓峰    | NULL | NULL        | NULL | NULL | NULL       |      NULL |
    +-----------+------+-------------+------+------+------------+-----------+

- 右外连接（right join）

以右表为主，如果左边的表里没有匹配记录，则增加一个万能记录与之连接



### 1.4 集合操作

可以使用union将两个查询结果合并，mysql只支持并，不支持差和交

- 两个结果集中字段数一样，对应字段类型兼容
- 自动去除重复记录,不去除重复记录可以用 union all
- order by 放到最后

  ~~~
  select * from student where class = '95031'
  union all
  select * from student where ssex='女';
  ~~~

### 1.5 内部函数

- 字符串函数

  | 函数                     | 功能                                                         |
  | ------------------------ | ------------------------------------------------------------ |
  | char_length(*str*)       | 获取字符串的字符个数                                         |
  | length(str)              | 获取字符串的字节数                                           |
  | concat(s1, s2, ... , sn) | 连接s1, s2, ..., sn 为一个字符串                             |
  | lower(str)               | 将字符串str中所有的字符转换为小写                            |
  | upper(str)               | 将字符串str中所有的字符转换为大写                            |
  | left(str, x)             | 返回字符串str最左边的x个字符                                 |
  | right(str, y)            | 返回字符串str最右边的y个字符                                 |
  | lpad(str, n, pad)        | 用字符串pad对str最左边进行填充， 直到长度为n个字符长度       |
  | rpad(str, n, pad)        | 用字符串pad对str最右边进行填充， 直到长度为n个字符长度       |
  | ltrim(str)               | 去掉str中最左边的空格                                        |
  | rtrim(str)               | 去掉str中最右边的空格                                        |
  | trim(str)                | 去掉字符串str两边的空格                                      |
  | repeat(str, x)           | 返回str中重复出现x次的结果                                   |
  | replace(str, a, b)       | 将字符串str中的a更换为b                                      |
  | insert(str, x, y, instr) | 将字符串str从第x位置开始， y个字符长度的子字符串替换为字符串instr |
  | strcmp（s1, s2）         | 比较字符串s1, s2                                             |
  | substring(str, x, y)     | 返回字符串str x位置开始y个字符长度的字符串                   |

- 日期函数

  | 函数名                | 功能                              |
  | --------------------- | --------------------------------- |
  | curdate()             | 得到当前日期                      |
  | curtime()             | 得到当前时间                      |
  | now()                 | 得到当前日期和时间                |
  | year(date)            | 得到date的年份                    |
  | month(date)           | 得到date的月份                    |
  | day(date)             | 得到date的天                      |
  | hour(time)            | 得到time的小时                    |
  | minute(time)          | 得到time 的分钟                   |
  | second(time)          | 得到time的秒                      |
  | week(date)            | 得到date是一年中的第几周          |
  | date_format(date,fmt) | 按格式化串fmt返回date的日期字符串 |

   select DATE_FORMAT(now(),'%Y- %m-%d %H:%i:%s');  

- 数学函数

  | 函数名     | 功能                        |
  | ---------- | --------------------------- |
  | abs(x)     | 求x的绝对值                 |
  | ceil(x)    | 向上取整                    |
  | floor(x)   | 向下取整                    |
  | round(x,d) | 四舍五入，d为保留小数的位数 |
  | pow(x,y)   | x的y次幂                    |
  | rand()     | 0~1之间的随机小数           |
  | mod(x,y)   | 等同于x % y,求x对y的模      |

- 其它函数

  | 函数名                                   | 功能                                                         |
  | ---------------------------------------- | ------------------------------------------------------------ |
  | convert(expr as type)/cast(expr as type) | 将表达式expr转换为type类型，type可以是：char(n)、date、datetime、integer、decimal |
  | md5(str)                                 | 计算str的哈希值，返回一个 32位十六进制数字的二进制字符串     |
  | sha1(str)/sha(str)                       | 计算str的哈希值，返回一个 40位十六进制数字的二进制字符串     |


## 二、数据控制

###2.1 事务

- 事务把一组操作看做一个整体，要不都操作成功，要不都操作失败 。(ACID)
- 表的数据库引擎必须是innodb，innodb支持事物，myisam不支持事务

- 修改表引擎：alter table  表名 engine = innodb

  ~~~~
  查询是否为自动提交
  select @@autocommit  (1为自动提交   0为手动提交)

  关闭自动提交
  set autocommit = 0

  start transaction /begin

  一组操作
  commit/rollback

  commit 提交 会把数据写到硬盘
  rollback 回滚 撤销操作
  ~~~~

  ​

###2.2 授权管理(了解)

- 创建用户

   ~~~
   create user '用户名'@'服务器地址' identified by '密码'
   ~~~

- 删除用户

  ~~~
  drop user  '用户名'@'服务器地址'
  ~~~

- 修改密码

  ~~~
  修改当前登录用户
  set password = password('123456');
  			
  一般管理员可以修改任意用户密码
  set password for 'db'@'localhost' = password('2333');
  ~~~

- 刷新

  ~~~
  flush privileges
  ~~~

- 授权

  ~~~
   grant 权限  on 数据库.表  to '用户名'@'服务器地址'
    grant all on *.* to 'dd'@'localhost'
  	 *.* 所有数据库的所有表
  	 all 代表所有权限  
  	 权限包括：select、update、delete、alter、insert
  ~~~

- 回收

  ~~~
   revoke select on test.stars from 'db'@'localhost';
  ~~~

## 三、索引

索引就像图书的目录，可以加快查询速度

### 3.1 索引的优点

- 可以大大加快数据的检索速度
- 唯一索引可以保证数据的唯一性
- 可以降低分组、排序的时间
- 可以使用查询优化器提高系统性能

### 3.2 索引的缺点

- 建立索引会建立对应索引文件，占用大量空间
- 建立索引会降低增、删、改的效率

### 3.3 不建立索引

- 频繁更新的字段不要建立索引
- 没出现在where、having，不要建立索引
- 数据量少的表没有必要建立索引
- 唯一性比较差的字段不要建立索引

### 3.4 索引分类

####  普通索引

    create index 索引名 on 表名(字段 asc/desc) 默认asc升序

####  唯一索引

  在唯一索引所在列不能有重复值，增加和修改会受影响。

~~~
create  unique index 索引名 on 表名(字段 asc/desc) 默认asc升序
~~~

####  主键索引

  创建表，主键索引会自动添加，要求在主键上不能有重复值，不能有空值

#### 复合索引（联合索引） 索引了多个列

- 使用联合索引，必须包含左前缀。  （a,b,c)
  - a
  - a,b
  - a,b,c

#### 全文索引（了解）

   一般会用全文索引服务器(sphinx)，不会直接创建全文索引

  ~~~
create  FULLTEXT index 索引名 on 表名(字段 asc/desc)
  ~~~

#### 删除索引

  ~~~
drop index 索引名 on 表
  ~~~

#### 查看索引

   ~~~
show index from 表 \G

#查看sql性能
explain select sno,sname from student where class='1812'\G;
mysql> explain select sno,sname from student where sclass='1812' ;
+----+-------------+---------+------------+------+---------------+------+---------+------+------+----------+-------------+
| id | select_type | table   | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
+----+-------------+---------+------------+------+---------------+------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | student | NULL       | ALL  | NULL          | NULL | NULL    | NULL |   10 |    10.00 | Using where |
+----+-------------+---------+------------+------+---------------+------+---------+------+------+----------+-------------+
1 row in set, 1 warning (0.00 sec)
type:  ALL  全表扫描
       index  使用索引
       range  在指定范围内使用索引
       const、system 常量查询

   ~~~

#### 其它创建索引的方式

 ~~~
alter table 表 add index(字段1,字段2,...)
alter table 表 add primary key(字段1,字段2,...)
alter table 表 add unique(字段1,字段2,...)
alter table 表 add fulltext(字段1,字段2,...)
 ~~~

### 3.5 不使用索引的情况

- 查询时的联合索引没有左前缀，不使用索引
- or条件里，如果一方字段没有索引，则不使用索引
- 类型不对应的不会使用索引
- like  '%tom' ,如果左边是通配符，不会使用索引
- 使用!=、<>、not in操作，不使用索引



## 四、外键

如果表A的主关键字是表B中的字段，则该字段称为表B的外键，表A称为主表，表B称为从表

- 数据表引擎必须是innodb
- 主表和从表相关的外键字段类型必须兼容

~~~
创建外键
ALTER TABLE 从表名
ADD CONSTRAINT 外键名称 FOREIGN KEY (从表的外键列) REFERENCES 主表名 (主键列) 
[ON DELETE reference_option]
[ON UPDATE reference_option]

reference_option:
RESTRICT | CASCADE | SET NULL | NO ACTION
  1. CASCADE: 从父表中删除或更新对应的行，同时自动的删除或更新子表中匹配的行。ON DELETE CANSCADE和ON UPDATE CANSCADE都被InnoDB所支持。
  
  2. SET NULL: 从父表中删除或更新对应的行，同时将子表中的外键列设为空。注意，这些在外键列没有被设为NOT NULL时才有效。ON DELETE SET NULL和ON UPDATE SET SET NULL都被InnoDB所支持。

  3. NO ACTION: InnoDB拒绝删除或者更新父表。

  4. RESTRICT: 拒绝删除或者更新父表。指定RESTRICT（或者NO ACTION）和忽略ON DELETE或者ON UPDATE选项的效果是一样的。

删除外键
ALTER TABLE 从表 DROP FOREIGN KEY 外键名
~~~



## 五、视图

有时候经常会遇到复杂的查询，写起来比较麻烦，这时候我们可以使用视图简化查询。视图就是固化的sql语句，可以不把视图当做基本表使用

- 不要在视图上进行增、删、改

~~~
创建视图
create view 视图名(字段列表) as 
select子句

删除视图
drop view 视图名
~~~



## 六、数据库备份与恢复

- 备份

  ~~~
  不用登录mysql，直接执行mysqldump命令,将指定数据库备份到家目录下的指定文件
  mysqldump –uroot –p 数据库名 > ~/备份文件名.sql;
  ~~~

- 恢复

  ~~~
  首先要创建一个mysql数据库，然后退出mysql，执行以下命令
  mysql -uroot –p 数据库名 < ~/备份文件.sql
  ~~~


## 七、pymysql操作mysql数据库

- 安装pymysql

    ~~~
    pip install pymysql
    ~~~

### 7.1 pymysql操作数据库的五行拳

1. 连接数据库

   使用Connect方法连接数据库

   ~~~
   pymysql.Connections.Connection(host=None, user=None, password='', database=None, port=0,  charset='')
   参数说明：
       host – 数据库服务器所在的主机。
       user – 登录用户名。
       password – 登录用户密码。
       database – 连接的数据库。
       port – 数据库开放的端口。（默认: 3306）
       charset – 连接字符集。
   返回值：
      返回连接对象
      
   例子：
   link = pymysql.Connect(host='localhost', port=3306, user='root', password='123456', db='zzl', charset='utf8')

   ~~~

   - 连接对象方法

   | 方法                  | 说明              |
   | ------------------- | --------------- |
   | begin()             | 开启事务            |
   | commit()            | 提交事务            |
   | cursor(cursor=None) | 创建一个游标用来执行sql语句 |
   | rollback()          | 回滚事务            |
   | close()             | 关闭连接            |
   | select_db(db)       | 选择数据库           |

2. 创建游标

   ~~~
   cursor = link.cursor()
   print(cursor.rowcount) #打印受影响行数
   ~~~

   | 方法                        | 说明                                       |
   | ------------------------- | ---------------------------------------- |
   | close()                   | 关闭游标                                     |
   | execute(query, args=None) | 执行单条语句，传入需要执行的语句，是string类型；同时可以给查询传入参数，参数可以是tuple、list或dict。执行完成后，会返回执行语句的影响行数。 |
   | fetchone()                | 取一条数据                                    |
   | fetchmany(n)              | 取多条数据                                    |
   | fetchall()                | 取所有数据                                    |

3. 执行sql语句

   ~~~
   # 执行sql语句
   sql = 'select * from user1'
   # 执行完sql语句，返回受影响的行数
   num = cursor.execute(sql)
   ~~~

4. 获取结果集

   ~~~
   result1 = cursor.fetchone()
   print(result1)
   ~~~

5. 关闭连接

   ~~~
   cursor.close()
   link.close()
   ~~~

- 注意：

  写完代码后，需要将py文件添加可执行权限 

  ~~~
  sudo chmod +x conndb.py
  ./conndb.py
  ~~~

  ​

### 7.2 pymysql中事务处理

pymysql默认是没有开启自动提交事务，所以我们如果进行增、删、改，就必须手动提交或回滚事务。

~~~
sql = 'delete from user where id=%s' % user_id

# 如果要执行增删改语句的时候，下面的就是固定格式
try:
	cursor.execute(sql)
	# 如果全部执行成功，提交事务
	link.commit()
	print(cursor.lastrowid) #获取最后插入记录的自增id号
except Exception as e:
	print(e)
	link.rollback()
finally:
	cursor.close()
	link.close()

~~~

