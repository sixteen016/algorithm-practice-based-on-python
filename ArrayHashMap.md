# ArrayHashMap——哈希数组（用数组增强哈希表）
## 原理
试想一下，如何在哈希表的基础上增加一个API，可以在O(1)时间内实现随机返回一个随机键。
我们可以想到，如果每个键都有一个索引，那么我们就可以使用随机数，来随即返回一个键。
```python
import random 
def randomElement(arr: list[int]) -> int:
    return arr[random.randint(0, len(arr) - 1)]
```
实际上，这就是数组的原理，每个元素被选中的概率是相等的。但是，前提是数组的元素连续的。如果说，数组的元素不是连续的，而是有空洞的，我们可能会想到使用环形数组的原理，向某一个方向遍历，直到遇到第一个非空元素。但是，这样的时间复杂度是O(n)，不符合要求。


因为哈希表的元素是离散的，我们可能下意识地就会如上文这般思考，但实际上，哈希数组的元素一定是保证连续的，只有这样，我们才能在O(1)时间内随即返回一个元素。


## 实现代码
```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
class ArrayHashMap:
    def __init__(self):
        self.map = dict()
        self.array = []

    # 查
    def get(self, key):
        if key not in self.map:
            return None
        index = self.map[key]
        node = self.array[index]
        return node.value

    # 增
    def put(self, key, value):
        if self.containsKey(key):
            index = self.map[key]
            self.array[index].value = value
            return
        node = self.Node(key, value)

        self.map[key] = len(self.array)
        self.array.append(node)

    # 删
    def remove(self, key):
        if key not in self.map:
            return
        index = self.map[key]
        node = self.array[index]
        # 交换删除
        # 交换删除的原理是，将数组的最后一个元素，移动到要删除的元素的位置上，然后删除数组的最后一个元素。
        # 这样做的好处是，我们可以在O(1)时间内删除一个元素，而不需要移动其他元素。

        e = self.array[-1]
        self.array[index] = e
        self.map[e.key] = index
        self.array[-1] = node
        self.array.pop()
        self.map.pop(key)

    def randomKey(self):
        if len(self.array) == 0:
            return None
        index = random.randint(0, len(self.array) - 1)
        return self.array[index].key

    def containsKey(self, key):
        return key in self.map

    def size(self):
        return len(self.array)

```