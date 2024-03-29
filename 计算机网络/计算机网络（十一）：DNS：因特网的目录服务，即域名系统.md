主机的一种识别方式是主机名，如cnn.com，但由于主机名可能由不定长的字母数字组成，路由器很难处理，由此主机也可以使用所谓的IP地址进行识别。
域名系统可以将IP地址和主机名进行映射。
一个IP地址由四个字节组成，并有严格的层次结构，每个字节（32位）都被句点分隔开，表示了0-255的十进制数字。
由于主机名中还有别名和真实名，故必须使用IP地址。

## 1、DSN提供的服务：域名->ip地址的转换

DNS协议是应用层协议，因为：
①、使用CS模式在通信的端系统之间运行
②、在通信的端系统之间通过下面的端到端运输层协议传送DNS报文
DNS是一种能够进行主机名到IP地址转换的目录服务。包括：
①、一个由分层的DNS服务器实现的分布式数据库（很多名字服务器组成的层次结构）
②、一个允许主机查询分布式数据库的应用层协议（名字服务器之间和客户端的应用层协议，实现名字解析）
DNS通常是运行在BIND软件的UNIX机器，DNS协议运行在UDP之上，使用53号端口。
DNS通常由其他应用层协议（SMTP和FTP）所使用，用于将用户提供的主机名解析为IP地址。过程如下：
①、同一台用户主机上运行着DNS应用的客户机端
②、该浏览器从URL中抽取出主机名，并将这个主机名传给DNS应用的客户机端
③、该DNS客户机向DNS服务器发送一个包含主机名的请求
④、该DNS客户机收到一份回答保温，其中包含对应于主机名的IP地址
⑤、一旦该浏览器接收到来自DNS的IP地址，可以向由该IP地址定位的HTTP服务器发起一个TCP连接。
除了进行主机名到IP地址的转换，DNS还提供了一些重要的服务：
①、主机别名：有复杂主机名的主机可以拥有一个或者多个别名，这种情况下真实的复杂主机名称为规范主机名。主机别名比主机规范名更容易记忆，应用程序可以调用DNS来获得主机别名对应的规范主机名以及主机的IP地址。
②、邮件服务器别名：邮箱地址可能也有别名，由此电子邮件应用程序可以调用DNS，对提供的邮件服务器别名进行解析，以获得该主机的规范主机名和IP地址。实际上MX记录允许一个公司的邮件服务器和web服务器使用相同的别名。
③、负载分配：繁忙的站点被冗余分配在多台服务器上，每台服务器运行在不同的端系统上，有着不同的IP地址，而IP地址集合对应于同一个规范主机名。DNS通过旋转这些IP地址在集合中的顺序，调整web服务器的负载分配。DNS的旋转同样可以用于邮件服务器，由此，多个邮件服务器可以具有相同的别名。

## 2、DNS工作机理概述：

DNS的一种简单设计方式是在因特网上使用一个DNS服务器，该服务器包含所有的映射。客户机直接将所有查询直接发往单一的DNS服务器，该DNS服务器直接对所有的查询客户机作出相应。但这种集中式设计的问题有：
①、单点故障：DNS服务器崩溃导致整个因特网崩溃
②、通信容量
③、远距离的集中式数据库：严重的时延
④、维护：为所有的因特网主机保留记录，需要频繁更新
总的来说，完全没有可拓展能力，因此，DNS采用了分布式的设计方案。

### a、分布式、层次数据库：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200408200249352.png)
有3种类型的DNS服务器：
①、根DNS服务器：因特网上有13个根DNS服务器，是冗余的服务器集群，以提供安全性和可靠性，互相镜像备份，可能有时间差。
②、顶级域（TLD）服务器：负责顶级域名（com\org\net等）和所有国家的顶级域名（uk\fr等）
③、权威DNS服务器：在因特网上具有公共课访问主机的每个权威机构必须提供公共可访问的DNS记录，将主机名映射为IP地址，由组织机构的权威DNS服务器负责保存这些DNS记录。
以上三种的交互的具体的过程如下：以www.a.com为例
①、客户机首先与根服务器之一联系，它将返回顶级域名com的TLD服务器的IP地址。
②、客户机与这些TLD服务器之一联系，它将返回权威服务器的IP地址。
③、客户机联系权威服务器之一，它将返回主机名www.a.com的IP地址。
除了以上三种，还有一种本地DNS服务器。并不属于DNS服务器的层次结构。每一个ISP都有一台本地DNS服务器（也叫默认名字服务器），当主机与某个ISP相连时，该ISP提供一台主机的IP地址，该主机具有一台或多台其本地DNS服务器的IP地址（通常通过DHCP）。当主机发出DNS请求时，该请求被发往本地DNS服务器，它起着代理的作用。
从主机开始的DNS过程如下：
①、请求主机向本地DNS服务器发送一个DNS查询报文发出请求
②、本地DNS服务器将该报文转发到根服务器
③、根服务器处理其顶级域名并返回负责顶级域名的TLD服务器
④、本地DNS服务器将该报文转发到TLD服务器
⑤、TLD服务器处理其域名（DHCP）并返回相应的权威DNS服务器
⑥、本地DNS服务器将该报文转发到权威DNS服务器
⑦、权威DNS服务器返回该域名的IP地址
⑧、本地DNS服务器将IP地址返回到请求主机
这个DNS过程中利用了递归查询和迭代查询。从主机向本地DNS发出的查询是递归查询，而后继的三个查询是迭代查询。理论上讲，任何DNS查询既可以是迭代的也可以是递归的。

