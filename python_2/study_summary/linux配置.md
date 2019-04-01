## 一、前置准备

```
sudo apt-get update

sudo apt-get install man gcc  make  lsof ssh openssl tree vim dnsutils iputils-ping -y

sudo apt-get install net-tools psmisc sysstat curl telnet traceroute wget libbz2-dev libpcre3 -y

sudo apt-get install libpcre3-dev  libreadline-dev libsqlite3-dev libssl-dev llvm -y

sudo apt-get install zlib1g-dev git mysql-server mysql-client zip  p7zip -y

sudo apt-get install nginx -y

sudo apt-get install libc6-dev gcc -y

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm
```



## 二、配置python和pip，跳过到第三步

```
sudo apt-get install python3-pip -y
pip3 install --upgrade pip
pip3 --version
```

会有报错，根据提示修改指定路径下的配置文件

```
# 修改前
form pip import main
if __name__ == '__main__':
	sys.exit(main())

# 修改后
from pip import __main__
if __name__ == '__main__':
	sys.exit(__main__._main())
```



## 三、配置python虚拟开发环境

### 1、配置pyenv

```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# 将安装路径写入 ~/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# 配置立即生效
source  ~/.bashrc

# 更新一下
pyenv update

cd ~/.pyenv
mkdir cache
# 或者 mkdir ~/.pyenv/cache

wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz -P  ~/.pyenv/cache/
# 路径可更改，版本按需修改

pyenv install 3.6.5 -v
# 版本需对应，否则会从github下载指定版本号

# 更新pyenv数据库
pyenv rehash

# 列出所有已安装的版本
pyenv versions

# 版本切换
pyenv global 3.6.5

# 版本验证
python  # 或 python --version

# 删除指定的python版本
pyenv uninstall 3.6.5
```

### 2、配置virtualenv

```
# 安装 virtualenv
pip install virtualenv

# 创建虚拟开发环境
pyenv virtualenv [版本号(pyenv version查询)] vir_name

# 切换进虚拟开发环境
pyenv activate vir_name

# 切出虚拟开发环境
pyenv deactivate vir_name
```

```
# 下载pyenv-virtualenv
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

# 写入环境变量
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# 重启shell
```

### 3、后备方法，可行性待验证

```
# 后备方案
# 安装virtualenvwrapper
pip install virtualenvwrapper

# 配置环境变量
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/workspace
source /usr/local/bin/virtualenvwrapper.sh

source ~/.bash_profile

# 注：若在pip下载后，找不到/usr/local/bin/virtualenvwrapper.sh路径的文件
# 使用 find / -name virtualenvwrapper.sh 寻找该文件路径

# 创建虚拟环境
mkvirtualenv [版本] vir_name

# 进入虚拟环境
workon vir_name

# 切出虚拟环境
deactivate
```

### 4、在win下搭载虚拟开发环境

```
# 以下依赖于virtualenv，使用在windows平台
# 在win平台下使用virtualenv,virtualenvwrapper-win

# 下载virtualenvwrapper
pip install virtualenvwrapper-win

# 创建虚拟环境
mkvirtualenv [指定版本，默认为当前版本] vir_name
# 默认会在C:\user\username\Envs下创建虚拟环境
# 在环境变量中添加一个名为'WORKON_HOME',值为'想要保存的路径'即可更改默认路径

# 查看当前所有venv环境
workon

# 进入虚拟环境
workon vir_name

# 切出虚拟环境
deactivate

# 删除虚拟环境
rmvirtualenv vir_name

# 复制虚拟开发环境
cpvirtualenv old_vir_name new_vir_name
```





## 四、数据库配置

```
# 修改配置文件，允许远程访问

# 备份
sudo cp /etc/mysql/mysql.conf.d/mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf.bak

# 修改配置文件
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf

    # 修改字符集(可选)
    [mysqld]
    user            = mysql
    pid-file        = /var/run/mysqld/mysqld.pid
    socket          = /var/run/mysqld/mysqld.sock
    port            = 3306
    basedir         = /usr
    datadir         = /var/lib/mysql
    tmpdir          = /tmp
    lc-messages-dir = /usr/share/mysql
    skip-external-locking
    character_set_server = utf8  # 在此处添加

    bind-address          = 127.0.0.1
    # 将这句语句注释

# 重启服务
sudo service mysql restart

# 创建用户
use mysql;
create user '用户名'@'服务器地址' identified by '密码';
# 服务器地址指访问提出访问的地址，非本服务器地址
# 用 '%' 指任意的访问地址

# 删除用户
drop user  '用户名'@'服务器地址'

# 修改密码

# mysql5.7前
set password = password('123456');
# mysql5.7
use mysql;
update user set authentication_string=password('234') where user='root';

# 刷新，立即生效
flush privileges;

# 授权
grant 权限  on 数据库.表  to '用户名'@'服务器地址'

eg: grant all on *.* to 'dd'@'localhost';
# *.* 为所有数据库的所有表，第一个*指数据库，第二个*指该数据库中的表
# all为所有权限，包括（select, update, delete, alter, insert）

# 回收授权
revoke select on test.stars from '用户名'@'服务器地址';

# 数据库备份
mysqldump -uroot -p database_name > ~/file_name.sql;
# 数据库恢复
mysql -uroot -p database_name < ~/file_name.sql;
```



## *、其他

```
screen -S 窗口名字
screen -r  窗口名  进入指定窗口
screen -X -S 窗口名 quit 退出会话
常用快捷键:
    ctrl + a + d   #退出会话
    ctrl + a + c  #创建一个新窗口
    ctrl + a + n  #显示下一个窗口
    ctrl + a + p  #显示上一个窗口
    ctrl + a + w  #显示所有窗口
    ctrl + a + k  #关闭当前窗口,先按ctl+a,然后松开，1秒后按k

# 生成 ssh
ssh-keygen -t rsa -C "your_email@example.com"
```

