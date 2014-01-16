---
layout: post
title: "准备Python工程师面试"
date: 2014-01-16 09:38:10 +0800
comments: true
categories: Python
---

之前在招聘网站放过简历，于是前2天有面试电话打来，是一家业内号称卖“理念”的公司，也的确还算有名气的公司，自称大公司中的小公司。职位是Python工程师。心想去去也好，看看自己到底是个什么水平，呆一家公司9年时间，都不知道外面的世界是什么样的了，偶尔会狂妄自大，偶尔会妄自菲薄。

比如说去这家公司面试心里就很紧张，Python实际只用了2年时间，期间一直仅仅忙于实现功能即可，对很多细节都是一知半解，程序能通就Ok。所以我还挺认真的开始找找资料，复习下。~~（当然还有个原因对方说有笔试，囧。心里很担心万一全不会多丢人啊！！）~~

这个总结是去之前写的，把它发出来的同时实际已经去过了，结果面试结果的感觉是不咋地，但也有好处，就是达到了认清自己、找到缺点的目的。ok，这块回头再写。

### pyc pyo pyd
http://www.cnblogs.com/dkblog/archive/2009/04/16/1980757.html

###什么是pyc文件
pyc是一种二进制文件，是由py文件经过编译后，生成的文件，是一种byte code，py文件变成pyc文件后，加载的速度有所提高，而且pyc是一种跨平台的字节码，是由python的虚拟机来执行的，这个是类似于JAVA或者.NET的虚拟机的概念。pyc的内容，是跟python的版本相关的，不同版本编译后的pyc文件是不同的，2.5编译的pyc文件，2.4版本的 python是无法执行的。

###什么是pyo文件
pyo是优化编译后的程序 python -O 源文件即可将源程序编译为pyo文件 

###什么是pyd文件
pyd是python的动态链接库。

###为什么需要pyc文件
这个需求太明显了，因为py文件是可以直接看到源码的，如果你是开发商业软件的话，不可能把源码也泄漏出去吧？所以就需要编译为pyc后，再发布出去。当然，pyc文件也是可以反编译的，不同版本编译后的pyc文件是不同的，根据python源码中提供的opcode，可以根据pyc文件反编译出 py文件源码，网上可以找到一个反编译python2.3版本的pyc文件的工具，不过该工具从python2.4开始就要收费了，如果需要反编译出新版本的pyc文件的话，就需要自己动手了（俺暂时还没这能力^--^）,不过你可以自己修改python的源代码中的opcode文件，重新编译 python，从而防止不法分子的破解。

### py文件在运行时会产生pyc文件，用于缓存编译后代码 不完全正确 ？？ why？？

## zen of python

The Zen of Python, by Tim Peters 

* Beautiful is better than ugly. 
* Explicit is better than implicit. 
* Simple is better than complex. 
* Complex is better than complicated. 
* Flat is better than nested. 
* Sparse is better than dense. 
* Readability counts. 
* Special cases aren't special enough to break the rules. 
* Although practicality beats purity. 
* Errors should never pass silently. 
* Unless explicitly silenced. 
* In the face of ambiguity, refuse the temptation to guess. 
* There should be one-- and preferably only one --obvious way to do it. 
* Although that way may not be obvious at first unless you're Dutch. 
* Now is better than never. 
* Although never is often better than *right* now. 
* If the implementation is hard to explain, it's a bad idea. 
* If the implementation is easy to explain, it may be a good idea. 
* Namespaces are one honking great idea -- let's do more of those!

翻译

* 美比丑好
* 直言不讳比心照不宣好
* 简单比复杂好
* 复杂比难以理解好
* 平面的比嵌套的好
* 错落有致比密密匝匝的好
* 可读性很重要
* 虽然实用比纯粹更重要 但特殊情况不能特殊到打破规律
* 永远别让错误悄悄地溜走 除非是你故意的
* 碰到模棱两可的地方，绝对不要去作猜测
* 什么事情都应该有一个，而且最好只有一个显而易见的解决办法
* 虽然刚开始的时候，这个办法可能不是那么的显而易见，但谁叫你不是荷兰人
* 有些事情不理不睬可能会比过一会解决要好
* 但最好是现在就解决
* 如果一个想法实现起来很困难，那它本身就不是一个好想法
* 如果一个想法实现起来很容易，那它或许就是一个好想法
* 命名空间是一个很了不起的想法,让我们多多使用吧

## 排序

    str_list = ['a', 'b', 'c']
    str_list.sort(key=lambda x:x.lower(),reverse=True)
    
## 随机

    import random
    random.random()
    random.sample(range(10), 2)
    l = range(10)
    random.shuffle(l)
    

## 文件

    with open('1.txt', 'w') as f:
        f.write('abc')
        
    with open('1.txt', 'r') as f:
        for s in f:
            print s
            
    import os
    os.listdir('.')
    
    import shutil
    shutil.copyfile('1.txt', '2.txt')
    
    os.remove('2.txt')
            
    
## .items() .iteritems()

一个生成全部，一个是迭代器