### b、DNS缓存：

为了改善时延性能并减少在因特网上到处传输的DNS报文数量，DNS广泛使用了缓存技术。
在请求链中，当一个DNS服务器接收到一个DNS回答时，DNS服务器能将回答中的信息缓存在本地存储器。这个缓存包含在回答中的任何信息，包括主机名/地址对。因为主机和主机名与IP地址间的映射不是永久地，所以DNS服务器在一段时间后（通常为两天）将丢弃缓存的信息。
本地DNS服务器也可以缓存TLD服务器的IP地址（不仅仅是权威服务器的IP地址）。因此允许本地DNS绕过查询链中的根DNS服务器。

## 3、DNS记录和报文

实现DNS分布式数据库的所有DNS服务器共同存储着资源记录RR，RR提供了主机名到IP地址的映射。
资源记录是一个包含了下列字段的四元组：name、value、type、TTL
TTL是该记录的生存时间，他决定了资源记录应当从缓存中删除的时间。
name和value的值取决于type：
①、type=A，则name是主机名，value是该主机名的IP地址。提供了一条标准的主机名到IP地址的映射
②、type=NS，则name是域，value是知道如何获取该域中主机地址的权威DNS服务器的主机名，即负责解析域的权威主机名。
③、type=CNAME，则value是别名为name的主机对应的规范主机名。
④、type=MX，则value是别名为name的邮件服务器的规范主机名。
指定主机名的权威DNS服务器必有一条包含该主机名的A记录。
如果DNS服务器不是某个主机名的权威DNS服务器，那么将包含一条NS记录，对应于包含主机名的域；同时会包含一条A记录，提供了NS记录的value字段中的DNS服务器的IP地址。

### a、DNS报文：

DNS只有DNS查询报文和DNS回答报文。DNS只有这两种报文，并且查询和回答报文有着相同的格式。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200408200256527.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODUxNzQ0,size_16,color_FFFFFF,t_70)
DNS报文中各个字段的寓意如下：
①、前12字节是首部区域，分几个字段：
第一个字段是一个16bit的标识符，用来标识该查询，会被复制到对查询的回答报文中，以便让客户机匹配发送的请求和接收到的回答。
第二个字段是标志字段，中有若干标志，包括1bit的‘查询/回答’标志位、1bit的‘权威的’标志位（回答报文）、1bit的‘希望递归’标志位（请求报文）、1bit的‘递归可用’标志位（回答报文）。
剩余字段是四个‘数量’字段，指出了在首部后4类数据区域出现的数量。
②、问题区域，包含着正在查询的信息：
名字字段，指出正在被查询地主机名字
类型字段，指出正在被询问的问题类型（A或MX）
③、回答区域，仅回答报文，包含了对最初请求的名字的资源记录：
可以包含多条RR，因为一个主机名可以对应多个IP地址
④、权威区域，包含了其他权威DNS服务器的记录
⑤、附加区域，包含了其他一些有帮助的记录。

### b、在DNS数据库中插入记录：

首先，在注册登记机构注册域名。注册登记机构是一个商业实体，它验证域名的唯一性，将域名输入DNS数据库。
当向注册登记机构注册域名时，需要向该机构提供基本权威DNS服务器和辅助权威DNS服务器的名字和IP地址。注册登记机构将所有的IP地址输入到对应的TLD服务器。
确保用于web服务器的类型A资源记录和用于邮件服务器的类型MX记录被输入到你的权威DNS服务器中。
