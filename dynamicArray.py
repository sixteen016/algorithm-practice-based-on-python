'''
创建一个动态数组类，支持增删查改的基本功能
'''
class DynamicArray:
    # 默认初始容量
    INIT_CAP = 1

    def __init__(self,init_capacity=None):
        self.data = [None] * (init_capacity if init_capacity is not None else self.INIT_CAP)
        self.size = 0
    
    #增
    def add_last(self,value):
        cap = len(self.data)
        # 看看数组的容量是否足够
        if self.size == cap:
            self._resize(2 * cap)
        # 在数组尾部插入元素
        self.data[self.size] = value
        self.size += 1
    
    def add(self,index,value):
        # 检查索引是否合法
        self._check_position_index(index)
        cap = len(self.data)
        # 看看数组的容量是否足够
        if self.size == cap:
            self._resize(2 * cap)
        # 数据迁移
        for i in range(self.size - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]
        
        # 插入要添加的元素
        self.data[index] = value
        self.size += 1

    def add_first(self,value):
        self.add(0,value)

    # 删
    def remove_last(self):
        if self.size == 0:
            raise IndexError("NoSuchElement")
        cap = len(self.data)
        # 缩容
        if self.size == cap // 4:
            self._resize(cap // 2)
        
        deleted_value = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return deleted_value
    
    def remove(self,index):
        # 检查索引越界
        self._check_element_index(index)
        cap = len(self.data)
        # 缩容
        if self.size == cap // 4:
            self._resize(cap // 2)
        
        deleted_value = self.data[index]
        # 数据迁移
        for i in range(index + 1, self.size):
            self.data[i - 1] = self.data[i]
        self.data[self.size - 1] = None
        self.size -= 1

        return deleted_value
    
    def remove_first(self):
        return self.remove(0)
    
    # 查
    def get(self,index):
        # 检查索引越界
        self._check_element_index(index)
        return self.data[index]
    
    # 改
    def set(self,index,value):
        # 检查索引越界
        self._check_element_index(index)
        old_value = self.data[index]
        self.data[index] = value

        return old_value
    
    # 工具方法
    def  get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    # 讲data的容量更改为new_capacity
    def _resize(self,new_capacity):
        temp = [None] * new_capacity
        for i in range(self.size):
            temp[i] = self.data[i]
        self.data = temp

    def is_element_index(self,index):
        return 0 <= index < self.size
    
    def is_position_index(self,index):
        return 0 <= index <= self.size
    
    def _check_element_index(self,index):
        if not self.is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")
        
    def _check_position_index(self,index):
        if not self.is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")
        
    def display(self):
        print(f"DynamicArray: size = {self.size}, capacity = {len(self.data)}")
        print(self.data)

if __name__ == "__main__":
    arr = DynamicArray(init_capacity=3) 


    # 添加 5 个元素
    for i in range(1, 6):
        arr.add_last(i)

    arr.remove(3)
    arr.add(1, 9)
    arr.add_first(100)
    val = arr.remove_last()

    # 100 1 9 2 3
    for i in range(arr.get_size()):
        print(arr.get(i))

        


        
