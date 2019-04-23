
数据库可能会考的题目
1、数据库和数据库管理系统之间的关系？
数据库：存储，维护和管理数据的集合
数据库管理系统：其实就是数据库管理软件，通过它可以进行数据库的管理和维护工作

2、sql 语言分类
DDL 数据定义语言  库 表结构
DML 数据操作语言  数据增删改
DQL 数据查询语言 数据查询
DCL 数据控制语言

3、库层的增删改查
创建库 create database 数据库名 default charset=utf8;
删除库 drop database 数据库名;
修改库字符集 alter database 数据库名 default charset=utf8;
查看库 show databases；
查看建库语句 show create database 数据库名；
查看当前使用的数据库 select database();
切换进入数据库 use database

4、表结构层的增删改查
- 创建表create table 表名（

  ​       字段名1 类型 限制，（primary key   auto_increment）

  ​       字段名2 类型  限制，

  ​       ...

  ​     复合主键可以放在这primary key（字段，字段）

  ）engine=innodb default charset=utf8;

primary key 主键 不允许有重复值,不允许为空
auto_increment 自增长，只对int型主键起作用

- 删除表 drop table 表名；

- 改表

  - 修改表名   alter table 表名 **rename** 新表名

  - 修改字段数据类型  alter table 表名 **modify** 字段名 类型 [限制]
  - 修改字段名和类型 alter table 表名 **change** [column] 旧字段名 新字段名 类型 [限制];
  - 增加字段 alter table 表名  **add** [column] 字段名 类型 [限制];
  - 删除字段 alter table 表名 **drop** [column] 字段名;
  - 修改字段的排列位置 alter table 表名 modify 字段1 数据类型 first|after 字段2

- 查看表结构 desc 表名；

- 查看建表语句 show create table 表名；

5、表数据层的增删改查
- 增 insert

  ```
  insert into 表名(字段1，字段2...) values(值1,值2...);
  insert into 表名 values(值1,值2...);
  insert into 表名(字段1，字段2...) 
    		 values(值1,值2...),
    		 (值1,值2...),
    		 (值1,值2...)....
  
  ```

- 删 delete和truncate

  delete from 表名 where 条件；#如果不加条件，会删除表中所有数据,慎重使用

  truncate table 表名,清空表中所有记录，等价于delete from 表名；

```
delete和truncate差别，truncate后，表中自增主键值从1开始
```

- 改 update

  update 表名 set 字段1=值1,字段2=值2... where 条件  #不加where修改的是所有的记录

- 查 select
select 字段 from 表名 [ where 条件 、  group by  、having 、 order by 、limit  ] 

  - 单表常规查询 
  - 单表子查询
  - 多表查询 隐式连接（标准sql）和 显示内连接 join on
  - 表自身连接
  - 外链接 左连接和右连接
  - 查询合并操作（只支持查询结果的并集）

6、事务
7、索引
- 创建索引
  普通索引 create index 索引名 on 表名(字段 asc/desc) 默认asc升序
  唯一索引 create  unique index 索引名 on 表名(字段 asc/desc) 默认asc升序 （或修改字段限制为unique）
  主键索引 主键字段自带
  全文索引 create  FULLTEXT index 索引名 on 表名(字段 asc/desc)
- 删除索引 drop index 索引名 on 表
- 查看索引 show index from 表 \G（；）

> 通过修改字段的方式添加索引：
> alter table 表 add index(字段1,字段2,...)
> alter table 表 add primary key(字段1,字段2,...)
> alter table 表 add unique(字段1,字段2,...)
> alter table 表 add fulltext(字段1,字段2,...)

8、外键
如果表A的主关键字是表B中的字段，则该字段称为表B的外键，表A称为主表，表B称为从表。
添加外键：
- create table score1( score int, courseid int,stuid varchar(10), constraint stu_sco_id foreign key(stuid) references student(stuid) );

- alter table score2 add constraint stu_sco_id foreign key(stuid) references student(stuid);

