---
layout: post
title: "迭代器与生成器"
date: 2014-01-16 11:55:36 +0800
comments: true
published: false
categories: Python iterative generator recursive
---

### Recursive 与 Iterative

首先得说递归和迭代的区别，我对此实际理解不深，趁这个机会再补补。


面试的时候还有几个问题没答上来，好吧，这块实际是完全模糊的。

1. 迭代器组成有几个必要条件？
	a. 实现.next()  这个方法返回下一个值，如果没有了就返回StopIteration异常
	b. 实现.__iter__()  这个方法返回self
2. Python的协程怎么工作？
	暂时不准备搞明白了，因为似乎平时工作用不上。大致理解就是和多线程相关的DD。 