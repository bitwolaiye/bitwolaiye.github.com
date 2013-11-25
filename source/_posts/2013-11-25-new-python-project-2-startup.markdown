---
layout: post
title: "新python项目--2.框架搭建"
date: 2013-11-25 10:36:41 +0800
comments: true
published: false
categories: 
---

## 创建新的django project

	$ django-admin.py startproject pet_api
	$ python manage.py startapp pet
	
### db
db我选择mysql，安装

Ubuntu：

	$ sudo apt-get install python-MySQLdb
	
Mac:

mac下的安装似乎有点问题，简单的pip是装不了的，给个参考按[mac os x 10.8 安装python-mysqldb血泪史](http://blog.csdn.net/intel80586/article/details/8487682) 的步骤做就可以了。我装的是MySQL-python-1.2.4b4，其实也不算太麻烦，就是下的源码包，然后修改下配置文件

	mysql_config = /usr/local/mysql/bin/mysql_config

就可以了，验证是否安装ok，在python下

	>>> import MySQLdb
	
没异常就是ok了。

	
之前我参与的项目一般都是dba会提前做好模型，然后我在django上写出对应的代码，在这个项目里，我准备使用[South](http://south.aeracode.org) 来做db的版本控制等。

	$ pip install south
	
在pet_api的settings.py里找到DATABASES，加入

	'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pet', # Or path to database file if using sqlite3.
        'USER': 'pet', # Not used with sqlite3.
        'PASSWORD': 'pet', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
	
在pet_api的settings.py文件中找到INSTALLED_APPS，在里面加上pet和south

先将基础的表创建

	$ python manage.py syncdb

此时再在pet的models.py里加入一个简单的model
	
	$ python manage.py schemamigration pet --initial
	
最后执行

	$ python manage.py migrate pet
	
后面如果要更新model只需要在modes.py里修改了，然后执行

	$ python manage.py schemamigration pet --auto
	$ python manage.py migrate pet
	
如果想直接执行manage.py而不需要敲python可以

	$ sudo chmod 744 manage.py
	
在mysql中创建用户及database，登陆mysql后执行以下：

	create database pet;
	create user 'pet'@'localhost' identified by 'pet';
	create user 'pet'@'%' identified by 'pet';
	grant all on pet.* to 'pet'@'localhost';
	grant all on pet.* to 'pet'@'%';
	

