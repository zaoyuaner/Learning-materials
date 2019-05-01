#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
队列：先进先出
'''
import collections

queue = collections.deque()
queue.append("1")
queue.append("2")
queue.append("3")

print(queue.popleft())