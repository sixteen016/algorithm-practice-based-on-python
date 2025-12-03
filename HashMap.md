# HashMap——哈希表
## 原理
哈希表可以看作是一种强化的数组。普通的数组可以在O(1)时间内访问任意元素，索引是一个非负整数。
哈希表是类似的，可以通过key，计算得出一个索引，然后访问对应的value。
key的类型是多样的，比如整数、字符串、对象等。

## 代码实现
```python
class HashMap:
    def __init__(self):
        self.table = [None] * 1000
    
    # 增
    def put(self, key, value):
        index = self.hash(key)
        self.table[index] = value

    # 删
    def remove(self, key):
        index = self.hash(key)
        deleted_value = self.table[index]
        self.table[index] = None
        return deleted_value

    # 查
    def get(self, key):
        index = self.hash(key)
        return self.table[index]

    # 哈希函数
    # 将key转换为哈希值，必须时间复杂度是O(1)，才能保证以上所有操作的时间复杂度都是O(1)
    def hash(self, key):
        pass
```

## 关键的概念
1. key 是唯一的，每个key都对应一个value;value 可以重复。
2. 哈希函数
    1. 哈希函数的作用是将key转换为哈希值，必须时间复杂度是O(1)，才能保证以上所有操作的时间复杂度都是O(1)。
    2. 哈希函数的设计要考虑到哈希值的均匀分布，避免哈希冲突。
3. 哈希冲突
    1. 哈希冲突是指不同的key，通过哈希函数计算出了相同的哈希值。
    2. 哈希冲突的解决办法有很多种，比如链地址法、开放地址法、再哈希法等。
    3. 链地址法
        1. 链地址法的原理是将哈希表的每个槽位都指向一个链表，当发生哈希冲突时，将新元素插入到链表的末尾。
        2. 链地址法的时间复杂度是O(1)，但是空间复杂度是O(n)，n是哈希表中元素的数量。
    4. 开放地址法
        1. 开放地址法的原理是当发生哈希冲突时，通过探测序列，找到一个空槽位插入新元素。
        2. 开放地址法的时间复杂度是O(1)，但是空间复杂度是O(n)，n是哈希表中元素的数量。
4. 扩容与负载因子
    1. 负载因子是哈希表中元素的数量与哈希表槽位数量的比值。
    2. 负载因子的作用是衡量哈希表的填充程度，当负载因子超过一个阈值时，需要对哈希表进行扩容。
    3. 负载因子的计算公式是：负载因子 = 元素数量 / 槽位数量
    4. 负载因子的阈值一般取0.75，当负载因子超过0.75时，需要对哈希表进行扩容。

### 拉链法实现哈希表
```python
class KVNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class ExampleChainingHashMap:
    def __init__(self, init_capacity=4):
        self.size = 0
        self.capacity = max(init_capacity, 1)
        self.table = [[] for _ in range(self.capacity)]
    

    # 增/改
    def put(self, key, value):
        if key is None:
            raise ValueError("key is null")


        index = self.hash(key)
        bucket = self.table[index]

        # 链表不为空，遍历链表，检查是否存在相同key
        for node in bucket:
            if node.key == key:
                # 存在相同key，更新value
                node.value = value
                return 

        # 不存在相同key，插入到链表尾部
        bucket.append(KVNode(key, value))
        self.size += 1
        # 如果元素数量超过了负载因子，扩容
        if self.size > self.capacity * 0.75:
            self._resize(self.capacity * 2)
    
    # 删
    def remove(self, key):
        if key is None:
            raise ValueError("key is null")
        index = self.hash(key)
        bucket = self.table[index]
        # 链表不为空，遍历链表，检查是否存在相同key
        for node in bucket:
            if node.key == key:
                # 存在相同key，删除该节点
                bucket.remove(node)
                self.size -= 1
                # 如果元素数量低于了负载因子的一半，缩容
                if self.size < self.capacity * 0.125:
                    self._resize(self.capacity // 4,1)
                return 
    
    # 查
    def get(self, key):
        if key is None:
            raise ValueError("key is null")
        index = self.hash(key)
        bucket = self.table[index]
        
        # 链表不为空，遍历链表，检查是否存在相同key
        for node in bucket:
            if node.key == key:
                # 存在相同key，返回value
                return node.value
        # 不存在相同key，返回None
        return None
    
    '''
          # 链表不为空，遍历链表，检查是否存在相同key
        for node in self.table[index]:
            if node.key == key:
                # 存在相同key，返回value
                return node.value
        # 不存在相同key，返回None
        return None

        ----->

        self.table[index][:] = [node for node in self.table[index] if node.key != key]
    '''

    # 返回所有key
    def keys(self):
        keys = []
        for bucket in self.table:
            for node in bucket:
                keys.append(node.key)
        return keys 
    
    # 其他工具函数
    def size(self):
        return self.size

    # 哈希函数
    def hash(self, key):
        return key % len(self.table)

    def _resize(self, new_capacity):
        # 构造一个新的哈希表
        new_table =  ExampleChainingHashMap(new_capacity)
        # 遍历旧哈希表，将元素迁移到新哈希表
        for bucket in self.table:
            for node in bucket:
                new_table.put(node.key, node.value)
        # 更新哈希表引用
        self.table = new_table.table
        self.capacity = new_table.capacity
``` 

