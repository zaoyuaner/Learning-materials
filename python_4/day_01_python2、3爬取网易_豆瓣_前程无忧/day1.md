# day1 

## 虚拟环境

### 为什么需要虚拟环境：

到目前位置，我们所有的第三方包安装都是直接通过`pip install xx`的方式进行安装的，这样安装会将那个包安装到你的系统级的`Python`环境中。但是这样有一个问题，就是如果你现在用`Django 1.10.x`写了个网站，然后你的领导跟你说，之前有一个旧项目是用`Django 0.9`开发的，让你来维护，但是`Django 1.10`不再兼容`Django 0.9`的一些语法了。这时候就会碰到一个问题，我如何在我的电脑中同时拥有`Django 1.10`和`Django 0.9`两套环境呢？这时候我们就可以通过虚拟环境来解决这个问题。

### 虚拟环境原理介绍：

虚拟环境相当于一个抽屉，在这个抽屉中安装的任何软件包都不会影响到其他抽屉。并且在项目中，我可以指定这个项目的虚拟环境来配合我的项目。比如我们现在有一个项目是基于`Django 1.10.x`版本，又有一个项目是基于`Django 0.9.x`的版本，那么这时候就可以创建两个虚拟环境，在这两个虚拟环境中分别安装`Django 1.10.x`和`Django 0.9.x`来适配我们的项目。

### 安装`virtualenv`：

`virtualenv`是用来创建虚拟环境的软件工具，我们可以通过`pip`或者`pip3`来安装：

```shell
    pip install virtualenv
    pip3 install virtualenv
```

### 创建虚拟环境：

创建虚拟环境非常简单，通过以下命令就可以创建了：

```shell
    virtualenv [虚拟环境的名字]
```

如果你当前的`Python3/Scripts`的查找路径在`Python2/Scripts`的前面，那么将会使用`python3`作为这个虚拟环境的解释器。如果`python2/Scripts`在`python3/Scripts`前面，那么将会使用`Python2`来作为这个虚拟环境的解释器。

### 进入环境：

虚拟环境创建好了以后，那么可以进入到这个虚拟环境中，然后安装一些第三方包，进入虚拟环境在不同的操作系统中有不同的方式，一般分为两种，第一种是`Windows`，第二种是`*nix`：

1. `windows`进入虚拟环境：进入到虚拟环境的`Scripts`文件夹中，然后执行`activate`。
2. `*nix`进入虚拟环境：`source /path/to/virtualenv/bin/activate`
   一旦你进入到了这个虚拟环境中，你安装包，卸载包都是在这个虚拟环境中，不会影响到外面的环境。

### 退出虚拟环境：

退出虚拟环境很简单，通过一个命令就可以完成：`deactivate`。

### 创建虚拟环境的时候指定`Python`解释器：

在电脑的环境变量中，一般是不会去更改一些环境变量的顺序的。也就是说比如你的`Python2/Scripts`在`Python3/Scripts`的前面，那么你不会经常去更改他们的位置。但是这时候我确实是想在创建虚拟环境的时候用`Python3`这个版本，这时候可以通过`-p`参数来指定具体的`Python`解释器：

```shell
    virtualenv -p C:\Python36\python.exe [virutalenv name]
```

------

### virtualenvwrapper：

`virtualenvwrapper`这个软件包可以让我们管理虚拟环境变得更加简单。不用再跑到某个目录下通过`virtualenv`来创建虚拟环境，并且激活的时候也要跑到具体的目录下去激活。

#### 安装`virtualenvwrapper`：

1. *nix：`pip install virtualenvwrapper`。 
2. windows：`pip install virtualenvwrapper-win`。

#### `virtualenvwrapper`基本使用：

1. 创建虚拟环境：

   ```shell
    mkvirtualenv my_env
   ```

   那么会在你当前用户下创建一个`Env`的文件夹，然后将这个虚拟环境安装到这个目录下。
   如果你电脑中安装了`python2`和`python3`，并且两个版本中都安装了`virtualenvwrapper`，那么将会使用环境变量中第一个出现的`Python`版本来作为这个虚拟环境的`Python`解释器。

2. 切换到某个虚拟环境：

   ```shell
    workon my_env
   ```

3. 退出当前虚拟环境：

   ```shell
    deactivate
   ```

4. 删除某个虚拟环境：

   ```shell
    rmvirtualenv my_env
   ```

