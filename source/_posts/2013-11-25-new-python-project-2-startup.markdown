---
layout: post
title: "新python项目--2.框架搭建"
date: 2013-11-25 10:36:41 +0800
comments: true
published: false
categories: 
---

## 一、新建项目

运行如下命令创建django项目

	$ django-admin.py startproject pet_api
	$ python manage.py startapp pet

## 二、建立模型
	
之前我参与的项目一般都是dba会提前做好模型，然后我在django上写出对应的代码，在这个项目里，我准备使用[South](http://south.aeracode.org) 来做db的版本控制等。

在做这些之前先准备db环境。
在mysql中创建用户及database，登陆mysql后执行以下：

	create database pet;
	create user 'pet'@'localhost' identified by 'pet';
	create user 'pet'@'%' identified by 'pet';
	grant all on pet.* to 'pet'@'localhost';
	grant all on pet.* to 'pet'@'%';
	
在pet_api的settings.py里找到DATABASES，加入

	'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pet', # Or path to database file if using sqlite3.
        'USER': 'pet', # Not used with sqlite3.
        'PASSWORD': 'pet', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }

安装south

	$ pip install south
	
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
	
目前我在models.py里加入了

* User 用户信息
* Follow 关注信息
* Fan 粉丝信息
* Friend 双向关注后成为好友
* Info 用户发布的信息，可以带一张图或者短文本
* Feed 用户的信息流，他关注的用户发布的Info将进入他的信息流。
* Comment 用户对Info进行评论
* News 评论的同时将通知原po主

最开始的版本将带有这些基本功能。

此时命令行运行

	$ manage.py runserver
	
在浏览器中打开 http://127.0.0.1:8000/ 然后你将看到

> It worked!


## 三、简单应用
之前我用的Django REST framework是0.4.0，现在已经是2.3.9，整个变化已经很大了，甚至是在settings.py里以前的名字是djangorestframework，现在是rest_framework。

[Django REST framework](http://django-rest-framework.org)

感叹完毕，在django项目中启用包需要在settings.py里的INSTALLED_APPS里加上，Django REST framework的名字是rest_framework。

我看了下django rest framework的guide，整个和我当时的框架差太多，所以我需要点时间重新熟悉。另外似乎django1.6和1.4差距同样的大。