删除外键：
ALTER TABLE 从表 DROP FOREIGN KEY 外键名

9、备份与恢复
shell下备份 mysqldump -u root -p  数据库名>生成sql脚本的路径
mysql下恢复  创建空数据库 -> use 库 -> source /home/rock/Desktop/mydb1.sql;
            或者 创建空数据库 -> mysql -uroot –p 数据库名 < ~/备份文件.sql

10、pymysql 操作mysql的通用步骤

```python
import pymysql

# 连接数据库
conn = pymysql.connect('localhost', 'user', 'password', 'db')
# 创建游标
cursor = conn.cursor()

# 定制sql语句
sql = '增删改查语句，mysql怎么写这里怎么写'


# 操作表数据第一种情况是需要执行事务的增删改写法
try:
    cursor.execute(sql)
    conn.commit()  # 如果全部执行成功，提交事务
except Exception as e:
    print(e)
    conn.rollback() # 失败回滚

# 操作表数据第二种情况是不需要执行事务的查询写法
# 执行sql语句，获取结果集
cursor.execute(sql)
res = cursor.fetchone()  # res = cursor.fetchall()

# 关闭游标
cursor.close()
# 关闭数据库
conn.close()

```

11、char和varchar的区别：

- char的执行效率高于varchar ，varchar 相对于 char 节省存储空间
- 如果使用char 传入的数据的长度 小于指定的长度的时候 存储的实际长度 不够的会拿空格来填充
- 如果使用 varchar 传入的数据的长度 小于指定的长度的时候 存储的实际长度 为传进来的数据的长度

12、数据库引擎，其中 myisam和innodb的区别：

- myisam查询速度快，不支持事务、不支持外键、支持表锁

- innodb增删改效率高，支持事务、支持外键，支持行锁

13、事务的四大特征ACID

原子性（Atomicity，或称不可分割性）、
		一致性（Consistency）、
		隔离性（Isolation，又称独立性）、
		持久性（Durability）。

原子性：
	一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。

一致性：
	在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设规则，这包含资料的精确度、串联性以及后续数据库可以自发性地完成预定的工作。

隔离性：
	数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）。

持久性：
	事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。

14、事务的流程

 执行开始事务命令后,下面将进入事务模式. **start transaction、begin**

sql语句下 **update、delete、insert** 需要事务

1在事务执行完成后,确认执行无误且成功,就可以使用**commit**把内存中执行的结果,提交到物理内存中

2如果在事务执行过程中,发生了错误,则可以使用rollback命令回滚到上一个事务操作



#####################################华丽的分割线###################################################
1、登录 mysql -uroot -p
2、启动 sudo service mysql start
3、退出 exit
三日来上课文档的mysql表数据查询语句：
- 基础查询
4、查询所有列 
select * from 表名;
5、查询指定列 
select 字段1，字段2 ... from 表名;

- 条件查询
6、查询 条件1 ，且 条件2的记录 
select * from 表名 where 字段="条件1" and 字段="条件2";
select * from student where gender="女" and age="20";
7、查询 条件1 ，或 条件2的记录
select * from 表名 where 字段="条件1" or 字段="条件2";
select * from student where gender="女" or age="20";
8、查询 条件分别是 1,2,3的记录（可以用or），不为123的用not in
select * from 表名 where 字段 in("条件1"，"条件2","条件3");
select * from student where id in("1","2","3");
9、查询 字段 为（是） 条件X 的记录
select * from 表名 where 字段 is "条件";
select * from student where age is null;
10、查询 字段 在 条件之间 的记录
select * from 表名 where 字段 between 条件1 and 条件2; (等价：大于等于条件1 小于等于条件2)
select * from student where age between 15 and 20;
11、查询 字段 非 条件的记录
select * from 表名 where 字段!="条件";
select * from student where gender!="male";
- 模糊查询
12、查询 字段 由 n个字符 组成的记录
select * from 表名 where 字段 like "___..."(n个下划线)
select * from  student where name like "____"
13、查询开头\结尾\包含不指定位数时候，用%
select * from student where name like "a%"/"%a"/"%a%"
- 字段控制查询
13、去重查询 
select distinct 字段名 from 表名；
select distinct id from student；
14、字段别名查询
select name as 姓名 from student；   as可以省略
15、排序
select * from  表 order by  xxx   asc升序   desc降序
select * from student order by age desc,id asc;
16、聚合函数
count()统计字段不为空的记录（行数）
select count(*/名) [名] from     [名]的作用是让显示在结果表的内容
select count(*)  from student where age>20;
sum() 指定字段求和
select sum（字段）from 表名;
select sum(age) from student;
max()指定列中最大值
min()指定列中最小值
select max(age),min(age) from student;
avg()求平均值
select avg(字段) from 表名；   常与分组结合使用
select avg(age) from student;

