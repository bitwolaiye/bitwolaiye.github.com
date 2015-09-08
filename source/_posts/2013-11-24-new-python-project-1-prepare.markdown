---
layout: post
title: "新python项目--1.准备工作"
date: 2013-11-24 18:13:09 +0800
comments: true
published: true
categories: 
---

## 一、准备python环境

我的工作机是Mac.而目标服务器应该大都是Ubuntu或者centOS，这2者我更倾向于Ubuntu，所以我将把Mac和Ubuntu下的步骤记录下来。

### 1.1 包管理

Mac下我用的包管理是brew，Ubuntu自带的包管理是apt-get。

pip是python下的包管理，pip如何装请自行google或者bing？

### 1.2 virtualenv
为什么需要virtualenv？

其实之前我一直没有用，但这次可能要用的一些类库的版本可能和现在已有的项目不大一样，所以试试吧。

安装virtualenv及创建一个虚拟环境命令如下：（pyCharm似乎自带这个功能，我没用过，同时需要在pyCharm中简单配置下才可以支持虚拟环境）

	$ sudo pip install virtualenv virtualenvwrapper
	$ export WORKON_HOME=~/work/python_project
	$ mkdir -p $WORKON_HOME
	$ source /usr/local/bin/virtualenvwrapper.sh
	$ mkvirtualenv env1

需要退出虚拟环境时

	$ deactivate
	
需要进入虚拟环境时

	$ cd ~/work/python_project/env1
	$ source bin/activate
	

相关参考：

* [virtualenv](https://pypi.python.org/pypi/virtualenv)
* [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)是一个对虚拟环境的一个包装工具。


### 1.3 django
之前我用的是django1.3后来升级到1.4，新装的环境一看已经是1.6了，所以这个项目将在django1.6的基础上继续

	$ pip install django

### 1.4 djangorestframework
djangorestframework是我找到的一个在django的基础上提供restful api的框架。版本2.3.9。

	$ pip install djangorestframework
	
### 1.5 MySQLdb

db是MySQL，python下需要安装MySQLdb。

Ubuntu：

	$ sudo apt-get install python-MySQLdb
	
我发现Ubuntu的virtualenv下直接装也有问题，所以还是源码包试试吧。[下载地址](http://downloads.sourceforge.net/project/mysql-python/mysql-python-test/1.2.4b4/MySQL-python-1.2.4b4.tar.gz?r=&ts=1386213050&use_mirror=jaist)

不过Ubuntu下不用改那个配置了，直接敲命令安装即可。

	
Mac:

*更新：*

直接建一个软链

	ln -s /usr/local/mysql/bin/mysql_config /usr/local/bin/mysql_config

因为反复要用，老下包然后改太麻烦

mac下的安装似乎有点问题，简单的pip是装不了的，给个参考按[mac os x 10.8 安装python-mysqldb血泪史](http://blog.csdn.net/intel80586/article/details/8487682) 的步骤做就可以了。我装的是MySQL-python-1.2.4b4，其实也不算太麻烦，就是下的源码包，然后修改下配置文件site.cfg

	mysql_config = /usr/local/mysql/bin/mysql_config
	
如果报错
	
	error: command 'cc' failed with exit status 1
	
则运行

	export CFLAGS=-Qunused-arguments
	export CPPFLAGS=-Qunused-arguments
	
来源[stackoverflow](http://stackoverflow.com/questions/21638444/error-command-cc-failed-with-exit-status-1-mysqldb-installation-on-mac)
	
修改完了运行命令

	$ python setup.py clean
	$ python setup.py build
	$ python setup.py install

就可以了，验证是否安装ok，在python下

	>>> import MySQLdb
	
没异常就是ok了。


## 二、数据库
数据库选择MySQL，此处不再详述安装等过程。关键是这块环境我是已有的，懒得再捣腾，你懂的。

## 三、版本库	
我在github上建立了一个开源项目[django_rest_api_sample](https://github.com/bitwolaiye/django_rest_api_sample) 用于存储代码。

将项目clone到本地

	$ cd env1
	$ git clone https://github.com/bitwolaiye/django_rest_api_sample.git
	
