---
layout: post
title: "新python项目--1.准备工作"
date: 2013-11-24 18:13:09 +0800
comments: true
published: false
categories: 
---

## python环境

我的工作机是Mac，而目标服务器应该大都是Ubuntu或者centOS，这2者我更倾向于Ubuntu，所以我将把Mac和Ubuntu下的步骤记录下来。

### pip

Mac下我用的包管理是brew，Ubuntu自带的包管理是apt-get。

pip是python下的包管理，如何装？

### virtualenv
为什么需要virtualenv？

其实之前我一直没有用，但这次可能要用的一些类库的版本可能和现在已有的项目不大一样，所以试试吧。

	$ sudo pip install virtualenv virtualenvwrapper
	$ export WORKON_HOME=~/work/python_project
	$ mkdir -p $WORKON_HOME
	$ source /usr/local/bin/virtualenvwrapper.sh
	$ mkvirtualenv env1

需要退出

	$ deactivate
	
需要进入

	$ cd ~/work/python_project/env1
	$ ./bin/activate
	

* [virtualenv](https://pypi.python.org/pypi/virtualenv)
* [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)

virtualenvwrapper是一个对虚拟环境的一个包装工具。

### django
之前我用的是django1.3后来升级到1.4，新装的环境看到已经是1.6了，也就是这个项目将在django1.6的技术上继续

	$ pip install django

### djangorestframework
djangorestframework是我找到的一个在django的基础上提供restful api的框架。版本2.3.9。

	$ pip install djangorestframework
	
### github
我在github上建立了一个开源项目https://github.com/bitwolaiye/django_rest_api_sample 用于存储代码。

将项目clone到本地

	$ cd env1
	$ git clone https://github.com/bitwolaiye/django_rest_api_sample.git
	
