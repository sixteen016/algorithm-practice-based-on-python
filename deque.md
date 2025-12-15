# Deque——双端队列
## 原理
双端队列是一种在队列的基础上进行扩展的队列，它允许在队列的两端都进行插入和删除操作。

```python
# 数组实现双端队列
class Deque:
    def __init__(self):
        self.items = []

    # 队头插入
    def add_front(self, val):
        self.items.insert(0,val)
    
    # 队尾插入
    def add_end(self, val):
        self.items.append(val)

    # 队头删除
    def remove_front(self):
        self.items.pop(0)
    
    # 队尾删除
    def remove_end(self):
        self.items.pop()

    # 队头查看
    def peek_front(self):
        return self.items[0]

    # 队尾查看
    def peek_end(self):
        return self.items[-1]
```