### 线性探查法相比较拉链法来说，具有两个难点：
1. 插入的时候需要运用到环形数组的概念，当数组的位置被占用时，需要从当前位置往后找，直到找到空槽位，如果直到结尾仍然没有，则需要从开头继续寻找，直到找到空槽位为止。
2. 删除的时候需要注意，删除一个元素后，就会出现先一个空槽位，这影响到数组的连续性。
   1. 解决方法一：从删除的位置向后遍历，将处于同一个索引的元素向前迁移，直到元素连续位置；
   2. 解决方法二：将删除位置标记为删除状态，当遇到删除状态的元素，跳过该位置，继续遍历。

### 线性探查法（开放寻址法）实现哈希表
```python
# rehash
class KVNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class ExampleLinearProbingHashMap:
    INIT_CAP = 4
    def __init__(self, capacity=INIT_CAP):
        self.size = 0
        self.table = [None] * self.capacity

    # 增/改
    def put(self, key, value):
        if key is None:
            raise ValueError("key is null")

        # 将负载因子默认为0.75，当元素数量超过负载因子，扩容
        if self.size >= len(self.table) * 0.75:
            self._resize(self.capacity * 2)

        index = self.get_key_index(key)
        # 如果key已经存在，更新value
        if self.table[index] is not None:
            self.table[index].value = value
            return 
        
        # 如果key不存在，插入到空槽位
        self.table[index] = KVNode(key, value)
        self.size += 1

    # 删
    def remove(self, key):
        if key is None:
            raise ValueError("key is null")
        
        # 缩容，当元素数量低于负载因子的0.125，缩容至当前容量的1/4
        if self.size < len(self.table) * 0.125:
            self._resize(self.capacity // 4)

        index = self.get_key_index(key)
        # 如果key不存在，直接返回
        if self.table[index] is None:
            return

        # 如果key存在，删除该节点
        self.table[index] = None
        self.size -= 1
        # 保持数组连续性，从删除位置开始，往后遍历，将处于同一个索引的元素向前迁移
        index = (index + 1) % len(self.table)
        while self.table[index] is not None:
            entry = self.table[index]
            self.table[index] = None
            # 迁移元素到新位置
            self.size -= 1
            self.put(entry.key, entry.value)
            index = (index + 1) % len(self.table)

    # 查
    def get(self, key):
        if key is None:
            raise ValueError("key is null")

        index = self.get_key_index(key)
        # 如果key不存在，直接返回
        if self.table[index] is None:
            return None
        # 如果key存在，返回value
        return self.table[index].value

    # 返回所有key
    def keys(self):
        return [entry.key for entry in self.table if entry is not None]

    # 其他工具函数
    def size(self):
        return self.size

    # 哈希函数
    def hash(self, key):
        return (hash(key) & 0x7fffffff) % len(self.table)

    # 对key进行线性探查
    def get_key_index(self, key):
        index = self.hash(key)
        # 从当前位置开始，往后遍历，直到找到空槽位或者key相等的位置
        while self.table[index] is not None:
            # 如果key相等，返回索引
            if self.table[index].key == key:
                return index
            index = (index + 1) % len(self.table)
        return index

    def _resize(self, new_capacity):
        new_map = ExampleLinearProbingHashMap(new_capacity)
        # 遍历旧哈希表，将元素迁移到新哈希表
        for entry in self.table:
            if entry is not None:
                new_map.put(entry.key, entry.value)
        self.table = new_map.table
```