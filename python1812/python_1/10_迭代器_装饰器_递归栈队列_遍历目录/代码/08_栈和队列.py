# 用于存储数据的线性表
# 栈：在表的一端进行插入和删除          先进后出,后进先出
#
# 队列：在表的一端进行插入，在表的另一端进行数据的删除(通的)      先进先出,后进后出

# 使用列表模拟一个栈
list1 = []
# 入栈 push
list1.append(1)
print(list1)
list1.append(2)
print(list1)
list1.append(3)
print(list1)

# 出栈 pop
list1.pop()     # 默认最后一个
print(list1)
list1.pop()
print(list1)
list1.pop()
print(list1)

# 模拟队列   先进先出
# 导入模块  collections
import collections

# 队列
queue = collections.deque([1,2,3,4])
print(queue)

#入队【存储数据】
queue.append(5)
print(queue)
queue.append(6)
print(queue)

#出队【获取数据】  popleft
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)