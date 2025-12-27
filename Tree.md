# Tree——树
树是一种本身非常简单的数据结构，我们概括地讲，树是由n个节点组成的集合。
最上层的节点称为根节点，最底层的节点称为叶子节点。
每个节点的上一层节点称为父节点，下一层节点称为子节点。而根节点是没有父节点的，叶子节点则没有子节点。
树的一个重要特性是：每个节点只能有一个父节点，但可以有多个子节点。
以子节点为根节点的树称为子树。


树中，每个节点的子节点数量不超过2个，我们将这样的树称为二叉树。
二叉树是应用最多的树形结构。
而二叉树中又有很多不同的类型，包括：满二叉树、完全二叉树、平衡二叉树等。
满二叉树即每一层的节点数量都达到了最大值，即2^h-1个节点，其中h为树的高度。

完全二叉树是指除了最后一层外，其他层的节点数量都达到了最大值，且最后一层的节点都靠左对齐。
完全二叉树的两个子树，一个是满二叉树，一个是完全二叉树。

平衡二叉树是指任意节点的左右子树高度差不超过1的二叉树。 

二叉搜索树是指任意节点的左子树中的所有节点的值都小于该节点的值，右子树中的所有节点的值都大于该节点的值。


## 二叉树的实现

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
上述代码是二叉树的简单实现，实际应用中，我们可能没有必要为了实现二叉树的结构单独设置一个TreeNode类，使用数组或者列表来表示二叉树也是一种常见的实现方式。

## 树形结构的最常用的应用是节点的查找与遍历。
二叉树的遍历方法有两种：递归遍历和层序遍历。
递归遍历可以延伸出DFS算法、回溯算法；层序遍历则可以延伸出BFS算法。

### 递归遍历（DFS）
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def traverse(root:TreeNode):
        if root.val is None:
            return
        traverse(root.left)
        traverse(root.right)
```
可见上述的traverse函数非常的短小精悍，但是确实实现了对二叉树的遍历。
为什么这段代码可以遍历二叉树呢？
因为递归遍历的基本思想是：先遍历左子树，再遍历右子树。
而二叉树的左子树和右子树本身也是二叉树，所以可以递归地遍历它们。

那么，接下来我们就能很好的理解什么是前序遍历、中序遍历、后序遍历。

前序遍历：先遍历根节点，再遍历左子树，最后遍历右子树。
中序遍历：先遍历左子树，再遍历根节点，最后遍历右子树。
后序遍历：先遍历左子树，再遍历右子树，最后遍历根节点。

也就是说，我们只要在上述的traverse函数的不同位置插入新的代码，即可实现前序遍历、中序遍历、后序遍历。
```python 
def traverse(root: TreeNode):
    if root.val is None:
        return 
    # 前序遍历
    traverse(root.left)
    # 中序遍历
    traverse(root.right)
    # 后序遍历
```

### 层序遍历（BFS）
层序遍历是指按照树的层次从上到下、从左到右依次遍历树中的节点。

```python 
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def traverse(root: TreeNode):
        if root.val is None:
            return
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            # 访问当前节点
            print(cur.val)
            # 访问当前节点的左子树
            if cur.left:
                q.append(cur.left)
            # 访问当前节点的右子树
            if cur.right:
                q.append(cur.right)

```
上述写法的优点在于，写法简单。但是缺点也很明显，在应用场景中，我们经常需要知道，当前节点的层数，而该写法并不能直接给出当前节点的层数。

```python 
from collections import deque

def traverse(root: TreeNode):
    if root.val is None:
        return
    q = deque()
    depth = 0
    q.append(root)
    depth += 1
    while q:
        sz = len(q)
        for _ in range(sz):
            cur = q.popleft()
            # 访问当前节点
            print(cur.val)
            # 访问当前节点的左子树
            if cur.left:
                q.append(cur.left)
            # 访问当前节点的右子树
            if cur.right:
                q.append(cur.right)
        # 遍历完当前层的所有节点后，深度加1
        depth += 1
```
上述代码中，我们使用了一个变量depth来记录当前节点的层数。
在每次遍历完当前层的所有节点后，深度加1，即可得到当前节点的层数。
最精妙的地方在于，这个for循环。
for循环的作用是遍历当前层的所有节点。
在每次遍历完当前层的所有节点后，深度加1，即可得到下一层的所有节点。

当然，上述的写法也可以进行延伸，比如，我们在学习最短路径问题的时候，不仅节点存在值，边也存在权重。
而上述写法，可以认为每条边的权重都是1。
而如果每条边的权重都不同，就需要下面的写法。

```python 
from collections import deque

