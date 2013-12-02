---
layout: post
title: "使用tornado搭建websocket服务"
date: 2013-12-01 12:53:51 +0800
comments: true
published: false
categories: 
---

## 准备
<br/>

	$ export WORKON_HOME=~/work/python_project
	$ mkvirtualenv env2
	$ pip install tornado
	$ cd ~/work/python_project/env2
	$ mkdir chatroom
	
接着打开pyCharm（我的python IDE)，并配置好Project Interpreter -> Python Interperters。

版本控制应该是用github，但暂时先跳过这一步。

## 第一步
<br/>

按tornado的介绍创建了app.py文件，再创建handlers.py，后续的handlers里放实现代码。虽然实际上写一个文件里也可以，不过分开应该更清晰。

说到默认端口，tornado的默认端口一定是facebook某个华裔的程序员写的。为啥呢？8888，一听就是那种。。。不说了，你懂的。想当年，我参与的一个团队的终端机的的默认密码就是6个8.相比之下，django是8000，rails是3000，octopress（Jekyll）是4000，就让人感觉普通青年了许多。

简单几行代码后就可以运行看效果了

	$ python app.py
	
但运行了发现也没法测试，浏览器直接看了没啥反应。所以还得做个Python的客户端来试试。

	$ pip install websocket-client
	
增加个client.py来放客户端代码，copy websocket-client的示例代码，然后运行之
	
	$ python client.py
	Sending 'Hello, World'...
	Sent
	Reeiving...
	Received 'You said: Hello, World'

ok，至少可以跑起来了。

创建个github项目来存放下当前代码。[项目地址](https://github.com/bitwolaiye/chatroom_sample)

我创建了tag来表示每一步的代码，其中step1就表示当前的代码。后面以此类推。

如何创建tag我参考了[git tag](http://xxw8393.blog.163.com/blog/static/37256834201010301043564/)

	$ git tag -a step1 11e463d00dbe93e896a5e81f6c5737edb5c48f04
	$ git push origin step1
	


## 第二步
<br/>

第一步只完成了后台可以接受websocket，但还不能由后台管理连接，同时当前的chatroom还只是个单机版的东西。接着我们要做到2个用户登录进来，他们可以向对方say hello。

tip:

在app.py的application中加入debug=true，那么他会在你改变代码的同时服务更新，省去了你ctrl+c然后再运行的麻烦。

### server

我在handler里存了下connection，也同时在open时加入list，close移出list，这样当有一个用户说了点什么时，我可以在on_message事件里直接将信息发给另一个用户。

### client

我新建了个class User，user可以say可以show。

同时在main里初始化2个用户，2个用户都有timer来循环获取发给他的消息。同时我还模拟了他们的对话，最后的一个sleep 10秒是为了不让主进程退出。
	
到此step2完成。
