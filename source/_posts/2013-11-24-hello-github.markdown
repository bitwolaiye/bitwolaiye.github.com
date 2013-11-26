---
layout: post
title: "Hello Github!"
date: 2013-11-24 14:59:24 +0800
comments: true
categories: 
---

我很早之前就看过了github的page的功能，并且尝试搭了下，但是一直也没有坚持写下去。这次有点想法，于是参照了破船和唐巧写的内容，重新搭一次。后续我准备在这个平台正式的写点技术总结，不同于我在另一个平台上的流水，这边应该是一些对别人也有些用的内容，同时也是对自己的总结。
这篇是一个开头，同时我也将在这片里面持续的记录利用github page搭建博客的过程以及遇到的问题。


## 一、搭建

大部分都参照于
[利用Octopress搭建一个Github博客 from 破船之家](http://beyondvincent.com/blog/2013/08/03/108-creating-a-github-blog-using-octopress/)
而完成，同时辅助参考
[象写程序一样写博客：搭建基于github的博客 from 唐巧](http://blog.devtang.com/blog/2012/02/10/setup-blog-based-on-github/)

模板我用的不是默认的，而是和破船之家一样的 [greyshade](https://github.com/shashankmehta/greyshade)

评论我用了多说。可以选择的还有有言。

后续的内容还需要继续摸索，慢慢更新。

## 二、心得
<br/>
### 2.1 fabric
我习惯用python的fabric来替代一些需要记忆的脚本，比如在这里我记不住发布的命令，于是每次翻别人blog太麻烦，于是我就用fabric。

安装fabric

	$ pip install fabric
	
在当前目录创建fab.py

	from fabric.api import local
	def deploy(msg=''):
	    local('rake generate')
		local('git add .')
	    local('git commit -am "%s"' % msg)
	    local('git push origin source')
	    local('rake deploy')
	    
保存退出

然后我需要发布时只需要输入

	$ fab deploy:msg='these message is commit to github'
	
即可