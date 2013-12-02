---
layout: post
title: "gevent_vs_tornado"
date: 2013-12-02 10:45:39 +0800
comments: true
published: false
categories: 
---

## 

在写上篇tornado做websocket的同时我搜了下，发现不仅仅是node.js有个Socket.IO，在Python领域还有gevent等挺不错的框架，甚至有人表示，tornado只是土豪facebook的一个明星产品，而实际上没有那么好。于是我看了下面这篇文章[gevent vs. Tornado](http://mmopy.com/gevent-vs-tornado/) 我觉得内容还是很中肯的。现在优性能的服务器其实追其根源都是利用了linux下的epoll特性，对非阻塞的应用有了很好的提升，包括nginx、tornado、gevent。所以从原理来说gevent和tornado是同源，那么其实他们之间性能如果有差异，可能也不大。在差距不大的情况下，不如对比下他们之间的可用性，文中提出，tornado对异步编程的支持并不好，相对来说gevent会好不少。这点是打动我的，因为我用tornado写过些简单的异步，其中的逻辑复杂，很难掌控。后面我准备再用gevent再实现个chatroom。


gevent

gevent-websocket

gevent-socketio

上来就找到了这3个，似乎需要用到这3个，那么对于这3个是什么分别进行了解下吧。

