# LinkedHashMap——哈希链表（用链表增强哈希表）
现在，我们已经知道了HashMap是一种可以在O(1)的事件内可以实现元素的查询、插入和删除等操作。但是，HashMap是一种无序的集合，这就导致了一个问题：我们无法按照插入的顺序来遍历HashMap的元素。
而根据我们对于Python的了解，我们知道Python中的字典是一种有序的集合，可以按照插入的顺序来遍历字典的元素。
而这正是LinkedHashMap的作用。
## 原理
我们知道链表和数组是可以保证元素的有序性的。
而HashMap本身是一种对元素的映射，我们可以在HashMap的基础上，添加一个链表来维护元素的插入顺序。

## 代码实现
```python
class LinkedHashMap:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.pre = None
            self.next = None

    def __init__(self):
        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.map = dict()


    # 查
    def get(self, key):
        if key not in self.map:
            return None
        node = self.map[key]
        return node.value

    
    # 增
    def put(self, key, value):
        if key not in self.map:
            node = self.Node(key, value)
            self.map[key] = node
            self.add_last_node(node)
            return 
        self.map[key].value = value

    # 删
    def remove(self, key):
        if key not in self.map:
            return 
        node = self.map[key]
        del self.map[key]
        self.remove_node(node)

    def contains_key(self, key):
        return key in self.map

    def keys(self):
        key_list = []
        node = self.head.next
        while node != self.tail:
            key_list.append(node.key)
            node = node.next
        return key_list

    def add_last_node(self, node):
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node

    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
```
