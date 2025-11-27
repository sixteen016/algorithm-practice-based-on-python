# Queue & Stack——队列与栈
## 原理
队列与栈都是从链表衍生出来的数据结构，不同的是，它们对数据的操作受到一定的限制。
* 队列(Queue): 先进先出，只能在队尾插入，队头删除
* 栈(Stack): 先进后出，只能在栈顶插入，栈顶删除

## 代码实现
```python

# 用链表作为底层的数据结构实现栈
# python的deque是就是双链表
from collections import deque
# 队列的基本API
class Queue:
    def __init__(self):
        self.list = deque()
    # 向队尾插入元素
    def push(self, val):
        self.list.append(val)

    # 从队头删除元素
    def pop(self):
        return self.list.popleft()
    
    # 查看队头元素
    def peek(self):
        return self.list[0]

    # 返回队列中元素的个数
    def size(self):
        return len(self.list)

# 栈的基本API
class Stack:
    def __init__(self):
        self.list = deque()


    # 向栈顶插入元素
    def push(self, val):
        self.list.append(val)

    # 从栈顶删除元素
    def pop(self):
        return self.list.pop()

    # 查看栈顶元素
    def peek(self):
        return self.list[-1]
         
    # 返回栈中元素的个数
    def size(self):
        return len(self.list)
```

```python
# 用数组作为底层的数据结构实现栈
# 数组实现栈的基本操作

# 用数组或者链表实现栈的API，都是将数组或者链表的末尾作为栈顶
# 这或许与数组或者链表本身的API有关，
# 数组或者链表的append()方法就是在末尾插入元素，
# 而pop()方法就是删除末尾元素
class Stack:
    def __init__(self):
        self.arr = []

    # 像栈顶插入元素
    def push(self, val):
        self.arr.append(val)

    # 从栈顶删除元素
    def pop(self):
        return self.arr.pop()

    # 查看栈顶元素
    def peek(self):
        return self.arr[-1]

    # 返回栈中元素的个数
    def size(self):
        return len(self.arr)


# 用数组作为底层的数据结构实现队列
# 数组实现队列的基本操作

class Queue:
    def __init__(self):
        self.arr = []

    # 向队尾插入元素
    def push(self, val):
        self.arr.append(val)

    # 从队头删除元素
    def pop(self):
        return self.arr.pop(0)

    # 查看队头元素
    def peek(self):
        return self.arr[0]

    # 返回队列中元素的个数
    def size(self):
        return len(self.arr)
```