> 查询关键字的书写顺序：select 聚合函数  from where order by
- 分组查询
  group by   having
  查询 各个 字段 的个数
  select count(*) from 表名 group by 字段名;

  查询每个部门的部门编号和每个部门的工资和
  select deptno,sum(sal) from emp group by deptno;

  查询每个部门的部门编号和每个部门的人数
  select deptno,count(*) from emp group by deptno;

  查询每个部门的部门编号和每个部门工资大于1500的人数
  select deptno,count(*) from emp where sal>1500 group by deptno;

  查询工资总和大于7000的部门编号以及工资和
  select deptno,sum(sal) from emp group by deptno having sum(sal)>7000;

  查询工资大于1500，工资总和大于6000的部门编号和工资和
  select deptno,sum(sal) from emp where sal>1500 group by deptno having sum(sal)>6000;

   - 分页查询

     查询4行记录，起始行从0开始
     select * from emp limit 0,4;

> > > > > > ​        查询语句书写顺序：select----》from---》where---》group by-----》having-----》order by----->limit

​	查询语句的执行顺序：from----》where-----》group by----》having----》select-----》order by----》limit

   - 多表查询

     **内连接**
     mysql> select s.stuid,s.stuname,c.score,c.courseid  from student s join score c on s.stuid=c.stuid;

     隐式连接

     select  s.stuid,s.stuname,c.score,c.courseid from student s,score c where s.stuid=c.stuid;

     

     查询成绩大于70的学生记录
     #方式一
     mysql> select  s.stuid,s.stuname,c.score,c.courseid from student s,score c where s.stuid=c.stuid and c.score>70;

     #方式二
     #也是内连接，只不过相当于是方言，join on相当于是普通话
     mysql> select  s.stuid,s.stuname,c.score,c.courseid from student s,score c where s.stuid=c.stuid and score>70;

     #方式三
     mysql> select s.stuid,s.stuname,c.score,c.courseid  from student s join score c on s.stuid=c.stuid where score>70;

     **外连接**

     #左外连接
     mysql> select s.stuid,s.stuname,c.score,c.courseid  from student s left join score c on s.stuid=c.stuid;

     #右外连接
     #参照为c
     mysql> select s.stuid,s.stuname,c.score,c.courseid  from student s right join score c on s.stuid=c.stuid;

     **子查询**

     #1.查询和scott在同一个部门的员工
     #思路：先查询scott所在的部门，然后根据部门查找所有的信息
     mysql> select deptno from emp where enname='scott';

     #2.查询工资高于joens的员工信息
     #思路：先查询jones的工资，然后根据jones查询其他的员工信息
     mysql> select * from emp where sal>(select sal from emp where enname='jones');

     #3.查询工资高于30号部门所有人的员工信息
     #思路：先查询30号部门中的最高工资，根据最高工资查询其他的员工信息
     mysql> select * from emp where deptno=30;

     #4.查询工作类型和工资与martin完全相同的员工信息
     #思路：先查询martin的工作类型和工资，然后再查询其他的员工信息
     mysql> select * from emp where (job,sal) in(select job,sal from emp where enname='martin');

   - 









