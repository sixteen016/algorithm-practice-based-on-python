# HashSet——哈希集合

## 原理
哈希集合的主要使用场景是**去重**，可以在O(1)的时间复杂度内判断一个元素是否存在，可以在O(1)的时间复杂度内插入一个元素，可以在O(1)的时间复杂度内删除一个元素。

而以上所有操作都可以通过哈希表来实现，因此哈希集合实际上是基于哈希表来实现的，是哈希表的一个封装。

大部分高级程序设计语言都提供了哈希集合的实现，例如Python中的set类型，Java中的HashSet类，C++中的unordered_set类等。
## 实现代码
```python
class HashSet:
    def __init__(self):
        # 底层字典
        self.map = {}

    # 增
    def add(self, key):
        self.map[key] = True

    # 删
    def remove(self, key):
        if key in self.map:
            del self.map[key]

    # 查
    def contains(self, key):
        return key in self.map

    def _size(self):
        return len(self.map)

```
