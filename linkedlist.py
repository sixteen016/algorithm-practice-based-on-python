'''
创建一个双链表类，实现基本的增删查改的操作
'''
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.pre = None

class MyLinkedlist:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0
    
    # 增
    def add_last(self,value):
        node = Node(value)
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node
        self.size += 1

    def add_first(self,value):
        node = Node(value)
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node
        self.size += 1

    def add(self,index,value):
        node = Node(value)
        
        # 检索索引越界
        self._check_position_index(index)

        cur = self.head
        for i in range(index):
            cur = cur.next
        
        node.next = cur.next
        node.pre = cur
        cur.next.pre = node
        cur.next = node
        self.size += 1

    # 删
    def remove_first(self):
        if self.size == 0:
            raise IndexError("No element to remove")
        
        deleted_value = self.head.next.value
        self.head.next = self.head.next.next
        self.head.next.pre = self.head
        self.size -= 1

        return deleted_value
    
    def remove_last(self):
        if self.size == 0:
            raise IndexError("No element to remove")
        
        deleted_value = self.tail.pre.value
        self.tail.pre = self.tail.pre.pre
        self.tail.pre.next = self.tail
        self.size -= 1

        return deleted_value
    
    def remove(self,index):
        # 检查索引越界
        self._check_element_index(index)

        cur = self.head
        for i in range(index):
            cur = cur.next
        
        deleted_value = cur.next.value
        cur.next = cur.next.next
        cur.next.pre = cur.pre
        self.size -= 1

        return deleted_value
    
    # 查
    def get(self,index):
        # 检查索引越界
        self._check_element_index(index)
        p = self.getNode(index)
        
        return p.value
    
    def get_last(self):
        if self.size < 1:
            raise IndexError("No element in the list")
        
        return self.tail.pre.value
    
    def get_first(self):
        if self.size < 1:
            raise IndexError("No element in the list")
        
        return self.head.next.value
    
    # 改
    def set(self,index,value):
        # 检查索引越界
        self._check_element_index(index)
        p = self.getNode(index)
        old_value = p.value
        p.value = value

        return old_value
    


    # 其他工具函数
    def size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def getNode(self,index):
        # 检查索引越界
        self._check_element_index(index)

        p = self.head.next
        for _ in range(index):
            p = p.next
        
        return p
    
    def is_element_index(self,index):
        return 0 <= index <self.size
    
    def is_position_index(self,index):
        return 0 <= index <= self.size
    
    def _check_element_index(self,index):
        if not self.is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")
        
    def _check_position_index(self,index):
        if not self.is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")
        
    
    def display(self):
        print(f"size = {self.size}")
        p = self.head.next
        while p != self.tail:
            print(f"{p.value} <-> ",end = " ")
            p = p.next
        print("null\n")

if __name__ == "__main__":
    list = MyLinkedlist()
    list.add_last(1)
    list.add_last(2)
    list.add_last(3)
    list.add_first(0)
    list.add(2, 100)

    list.display()
    # size = 5
    # 0 <-> 1 <-> 100 <-> 2 <-> 3 <-> null

    

