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


