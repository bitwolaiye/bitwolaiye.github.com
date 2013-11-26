---
layout: post
title: "新python项目--1.准备工作"
date: 2013-11-24 18:13:09 +0800
comments: true
published: true
categories: 
---

## python环境

我的工作机是Mac.而目标服务器应该大都是Ubuntu或者centOS，这2者我更倾向于Ubuntu，所以我将把Mac和Ubuntu下的步骤记录下来。

### pip

Mac下我用的包管理是brew，Ubuntu自带的包管理是apt-get。

pip是python下的包管理，pip如何装请自行google或者bing？

### virtualenv
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
	$ ./bin/activate
	

相关参考：

* [virtualenv](https://pypi.python.org/pypi/virtualenv)
* [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)是一个对虚拟环境的一个包装工具。


### django
之前我用的是django1.3后来升级到1.4，新装的环境一看已经是1.6了，所以这个项目将在django1.6的基础上继续

	$ pip install django

### djangorestframework
djangorestframework是我找到的一个在django的基础上提供restful api的框架。版本2.3.9。

	$ pip install djangorestframework

## DB
db选择MySQL，此处不再详述安装等过程。关键是这块环境我是已有的，懒得再捣腾，你懂的。

## 版本库	
我在github上建立了一个开源项目[django_rest_api_sample](https://github.com/bitwolaiye/django_rest_api_sample) 用于存储代码。

将项目clone到本地

	$ cd env1
	$ git clone https://github.com/bitwolaiye/django_rest_api_sample.git
	
