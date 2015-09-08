---
layout: post
title: "初试Node.js"
date: 2014-02-20 14:29:48 +0800
comments: true
categories: 
---

公司准备弄个微信服务号，于是几天前开始看了看微信服务号能干的事情。个人感觉，微信并没有给服务号提供什么神级api，仅仅是被动式的客服，也不知道为什么被各大科技博客吹上了天。干不了多少也得干，好吧，搜了下github，star最多的wechat的project都是node.js的，其次是php、python。前几天弄blockexplorer.com的时候被php伤了，一时半会不想碰，python的似乎也不太成熟。众多原因下，我鼓起勇气，node.js就node.js吧。

## 环境

mac下的环境是ok的，之前用rails的js模块就是node.js的。

	brew install nodejs
	
	
IDE选择WebStorm，Jetbrains真是。。。唉，真心好公司。



ubuntu 12.04下似乎默认apt-get安装的是旧版本

	apt-get install python-software-properties
	apt-add-repository ppa:chris-lea/node.js
	apt-get update
	
	apt-get install nodejs
	apt-get install npm
	
	
上面的方法似乎没用，因为apt-get的源里的npm依赖旧版本的nodejs。

https://gist.github.com/dwayne/2983873

