# 循环数组

## 1、原理
数组需要的空间是一块线性连续的，也就是说是不可能存在环的概念的。
但是，我们可以通过取模的方式，在逻辑上实现环的效果。

比如 **i** 是数组的最后一个元素，那么 **i+1** 和 **arr.length** 取模的结果就是0，那么就又回到了数组的第一个元素，实现了环的效果。

## 2、实现
环形数组的代码实现主要是依靠于start和end两个指针，start指向数组的第一个有效的元素，end则指向数组中的最后一个有效元素的下一个位置。
这样，实际上就实现了一个左闭右开的区间，即[start, end)，其中start指向的元素是有效的，而end指向的元素是无效的。

下面，是环形数组的代码实现：
```python
class CircularArray:
    def __init__(self, size=1):
        self.size = size
        self.array = [None] * size
        self.start = 0
        self.end = 0
        self.count = 0
    
    # 自动扩容
    def resize(self, newSize:int):
        # 1、创建一个新的数组
        newArray = [None] * newSize

        # 2、将旧数组的元素复制到新数组中
        for i in range(self.count):
            newArray[i] = self.array[(self.start + i) % self.size]
        self.array = newArray

        # 3、更新
        self.size = newSize
        self.start = 0
        self.end = self.count

    # 增加第一位元素
    def add_first(self, value):
        # 当数组满的时候，扩容至两倍
        if self.isfull():
            self.resize(self.size * 2)
        
        # 1、将start指针向左移动一位
        self.start = (self.start - 1) % self.size
        # 2、将新元素插入到start指针的位置
        self.array[self.start] = value
        # 3、更新元素数量
        self.count += 1
    
    # 删除第一位元素
    def remove_first(self):
        # 1、判断数组是否为空
        if self.isempty():
            raise Exception("数组为空")
        
        # 2、将数组的首位置为None
        self.array[self.start] = None
        # 3、将数组的start指针向右移动一位
        self.start = (self.start + 1) % self.size
        # 4、更新元素数量
        self.count -= 1

        # 缩容
        if self.count > 0 and self.count == self.size // 4:
            self.resize(self.size //2)

    # 增加最后一位元素
    def add_last(self, value):
        # 当数组满的时候，扩容至两倍
        if self.isfull():
            self.resize(self.size * 2)
        
    #   1、将新元素插入到end的位置
        self.array[self.end] = value
        # 2、将end指针向右移动1位
        self.end = (self.end + 1) % self.size
        # 3、更新元素数量
        self.count += 1

    # 删除最后以为元素
    def remove_last(self):
        # 1、判断数组是否为空
        if self.isempty():
            raise Exception("数组为空")
        # 2、将数组的end指针向左移动1位
        self.end = (self.end - 1) % self.size
        # 3、将数组的end位置置为None
        self.array[self.end] = None
        # 4、更新元素数量
        self.count -= 1

        # 缩容
        if self.count > 0 and self.count == self.size // 4: 
            self.resize(self.size //2)

    # 获取数组的头部元素
    def get_first(self):
        # 1、判断数组是否为空
        if self.isempty():
            raise Exception("数组为空")
        # 2、返回数组strat位置的元素
        return self.array[self.start]

    # 获取数组的尾部元素
    def get_last(self):
        # 1、判断数组是否为空
        if self.isempty():
            raise Exception("数组为空")
        # 2、返回数组的end位的前一个元素
        return self.array[(self.end - 1) % self.size]

    # 其他工具函数

    def isempty(self):
        return self.count == 0

    def isfull(self):
        return self.count == self.size

    def get_count(self):
        return self.count
    
```