class State；
    def __init__(self, node: TreeNode, depth: int):
        self.node = node
        self.depth = depth


def traverse(root: TreeNode):
    if root.val is None:
        return 
    q = deque()
    q.append(State(root, 1))
    while q:
        cur = q.popleft()
        # 访问当前节点
        print(cur.node.val, cur.depth)
        # 访问当前节点的左子树
        if cur.node.left:
            q.append(State(cur.node.left, cur.depth + 1))
        # 访问当前节点的右子树
        if cur.node.right:
            q.append(State(cur.node.right, cur.depth + 1))
    
```
### DFS和BFS算法
DFS和BFS算法都是非常重要的算法。它们常用于最短路径问题和穷举所有路径的问题。
其中，DFS算法常用于穷举所有路径的问题，而BFS算法常用于最短路径问题。
下面解释为什么。
首先，我们要明白这两种算法都是能够解决这两种问题的，只是解决的时间和方式不同。
我们先来探讨一下最短路径问题：
```python
class Solution:
    def __init__(self):
        # 记录最短路径
        self.min_depth = float('inf')
        # 记录当前节点的深度
        self.depth = 0
    def minDepth(self, root: TreeNode) -> int:
        if root.val is None:
            return 0
        self.dfs(root)
        return self.min_depth

    def dfs(self, root: TreeNode):
        if root.val is None:
            return 

        depth += 1
        # 到达叶子节点，更新最短路径
        if root.left is None and root.right is None:
            self.min_depth = min(self.min_depth, self.depth)
        self.dfs(root.left)
        self.dfs(root.right)
        depth -= 1
```
```python
class Solution:
    def BFS(self, root: TreeNode) -> int:
        if root.val is None:
            return 0

        q = deque()
        q.append(root)
        depth = 1
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if cur.left is None and cur.right is None:
                    return depth
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            depth += 1
        return depth
```

在上述代码中，我们分别使用DFS和BFS算法来解决最短路径问题。
二者的区别在于，DFS算法必须遍历完所有路径才能得出最短路径，而BFS算法可以在遍历到第一个叶子节点时，直接返回最短路径。

下面，我们讨论穷举所有路径的问题
为什么DFS算法用的多，因为写起来比较简单，DFS算法本身就是一条路径，一条路径遍历的算法。

## 多叉树和森林
多叉树是二叉树的延申，二叉树是特殊的多叉树
```python
# 二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 多叉树
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.children = []

```

森林就是多叉树的集合
即: vector<TreeNode> forest

多叉树和森林的DFS和BFS算法

```python
# 二叉树的DFS算法
def traverse(root: TreeNode):
    if root is None:
        return
    # 前序遍历
    traverse(root.left)
    # 中序遍历
    traverse(root.right)
    # 后序遍历
# 多叉树的DFS算法
def traverse(root: TreeNode):
    if root is None:
        return
    # 前序遍历
    for child in root.children:
        traverse(child)
    # 后序遍历
# 多叉树的DFS算法没有中序遍历，毕竟多叉树的每个节点有多个子节点，中序遍历没有什么意义


# 多叉树的BFS算法
# 写法一
def traverse(root: TreeNode):
    if root is None:
        return
    q = deque()
    q.append(root)
    while q:
        cur = q.popleft()
        # 访问当前节点
        print(cur.val)
        for child in cur.children:
            q.append(child)

# 写法二
def traverse(root: TreeNode):
    if root is None:
        return
    q = deque()
    q.append(root)
    depth = 1
    while q:
        sz = len(q)
        for _ in range(sz):
            cur = q.popleft()
            # 访问当前节点
            print(cur.val, depth)
            for child in cur.children:
                q.append(child)
        depth += 1  

# 写法三
class State:
    def __init__(self, node: TreeNode, depth: int):
        self.node = node
        self.depth = depth

def traverse(root: TreeNode):
    if root is None:
        return
    q = deque()
    q.append(State(root,1))
    while q:
        cur = q.popleft()
        # 访问当前节点
        print(cur.node.val, cur.depth)
        for child in cur.node.children:
            q.append(State(child, cur.depth + 1))
```

## 二叉搜索树

