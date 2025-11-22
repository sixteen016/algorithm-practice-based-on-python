# Bit Map——位图
## 原理
Bit Map是一种非常节省空间的数据结构，它用一个比特位来标记某个元素是否存在
实际应用中，除非要处理的数据量非常大，否则不建议为了节省空间使用Bit Map

Bit Map的原理是将一个元素映射到一个比特位上，例如将元素i映射到第i个比特位上
那么，这就需要在元素和比特位之间建立一个映射关系
这个映射关系的建立可以有多种方式，例如：
1. 直接映射
   例如将元素i映射到第i个比特位上，那么就可以直接使用i作为比特位的索引
2. 哈希映射
   例如将元素i映射到第hash(i)个比特位上，那么就需要使用一个哈希函数来计算元素i对应的比特位索引

一般来说，直接映射就足以使用了。
例如：
以long[]作为Bit Map，每个long类型有64个比特位，那么就可以将64个元素映射到64个比特位上
假如，我们想访问第135个比特位，那么就需要访问第**135//64=2** 个long类型的元素，第**135%64=31**个比特位

## 代码实现
```python
class BitMap:
    def __init__(self, size):
        self.size = size
        self.words = [0] * (size // 64 + 1)
    
    # 判断指定比特位是否为1
    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError(f"bitIndex must be between 0 and {self.size - 1}")
        
        wordIndex = i // 64
        bit_offset = i % 64
        return (self.words[wordIndex] & (1 << bit_offset)) != 0
    # 将指定比特位设置位1
    def set(self, i):
        if i < 0 or i >= self.size:
            raise IndexError(f"bitIndex must be between 0 and {self.size - 1}")
        wordIndex = i // 64
        bit_offset = i % 64
        self.words[wordIndex] |= (1 << bit_offset)

    # 将指定比特位设置位0
    def clear(self, i):
        if i < 0 or i >= self.size:
            raise IndexError(f"bitIndex must be between 0 and {self.size - 1}")
        wordIndex = i // 64
        bit_offset = i % 64
        self.words[wordIndex] &= ~(1 << bit_offset)
```