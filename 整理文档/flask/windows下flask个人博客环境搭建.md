
> flask作为一个web微框架，需要某些实现的功能需要我们自己去选择相关技术。

## 一、环境搭建

### 系统环境
#### 安装解释器（注意环境变量——自己配置或者安装的时候勾选默认的添加到环境变量 Add勾选）
2. pycharm安装（个人版，学习用这破解方便很多）
   pycharm安装（社区版，不想付费的商用）

### 数据库安装
1. mysql安装
   - 官网下载：https://www.mysql.com/downloads/   可选5.7.25版本
     community => downloads => mysql community server => MySQL Community Server 5.7 => 选择对应的系统版本和（32/64）=> 无需注册下载
   - 找个合适的位置解压 得到mysql-5.7.25-winx64
   - cmd 模式下进入mysql的bin目录  输入安装命令mysqld -install
2、配置mysql
   - mysql-5.7.25-winx64 目录下添加配置文件
```
[mysqld]
# 设置3306端口
port=3306
# 设置mysql的安装目录（修改为自己的目录）
basedir=D:\Mylargeprogram\Mysql\mysql-5.7.25-winx64
# 设置mysql数据库的数据的存放目录
datadir=D:\Mylargeprogram\Mysql\mysql-5.7.25-winx64\data
# 允许最大连接数
max_connections=200
# 允许连接失败的次数。这是为了防止有人从该主机试图攻击数据库系统
max_connect_errors=10
# 服务端使用的字符集默认为UTF8
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
# 默认使用“mysql_native_password”插件认证
default_authentication_plugin=mysql_native_password
[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8
[client]
# 设置mysql客户端连接服务端时默认使用的端口
port=3306
default-character-set=utf8
```

**mysql 安装出错，提示“mysqld: Can't change dir to 'D:\MySQL\MySQL Server 5.7\data\'”**

   - 执行 mysqld --initialize-insecure 指令进行配置，安装路径会默认生成一个data文件夹
3. 安装mysql服务
   mysqld --install
4、启动mysql服务
   net start mysql

修改密码：（修改之前关闭服务net stop mysql）
- data文件夹中（.err文件）有密码的话可以先用随机密码登录之后，
  执行 set password for root@localhost = password('=');  修改密码（进入数据库 mysql> 下）

- data文件夹中没找到随机密码也不要慌：
  通过mysql -u root mysqld进入数据库
  执行 set password for root@localhost = password('=');  修改密码（进入数据库 mysql> 下）

然后启动mysql，正常使用

#### redis安装
- https://github.com/MicrosoftArchive/redis/releases/tag/win-3.2.100 
  下载.zip那个就行
- 合适位置解压
- redis-server 启动服务
- redis-cli   进入服务

### 虚拟环境搭建（virtualenv）
- 安装：pip install virtualenv
- 创建虚拟环境：建议环境代码分离（在合适的位置创建一个env目录用来存放虚拟环境）
  virtualenv --no-site-packages -p python.exe的路径(盘符开始) env_name
- 进入虚拟环境
  Windows下：activate          Mac/Ubuntu：source activate
- 退出虚拟环境：deactivate

### 安装环境依赖 requirement.txt
执行命令： pip install -r requirement.txt
flask
flask-blueprint
flask-script
flask-session
flask-sqlalchemy
redis

### 密码加密的导包
from werkzeug.security import generate_password_hash, check_password_hash


## 二、模型创建

## 三、模板拆分

## 四、业务逻辑处理

## 五、部署上线




























   
