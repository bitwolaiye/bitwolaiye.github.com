---
layout: post
title: "Fibonacci in Python"
date: 2014-01-16 10:02:20 +0800
comments: true
categories: Python, interview
---

这是一道面试的题目，实际很简单，但，我没很好答上来。因为不够pythonic。

我的实现

	fib_list = [1, 1]
	def _f():
	  global fib_list
	  fib_list.append(sum(fib_list[-2:]))
		
	def fib(index):
	  if index < 0:
	    return -1
	  global fib_list
	  if len(fib_list) < index:
	    for i in xrange(index - len(fib_list)):
	      _f()
	  return fib_list[index - 1]
	  
			
当时我还写了另一个，但回来发现是错的。

搜了下，有这2个文章有更好的解法

[Fibonacci in Python](http://www.zacharyfox.com/blog/fibonacci-project/fibonacci-in-python)

~~[用Python实现Fibonacci函数](http://www.cr173.com/html/6631_1.html)~~

后一篇基本可以不看，就属于卖萌型的。回字有几种写法实际上只是程序员卖弄的技巧。


	def fibonacci(n):
	  a,b = 0,1
	  for i in range(0,n):
	    a,b, = b,a+b
	  return a
	  
	  
这个基本就是比较简洁的了。

还有一种Generator的实现方式

	def fib():
	  a, b = 0, 1
      while 1:
        yield a
        a, b = b, a + b
        
    a = fib()
    a.next()
    for i in range(10):
      print a.next(),

但我得辩解下，对于非科班的程序员，在工作中我很少需要关注该数列的实现方式，往往是根据实际的业务现想。像背诵一样的默写出这个实现实际上没有太大意义。

不过还没完，我搜到了http://en.literateprograms.org/Category:Fibonacci_numbers

这个对该问题还有更加深入的解释。包括如何利用数学上的知识更快的算出结果。