## 常用类型常用方法

    dir(list)
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    
    dir(tuple)
    ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
    
    dir(dict)
    ['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
    
    dir(set)
    ['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
    
    dir(str)
    ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    
### list
list可以作为栈

list可以作为队列

list到list的映射。??不明白

any和all在list中的使用。 

    l = range(10)
    all(n<10 for n in l)
    any(n==0 for n in l)

list与for的结合，相当于高级语言中的foreach功能。

对list的enumerate与for的结合，相当于高级语言中的for功能。

list的嵌套使用，相当于多维数组。

del相当于list本身的remove，都可以用来删除list中的元素。

    l = range(10)
    del l[9]

zip

### tuple
tuple相当于是不可修改的list，所以同时也不具有list的很多修改的方法，例如append，insert，remove等；但是tuples仍然可以使用count，index等查找方法。

使用 t2 = (2,4,8)来定义tuple，也可以使用list来定义tuple如 l = [1,2,3] 和 t = tuple(l)

### set
set的定义使用{}。

可以将list使用set显示的转化为set。

可以用in来判断指定元素是否存在于set中。

set于for结合使用，相当于foreach。

set可以进行|，&，^,-操作。

### dict
dictionary使用{1 : 'tom', 2 : 'bill'}来定义，也可以使用dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])来从list定义dictionary。

[]=来增加新的值。

del来删除指定的key和value。

in用来查找key是否存在。

### 语法糖

    isinstance([], list)
    isinstance((), tuple)
    isinstance({}, dict)
    isinstance({1:2}, dict)
    isinstance({1}, set)
    
## Pythonic

只可意会不可言传！

或者 参见 

    import this
    
## help

参看方法参数

    help(''.index)

## lambda

好处

匿名函数, 方便, 类函数式, 写回调方便

### filter

filter(function, sequence)：对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）返回：

### map
map(function, sequence) ：对sequence中的item依次执行function(item)，见执行结果组成一个List返回：

### reduce

reduce(function, sequence, starting_value)：对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用，例如可以用来对List求和：


## range xrange

一个列表 ~~一个迭代器~~ xrange

## yield

？？？


## python支持多线程，能够单进程无缝发挥多路CPU的优势

支持，不能够

为什么不能？并行计算？Python的线程实际上是使用单核在运行。

https://wiki.python.org/moin/ParallelProcessing

> 在大多数系统上，Python同时支持消息传递和基于线程的并发编程。尽管大多数程序员熟悉的往往是线程接口，但实际上Python线程受到的限制有很多。尽管最低限度是线程安全的，但Python解释器还是使用了内部的GIL(Global Interperter Lock,全局解释器锁定)，在任意指定的时刻只能在一个处理器上运行。尽管GIL经常是Python社区中争论的热点，但在可以预见的将来它都不可能消失。

号称来源于《python参考手册》但我没去证实。


## 在python中，使用for从列表中删除元素是错误的做法，会导致漏删元素。正确的做法是使用python内置的filter函数
<br/>

## 题目 考虑Decorator 装饰器

	def wrap_info (f):
	    b = {"b":10};
	    def inner_func (*p, **k):
	        print b['b'], p, k;
	        b['b'] += 1;
	        f(*p, **k);
	    return inner_func;

	def info (s):    print "func info: %s" % s;

	if __name__ == "__main__":
	    f1 = wrap_info (info);
	    f1 ("a");
	    f2 = wrap_info (info);
	    f1 ("b");
	    f2 ("c");

[Python装饰器学习（九步入门）](http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html)



## 题目 纯卖弄！

	a="a=%s%s%s;print a%%(chr(34),a,chr(34));";print a%(chr(34),a,chr(34));
	
## 题目 单例模式

	class singleton (object):
	    """ 单例模式的实现 """
    	def __new__ (cls, **kargs):
	    	if '_instance' not in cls.__dict__:
	            cls._instance = object.__new__ (cls, **kargs);
	        return cls._instance;

## 动态加载 反射等

[Python自省（反射）指南](http://www.cnblogs.com/huxi/archive/2011/01/02/1924317.html)

### 访问元数据

### 使用inspect


## unicode

	s.decode('utf-8')
	u.encode()

## 传值？传引用？传值！

[stackoverflow](http://stackoverflow.com/questions/986006/python-how-do-i-pass-a-variable-by-reference/986145#986145)

简单来说，你在方法里重新对一个参数赋值可能不会改变。

建议是return出来然后改变

    class PassByReference:
      def __init__(self):
        self.variable = 'Original'
        self.Change(self.variable)
        print self.variable
      def Change(self, var):
        var = 'Changed'

    p = PassByReference()
    p.Change(p.variable)
    print p.variable # Original
    
改为

    class PassByReference:
      def __init__(self):
        self.variable = 'Original'
        self.Change()
        print self.variable
      def Change(self):
        self.variable = 'Changed'

    p = PassByReference()
    p.Change()
    print p.variable # Changed
    
或者

    class PassByReference:
      def __init__(self):
        self.variable = 'Original'
        self.Change(p.variable)
        print self.variable
      def Change(self, var):
        return 'Changed'

    p = PassByReference()
    p.variable = p.Change(p.variable)
    print p.variable # Changed

甚至是变成一个数组传进去等等，但真不是个好办法了。太丑！

## 进阶链接


[Python Interview Question and Answers](http://ilian.i-n-i.org/python-interview-question-and-answers/)

## Python的内存是使用的heap？

http://docs.python.org/2/c-api/memory.html

[阮一峰对堆和栈的解释](http://www.ruanyifeng.com/blog/2013/11/stack.html)

## virtualenv

	source activate
	deactivate
	
	pip freeze > filename
	pip install -r filename