5. 列出所有虚拟环境：

   ```shell
    lsvirtualenv
   ```

6. 进入到虚拟环境所在的目录：

   ```shell
    cdvirtualenv
   ```

#### 修改`mkvirtualenv`的默认路径：

在`我的电脑->右键->属性->高级系统设置->环境变量->系统变量`中添加一个参数`WORKON_HOME`，将这个参数的值设置为你需要的路径。  重点

#### 创建虚拟环境的时候指定`Python`版本： 重点   

在使用`mkvirtualenv`的时候，可以指定`--python`的参数来指定具体的`python`路径：

```
    mkvirtualenv --python==C:\Python36\python.exe qf_env
```





# 爬虫前奏

## 爬虫的实际例子：

1. 搜索引擎（百度、谷歌、360搜索等）。
2. 伯乐在线。
3. 惠惠购物助手。
4. 数据分析与研究（数据冰山知乎专栏）。
5. 抢票软件等。

## 什么是网络爬虫：

1. 通俗理解：爬虫是一个模拟人类请求网站行为的程序。可以自动请求网页、并数据抓取下来，然后使用一定的规则提取有价值的数据。

2. 专业介绍：[百度百科](https://baike.baidu.com/item/网络爬虫/5162711?fr=aladdin)。

   蜘蛛网: 

   ​	搜索引擎  蜘蛛 

   ​	往:互联网 

## 为什么要学习爬虫 

1. 项目需要 获取更多的数据   并且进行分析  形成分析报告 提供战略 分析 
2. 进行seo优化    搜索引擎喜欢爬经常更新的网站 爬取数据让网站内容每天更新    

## 爬虫设计思路  

1 .确定爬取的url地址    放到队列中 

2.通过http\https 协议获取对应的页面 

3.提取有用的数据  进行存储

4.如果页面中还有其它的url 那么我们再执行第二步  

​		

## 通用爬虫和聚焦爬虫：

1. 通用爬虫：通用爬虫是搜索引擎抓取系统（百度、谷歌、搜狗等）的重要组成部分。主要是将互联网上的网页下载到本地，形成一个互联网内容的镜像备份。

   百度、360、搜狗 抓取网页 、数据存储、数据处理、提供检索服务 （提供接口）

   robots 协议  ：可以限制 百度、360等 可以爬什么  不可以爬哪些  

   淘宝 不允许百度爬取  

   仅仅是一个协议  完全可以不遵守

   如何让百度等爬取你的网站  需要提交robots协议  

   SEO: 

   ​	pagerank值 （流量、点击率）值越高 排名越靠前 

   ​	百度、360竞价排名  

   通用爬虫的缺点: 

   ​	1.抓取的数据太多了  好多没用的 

   ​	2.不会根据用户的需求 爬取数据  	

2. 聚焦爬虫： 也叫专业爬虫  主题爬虫  是面向特定需求的一种网络爬虫程序，他与通用爬虫的区别在于：聚焦爬虫在实施网页抓取的时候会对内容进行筛选和处理，尽量保证只抓取与需求相关的网页信息。

   1. 根据自己的需求  设计爬取程序 然后抓取对应的数据即可 

      通过聚焦爬虫如何抓取到数据？

   ​	1.每个网页都有一个 统一资源定位符  URL 

   ​	2.网页都是有标签 组成 

   ​	3.遵循http、https协议 

   

## 为什么用Python写爬虫程序：

1. PHP：PHP是世界是最好的语言，但他天生不是做这个的，而且对多线程、异步支持不是很好，并发处理能力弱。爬虫是工具性程序，对速度和效率要求比较高。
2. Java：生态圈很完善，是Python爬虫最大的竞争对手。但是Java语言本身很笨重，代码量很大。重构成本比较高，任何修改会导致代码大量改动。爬虫经常要修改采集代码。
3. C/C++：运行效率是无敌的。但是学习和开发成本高。写个小爬虫程序可能要大半天时间。
4. Python：语法优美、代码简洁、开发效率高、支持的模块多。相关的HTTP请求模块和HTML解析模块非常丰富。还有Scrapy和Scrapy-redis框架让我们开发爬虫变得异常简单。



django、flask、tornado 

## 爬虫需要掌握什么? 

1.HTML 

2.re\XPATH \beautifulsoup4（提取html、xml的库）\jsonpath\pyquery (网页解析库) 用来解析服务器的响应内容  

3.动态模拟浏览器的行为 selenium 模拟浏览器 加载 js 等  获取验证码这些   

4.构建分布式  scrapy+redis 

5.twisted  异步网络框架  



### 爬虫 、反爬虫、反反爬虫   博弈最后赢家 必定是爬虫

爬虫：最后赢的人   最后不是页面结构复杂、数据量大 而是 反爬虫人员   

反爬虫:(面子、竞争对手)
	1.验证码

​	2.js压缩混淆加密

​	3.动态加载数据 替代静态页面   

​	4.将get 改为post  

反反爬虫:

​	1.伪造用代理   user-agent

​	2.用代理  

​	

## 准备工具：

1. Python3.6开发环境。
2. Pycharm 2017 professional版。
3. 虚拟环境。`virtualenv/virtualenvwrapper`。



# http协议和Chrome抓包工具

fiddler简单用法: 

​	1.页面分为左右

​		 左边 会话窗口  

​		右边分为上下:

​				上面是请求 request

​				下面是响应 response

​	2.左下角黑色框 输入指令 

​	   select html

​	  select json /javascript/image

​	3.禁止抓包  file 第一个 取消对号即可 

​	4.清空会话  点击X号 remove all 即可

​	5.抓取https  tools-》options-》https 选择左边前三个   右边 actions 添加证书到信任机构  

 6. 配置允许远程连接   tools-》options-》connections  左边倒数三个选中  右边第一列三个选中   

    

## 什么是http和https协议： 基于TCP/IP协议  

HTTP协议：全称是`HyperText Transfer Protocol`，中文意思是超文本传输协议，是一种发布和接收HTML页面的方法。服务器端口号是`80`端口。 HTTPS协议：是HTTP协议的加密版本，在HTTP下加入了SSL层。服务器端口号是`443`端口

http:80      ssh:22       pop3:110    memcached:11211  

https 443  scp： 22    mysql:3306   mongodb:27017  

ftp:21       smtp:25    redis:6379 

0~127 都被系统占用了  

自定义端口号 ：1024以前的 需要root权限      



## 在浏览器中发送一个http请求的过程：

1. 当用户在浏览器的地址栏中输入一个URL并按回车键之后，浏览器会向HTTP服务器发送HTTP请求。HTTP请求主要分为“Get”和“Post”两种方法。
2. 当我们在浏览器输入URL <http://www.baidu.com> 的时候，浏览器发送一个Request请求去获取 <http://www.baidu.com> 的html文件，服务器把Response文件对象发送回给浏览器。
3. 浏览器分析Response中的 HTML，发现其中引用了很多其他文件，比如Images文件，CSS文件，JS文件。 浏览器会自动再次发送Request去获取图片，CSS文件，或者JS文件。
4. 当所有的文件都下载成功后，网页会根据HTML语法结构，完整的显示出来了。

## url详解：

`URL`是`Uniform Resource Locator`的简写，统一资源定位符。 一个`URL`由以下几部分组成：

```
    scheme://host:port/path/?query-string=xxx#anchor
```

- **scheme**：代表的是访问的协议，一般为`http`或者`https`以及`ftp`等。
- **host**：主机名，域名，比如`www.baidu.com`。
- **port**：端口号。当你访问一个网站的时候，浏览器默认使用80端口。
- **path**：查找路径。比如：`www.jianshu.com/trending/now`，后面的`trending/now`就是`path`。
- **query-string**：查询字符串，比如：`www.baidu.com/s?wd=python`，后面的`wd=python`就是查询字符串。
- **anchor**：锚点，后台一般不用管，前端用来做页面定位的。

在浏览器中请求一个`url`，浏览器会对这个url进行一个编码。除英文字母，数字和部分符号外，其他的全部使用百分号+十六进制码值进行编码。

## 常用的请求方法：

get、post、delete 、put 、patch  

在`Http`协议中，定义了八种请求方法。这里介绍两种常用的请求方法，分别是`get`请求和`post`请求。

1. `get`请求：一般情况下，只从服务器获取数据下来，并不会对服务器资源产生任何影响的时候会使用`get`请求。
2. `post`请求：向服务器发送数据（登录）、上传文件等，会对服务器资源产生影响的时候会使用`post`请求。 以上是在网站开发中常用的两种方法。并且一般情况下都会遵循使用的原则。但是有的网站和服务器为了做反爬虫机制，也经常会不按常理出牌，有可能一个应该使用`get`方法的请求就一定要改成`post`请求，这个要视情况而定。

## 请求头常见参数：

在`http`协议中，向服务器发送一个请求，数据分为三部分，第一个是把数据放在url中，第二个是把数据放在`body`中（在`post`请求中），第三个就是把数据放在`head`中。这里介绍在网络爬虫中经常会用到的一些请求头参数：

1. `User-Agent`：浏览器名称。这个在网络爬虫中经常会被使用到。请求一个网页的时候，服务器通过这个参数就可以知道这个请求是由哪种浏览器发送的。如果我们是通过爬虫发送请求，那么我们的`User-Agent`就是`Python`，这对于那些有反爬虫机制的网站来说，可以轻易的判断你这个请求是爬虫。因此我们要经常设置这个值为一些浏览器的值，来伪装我们的爬虫。
2. `Referer`：表明当前这个请求是从哪个`url`过来的。这个一般也可以用来做反爬虫技术。如果不是从指定页面过来的，那么就不做相关的响应。
3. `Cookie`：`http`协议是无状态的。也就是同一个人发送了两次请求，服务器没有能力知道这两个请求是否来自同一个人。因此这时候就用`cookie`来做标识。一般如果想要做登录后才能访问的网站，那么就需要发送`cookie`信息了。

```
常⽤的请求报头
1.	Host
Host：对应⽹址 URL 中的 Web 名称和端⼝号，⽤于指定被请求资源的
Internet 主机和端⼝号，它通常从 HTTP URL 中提取出来的

2.	Connection
Connection：表示客户端与服务连接类型
    1.Client 发起⼀个包含  Connection:keep-alive   的请求，HTTP/1.1 使⽤keep-alive为默认值。
    2.Server 收到请求后：
    		如果 Server ⽀持 keep-alive，回复⼀个包含 Connection:keep-alive的响应，不关闭连接；
    		如果 Server 不⽀持 keep-alive，回复⼀个包含 Connection:close 的响应，关闭连接。
    3.如果 client 收到包含 Connection:keep-alive 的响应，向同⼀个连接发送下⼀个请求，直到⼀⽅主动关闭连接。keep-alive 在很多情况下能够重⽤连接，减少资源消耗，缩短响应时间，⽐如当浏览器需要多个⽂件时(⽐如⼀个 HTML⽂件和相关的图形⽂件)，不需要每次都去请求建⽴连接。

3.Upgrade-Insecure-Requests
	Upgrade-Insecure-Requests：升级不安全的请求，意思是会在加载 http 资 源时⾃动替换成 https 请求，让浏览器不再显示 https⻚⾯中的 http 请求警报。
HTTPS 是以安全为⽬标的 HTTP 通道，所以在 HTTPS 承载的⻚⾯上不允许出现 HTTP 请求，⼀旦出现就是提示或报错，但是很多⽹站对 https 没有技术概念，在填⼊的数据中不免出现 http 的资源

4.User-Agent User-Agent：是客户浏览器的名称，以后会详细讲。

5.Accept
        Accept：指浏览器或其他客户端可以接受的 MIME（Multipurpose Internet Mail Extensions（多⽤		途互联⽹邮件扩展））⽂件类型，服务器可以根据它判断并返回适当的⽂件格式。
        举例：
         Accept: */* ：表示什么都可以接收。
         Accept：image/gif  ：表明客户端希望接受 GIF 图像格式的资源；
         Accept：text/html  ：表明客户端希望接受 html⽂本。
         Accept:  text/html,  application/xhtml+xml;q=0.9,  image/*;q=0.8  ：表示
        浏览器⽀持的 MIME 类型分别是 html⽂本、xhtml 和 xml⽂档、所有的图像格式资源。
        q 是权重系数，范围 0 =< q <= 1，q 值越⼤，请求越倾向于获得其“;”之前的类型表示的内容。若没有指		定 q 值，则默认为 1，按从左到右排序顺序；若被 赋值为 0，则⽤于表示浏览器不接受此内容类型。
        Text：⽤于标准化地表示的⽂本信息，⽂本消息可以是多种字符集和或者多种格式的；Application：⽤于传		   输应⽤程序数据或者⼆进制数据。详细请点击

6.Referer
        Referer：表明产⽣请求的⽹⻚来⾃于哪个 URL，⽤户是从该 Referer⻚⾯访问到当前请求的⻚⾯。这个属		性可以⽤来跟踪 Web 请求来⾃哪个⻚⾯，是从 什么⽹站来的等。

7.Accept-Encoding
        Accept-Encoding：指出浏览器可以接受的编码⽅式。编码⽅式不同于⽂件格式，它是为了压缩⽂件并加速⽂			件传递速度。浏览器在接收到 Web 响应之后先解码，然后再检查⽂件格式，许多情形下这可以减少⼤量的下			载时间。
        举例：Accept-Encoding:gzip;q=1.0, identity; q=0.5, *;q=0
        如果有多个 Encoding 同时匹配, 按照 q 值顺序排列，本例中按顺序⽀持 gzip,
        identity 压缩编码，⽀持 gzip 的浏览器会返回经过 gzip 编码的 HTML⻚⾯。如 果请求消息中没有设置		这个域服务器假定客户端对各种内容编码都可以接受。

8.Accept-Language
        Accept-Langeuage：指出浏览器可以接受的语⾔种类，如 en 或 en-us 指英语，zh 或者 zh-cn 指中			⽂，当服务器能够提供⼀种以上的语⾔版本时要⽤到。
 

 

9.Accept-Charset
	Accept-Charset：指出浏览器可以接受的字符编码。
    举例：Accept-Charset:iso-8859-1,gb2312,utf-8
    ISO8859-1：通常叫做 Latin-1。Latin-1 包括了书写所有⻄⽅欧洲语⾔不可缺少的附加字符，英⽂浏览器的默认值是 ISO-8859-1. gb2312：标准简体中⽂字符集;
    utf-8：UNICODE 的⼀种变⻓字符编码，可以解决多种语⾔⽂本显示问题，从⽽实现应⽤国际化和本地化。
    如果在请求消息中没有设置这个域，缺省是任何字符集都可以接受。

10.Cookie
	Cookie：浏览器⽤这个属性向服务器发送 Cookie。Cookie 是在浏览器中寄存 的⼩型数据体，它可以记载和服	     务器相关的⽤户信息，也可以⽤来实现会话 功能。

11.Content-Type
	Content-Type：POST 请求⾥⽤来表示的内容类型。
    举例：Content-Type = Text/XML; charset=gb2312：
    指明该请求的消息体中包含的是纯⽂本的 XML 类型的数据，字符编码采⽤“gb2312”。


服务端	HTTP响应 HTTP 响应也由四个部分组成，分别是： 状态⾏ 、 消息报头 、 正⽂ 、 响 应
 

 


常⽤的响应报头(了解)
理论上所有的响应头信息都应该是回应请求头的。但是服务端为了效率，安全，还有其他⽅⾯的考虑，会添加相对应的响应头信息，从上图可以看到：
1.	Cache-Control：must-revalidate, no-cache,
	private。
 
    这个值告诉客户端，服务端不希望客户端缓存资源，在下次请求资源时，必须要从新请求服务器，不能从缓存副本中获取资源。
    Cache-Control 是响应头中很重要的信息，当客户端请求头中包含 Cache- Control:max-age=0 请求，明确表示不会缓存服务器资源时,Cache-
    Control 作为作为回应信息，通常会返回 no-cache，意思就是说，"那就不 缓存呗"。
    当客户端在请求头中没有包含 Cache-Control 时，服务端往往会定,不同的资源不同的缓存策略，⽐如说 oschina 在缓存图⽚资源的策略就是Cache-Control：max-age=86400,这个意思是，从当前时间开始，在
    86400 秒的时间内，客户端可以直接从缓存副本中读取资源，⽽不需要向服务器请求。
2.	Connection：keep-alive
    这个字段作为回应客户端的 Connection：keep-alive，告诉客户端服务器的
    tcp 连接也是⼀个⻓连接，客户端可以继续使⽤这个 tcp 连接发送 http 请求。

3.	Content-Encoding:gzip
    告诉客户端，服务端发送的资源是采⽤gzip 编码的，客户端看到这个信息后，应该采⽤gzip 对资源进⾏解码。
4.	Content-Type：text/html;charset=UTF-8
告诉客户端，资源⽂件的类型，还有字符编码，客户端通过 utf-8 对资源进
⾏ 解码，然后对资源进⾏html 解析。通常我们会看到有些⽹站是乱码的， 往往 就是服务器端没有返回正确的编码。
5. Date：Sun, 21 Sep 2014 06:18:21 GMT
 
这个是服务端发送资源时的服务器时间，GMT 是格林尼治所在地的标准时间。http 协议中发送的时间都是 GMT 的，这主要是解决在互联⽹上，不同时区在相互请求资源的时候，时间混乱问题。

6.	Expires:Sun, 1 Jan 2000 01:00:00 GMT
这个响应头也是跟缓存有关的，告诉客户端在这个时间前，可以直接访问缓存副本，很显然这个值会存在问题，因为客户端和服务器的时间不⼀定会都是相同的，如果时间不同就会导致问题。所以这个响应头是没有 Cache- Control：max-age=*这个响应头准确的，因为 max-age=date 中的 date 是个相 对时间，不仅更好理解，也更准确。

7.	Pragma:no-cache 这 个含义与 Cache-Control 等同。
8.	Server：Tengine/1.4.6
这个是服务器和相对应的版本，只是告诉客户端服务器的信息。
9.	Transfer-Encoding：chunked
这个响应头告诉客户端，服务器发送的资源的⽅式是分块发送的。⼀般分块发送的资源都是服务器动态⽣成的，在发送时还不知道发送资源的⼤⼩，所以采⽤分块发送，每⼀块都是独⽴的，独⽴的块都能标示⾃⼰的⻓度，最后
⼀块是 0⻓度的，当客户端读到这个 0⻓度的块时，就可以确定资源已经传输完了。

10.	Vary: Accept-Encoding
告诉缓存服务器，缓存压缩⽂件和⾮压缩⽂件两个版本，现在这个字段⽤处并不⼤，因为现在的浏览器都是⽀持压缩的。

```





## 常见响应状态码：

常见的http状态码

`100`：继续 客户端应当继续发送请求。客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。

`101`： 转换协议 在发送完这个响应最后的空行后，服务器将会切换到在Upgrade 消息头中定义的那些协议。只有在切换新的协议更有好处的时候才应该采取类似措施。

`102`：继续处理 由WebDAV（RFC 2518）扩展的状态码，代表处理将被继续执行。

`200`：请求成功 处理方式：获得响应的内容，进行处理.  重点

`201`：请求完成，结果是创建了新资源。新创建资源的URI可在响应的实体中得到 处理方式：爬虫中不会遇到

`202`：请求被接受，但处理尚未完成 处理方式：阻塞等待

`204`：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。 处理方式：丢弃

`300`：该状态码不被HTTP/1.0的应用程序直接使用， 只是作为3XX类型回应的默认解释。存在多个可用的被请求资源。 处理方式：若程序中能够处理，则进行进一步处理，如果程序中不能处理，则丢弃
`301`：永久重定向。比如在访问`www.360buy.com`的时候会重定向到`www.jd.com`。 重点

`302`：临时重定向。比如在访问一个需要登录的页面的时候，而此时没有登录，那么就会重定向到登录页面。 重点

`304`：请求的资源未更新 处理方式：丢弃，使用本地缓存文件

`400`：请求的`url`在服务器上找不到。换句话说就是请求`url`错误。重点

`401`：未授权 处理方式：丢弃

`403`：服务器拒绝访问，权限不够。重点

`404`：没有找到 处理方式：丢弃重点

`500`：服务器内部错误。可能是服务器出现`bug`了。  重点

`501`：服务器无法识别 服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。

`502`：错误网关 作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。

`503`：服务出错 由于临时的服务器维护或者过载，服务器当前无法处理请求。这个状况是临时的，并且将在一段时间以后恢复。

## Chrome抓包工具：

`Chrome`浏览器是一个非常亲近开发者的浏览器。可以方便的查看网络请求以及发送的参数。对着网页`右键->检查`。然后就可以打开开发者选项。

## fidder 

```
请求 (Request) 部分详解
1. Headers —— 显示客户端发送到服务器的 HTTP 请求的 header， 显示为一个分级视图，包含了 Web 客户端信息、Cookie、传输状 态等。
2. Textview——显示POST请求的body部分为文本。
3. WebForms——显示请求的GET参数和POSTbody内容。
4. HexView——用十六进制数据显示请求。
5. Auth——显示响应header中的Proxy-Authorization(代理身份验
证) 和 Authorization(授权) 信息.
6. Raw——将整个请求显示为纯文本。
7. JSON-显示JSON格式文件。
8. XML——如果请求的body是XML格式，就是用分级的XML树来
显示它。


响应 (Response) 部分详解

1. Transformer——显示响应的编码信息。
2. Headers——用分级视图显示响应的header。
3. TextView——使用文本显示相应的body。
4. ImageVies——如果请求是图片资源，显示响应的图片。
5. HexView——用十六进制数据显示响应。
6. WebView——响应在Web浏览器中的预览效果。
7. Auth——显示响应header中的Proxy-Authorization(代理身份验
证) 和 Authorization(授权) 信息。
8. Caching——显示此请求的缓存信息。
9. Privacy——显示此请求的私密(P3P)信息。
10. Raw —— 将整个响应显示为纯文本。
11. JSON-显示JSON格式文件。
12. XML —— 如果响应的 body 是 XML 格式，就是用分级的 XML 树
来显示它 。
  
```





##  urllib 库  

> 这是一个库  python用来操作url的模块   <https://docs.python.org/2.7/library/urllib2.html>

* urllib2   python2.7自带  不需要安装  导入即可    
* urllib2 在 python3中升级到了 urllib.request  



```python
# -*- coding:utf-8 -*-
import  urllib2

url = 'http://www.baidu.com/'
#urlopen需要三个参数
#url 你要抓取的url
#data 默认为None 为none说明get 请求  如果你data不为none 就认为是post请求
#timeout 超时时间
res = urllib2.urlopen(url, data=None)
#print res
#print res.read() #返回所有的内容
#print res.readline() #按照行返回
#print res.readlines() #返回所有的行
#print res.getcode() #获取客户端请求的状态
#print res.geturl() #获取请求的url
#print res.code
print res.read().decode('utf-8')
#encode
```



## 第一个反反爬  

```python
User-Agent 伪造请求头   http://www.jsons.cn/useragent/  User-Agent在线解析    


# -*- coding:utf-8 -*-

import urllib2

headers = {
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
#url后边要加上/
url = "http://www.baidu.com/"

#创建请求对象
res = urllib2.Request(url,headers=headers)

print res.get_full_url() #获取完整的url
print res.get_method() #获取请求方法
print res.get_header("User-agent") #获取 浏览器的名称
print res.get_host() #host名称
print res.get_type() #协议名称
res.add_header("Connection","keep-alive") #wang header头中添加请求信息

print res.get_header("Connection")

```



```python
模拟百度搜索  
# -*- coding:utf-8 -*-
import os
import urllib
import urllib2

# urllib 和 urllib2 的区别:
#urllib仅仅接收url  能用urlencode 进行编码  urllib.urlencode()
#urllib2 可以接收设置了 headers 的 Request类
#以上 就让我们经常两个搭配来使用

#https://www.baidu.com/s?wd=美女
def baidu_search(params):

    headers = {
        "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    }

    url = "http://www.baidu.com/s?"+params

    requests = urllib2.Request(url,headers=headers) #创建请求对象
    #print requests
    response = urllib2.urlopen(requests)  #把请求对象传给 requests
    #print response
    print response.read()  #读取内容  

    dir = './'
    os.chdir(dir)
    file = urllib2.urlopen(url).read()
    open('baidu.html',"wb").write(file)   #保存页面  
    print "OK"
if __name__ == "__main__":
    kw = raw_input("请输入要查找的内容")
    params = {
        'wd':kw      #拼接参数  
    }
    params = urllib.urlencode(params) #将字典传承字符串参数   
    baidu_search(params) 



```



## python3 爬虫 

```
import urllib
from urllib import request

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

#url
url = "http://www.baidu.com/"

#创建请求对象
req =urllib.request.Request(url,headers=headers)
#发送请求 获取响应
responses = urllib.request.urlopen(req)
#print(responses)#二进制
# print("*"*30)
# print(responses.read())
# print("*"*30)
print(responses.read().decode('utf-8'))#解码   
#字符串->字节   encode
#字节-> 字符串   decode  
```



```
python3模拟百度搜索
from urllib import request
import urllib.parse
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
#/s?wd=
kw = input("请输入关键字:")
params = {
    'wd':kw
}

#将字典解析成参数字符串
params=urllib.parse.urlencode(params)
print(params)

#创建url
url = 'http://www.baidu.com/s?'+params

#创建请求对象
requests= urllib.request.Request(url,headers=headers)
responses = urllib.request.urlopen(requests)

#print(responses.read().decode('utf-8'))
#print(responses.status)
print(responses.__dict__)

```



