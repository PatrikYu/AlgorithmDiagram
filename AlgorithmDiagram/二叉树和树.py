#  coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')      # python的str默认是ascii编码，和unicode编码冲突,需要加上这几句

# 三、优先队列

# 基于list实现优先队列(假设值较小的元素优先级更高)
# 且最优先的项应该出现在表的尾端（为保证访问和弹出最优先数据项的操作能在O(1)时间内完成）
# 应在表首端加入元素

class PrioQueueError(ValueError):
    pass
# 将优先队列定义为一个类
class PrioQue:
    def __init__(self,elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True) # 对elems做从大到小的排序

# 插入元素
def enqueue(self,e):
    i = len(self._elems) - 1
    while i >= 0:
        if self._elems[i] <= e: # e的优先级低于序列为i的值，应排在i前面
            i -= 1
        else: # 否则将e排到i+1的位置上
            break
    self._elems.insert(i+1,e)

def is_empty(self):
    return not self._elems

def peek(self): # 输出最优先项
    if self.is_empty():
        raise PrioQueueError("in top")
    return self._elems[-1]

def dequeue(self): # 弹出首项（删除它）
    if self.is_empty():
        raise PrioQueueError("in pop")
    return self._elems.pop()

# 复杂度分析： 插入元素是O(n)操作，其他都是O(1)操作

# 基于堆的优先队列类 P193
# 应在表尾端加入元素，以首端作为栈顶（最优先的项出现在首端），与前面用排序表实现的情况相反？？？
# 总结： 基于堆的概念实现优先队列，创建操作的时间复杂度是O(n)，这件事只需做一次
#        插入和弹出操作的复杂度是0(log n),效率比较高


# 堆的应用：堆排序

# 初始建堆
# from __future__ import division  # // 表示整数除法，返回不大于结果的一个最大的整数 不加这句也ok，若要加得放在最前面
def buildheap(self):
    end = len(self._elems)
    for i in range(end//2,-1,-1): # 把初始表看作一棵完全二叉树，从下标 end//2 开始
        self.siftdown(self._elems[i],i,end)
# 排序 P196


# 四、离散事件模拟 P196

# 实现一个通用模拟器类
from random import randint
from prioqueue import PrioQueue # 自己写的包里面导入PrioQueue这个模块(.py文件)，这是基于堆的优先队列类
from queue_list import SQueue

# 海关检查站模拟系统 P198


# 五、二叉树的类实现

# 现在先定义一个表示二叉树结点的类。空二叉树直接用None表示
class BinTNode:
    def __init__(self,dat,left = None,right = None): # 接收三个参数：结点数据，左右子结点
        self.data = dat
        self.left = left
        self.right = right
    # 统计树中结点个数：
    def count_BinTNodes(t):
        if t is None:
            return 0
        else:
            return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)
    # 假设结点中保存数值，求这种二叉树里的所有数值和：
    def sum_BinTNodes(t):
        if t is None:
            return 0
        else:
            return t.dat + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)

    # 按先根序遍历二叉树的递归函数：
    def preorder(t,proc): # proc是具体的结点数据操作函数
        if t is None:
            return
        proc(t.data)
        preorder(t.left)
        preorder(t.right)
        # 按中根序和后根序遍历二叉树的函数与此类似，只是其中几个操作的排列顺序不同

    # 为能看到具体二叉树情况，定义一个以易读形式输出二叉树的函数，这里采用带括号的前缀形式输出
    def print_BinTNodes(t):
        if t is None:
            print ("^",end="") # 空树输出^
            return
        print ("(" + str(t.data),end="")
        print_BinTNodes(t.left)
        print_BinTNodes(t.right)
        print (")",end="")

# 下面语句构造了一棵包含4个结点的二叉树，变量t引着树根结点：
t = BinTNode(1,BinTNode(2,BinTNode(5)),BinTNode(3))
print_BinTNodes(t)
# 如果不在遇到空树输出一个记号，只有一棵子树时就无法区分左右了


# 宽度优先遍历
# 要实现采用宽度优先方式的二叉树遍历函数，同样需要用一个队列。下面定义使用了前面定义的SQueue类
from SQueue import *

def levelorder(t,proc):
    qu = SQueue() # qu取得这个类
    qu.enqueue(t) # t入队
    while not qu.is_empty():
        n = qu.dequeue()
        if t is None: # 弹出的树为空则直接跳过
            continue
        qu.enqueue(t.left)
        qu.enqueue(t.right)
        proc(t.data)
    # 在处理一个结点时，函数先将其左右子结点顺序加入队列。这样实现的就是对每层结点从左到右的遍历。

# 非递归的先根序遍历函数

def preorder_nonrec(t,proc):
    s = SStack() # 之前定义的 栈 类
    while t is not None or not s.is_empty(): # 在当前树非空（这棵树需要遍历）或者栈不空（还存在未遍历的部分），就继续循环
        while t is not None: # 沿左分支下行
            proc(t.data) # 先根序，先处理根数据
            s.push(t.right) # 右分支入栈
            t = t.left
        t = s.pop # 遇到空树，回溯

# 假设变量tree的值是一棵二叉树，其结点中保存的是可打印数据，下面语句将逐项输出该树中的数据内容,用空格分隔
preorder_nonrec(tree,lambda x:print(x,end=" "))
# 时间复杂度：上面函数在整个执行中将访问每个结点一次，所有右子树被压入和弹出栈各一次（栈操作是O(1)时间），整个遍历花费O(n)时间
# 空间复杂度：栈的最大深度由二叉树的高度决定，平均为 O(log n)


# 通过生成器函数遍历
# 简单修改前面的非递归先根序遍历函数，就能得到一个二叉树迭代器
def preorder_elements(t):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()
# 所有非递归定义的遍历算法都能修改为迭代器。但递归算法不行！！！？？？

# 非递归的后根序遍历算法
def postorder_nonrec(t,proc):
    s = SStack()
    while t is not None or not s.is_empty(): # 在当前树非空（这棵树需要遍历）或者栈不空（还存在未遍历的部分），就继续循环
        while t is not None: # 下行循环，直到栈顶的两子树空
            s.push(t) # 当前树入栈
            t = t.left if t.left is not None else t.right
            # 能左就左，否则向右一步
            ## 此内层循环找当前子树的最下最左结点，将其入栈后终止。
            ## 存储的是：左边完整二叉树 + 左边二级完整二叉树 + ... + 最下最左结点

        t = s.pop() # 栈顶是应访问结点（第一次循环时就弹出最下最左结点）
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right # 栈不空且当前结点是栈顶的左子结点
        else:
            t = None # 没有右子树或右子树遍历完毕，强迫退栈


# 六、哈父曼树

# 用一个优先队列存放这组二叉树，按二叉树根结点的权值排列优先顺序，从小到大
# 这里基于已有的构造二叉树的类派生出两个类
class HTNode(BinTNode):
    def __lt__(self, othernode): # 增加了一个“小于”比较操作
        return self.data < othernode.data

# 定义了一个专门为构造哈夫曼算法服务的优先队列类，其中增加了一个检查队列中元素个数的方法
class HuffmanPrioQ(PrioQueue): # PrioQueue是 基于堆的优先队列类
    def number(self): # 检查队列中元素个数
        return len(self._elems)

# 实现哈夫曼树
def HuffmanTree(weights): # 任何可迭代对象都能作为这个函数的参数weights
    trees = HuffmanPrioQ()
    for w in weights: # 第一个循环获取可迭代对象的一个个值，并将其加入优先队列
        trees.enqueue(HTNode(w)) # 入队
    while trees.number() > 1:
        t1 = trees.dequeue() # 出队
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x,t1,t2)) # 将新构造的二叉树压入优先队列（优先队列内部会自动排好序）
    return trees.dequeue{}
# 哈夫曼树 ： 时间复杂度：O(m log m) ; 空间复杂度：O(m)


# 七、树和树林

# 树的Python的list实现
class SubtreeIndexError(ValueError):
    pass

def Tree(data,*subtrees):
    return [data].extend(subtrees) # 这里的subtrees是一个序列参数

def is_empty_Tree(tree):
    return tree is None

def root(tree): # 取得树根结点
    return tree[0]

def subtree(tree,i):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    return tree[i+1]

def set_root(tree,data): # 设置根结点
    tree[0] = data

def set_subtree(tree,i,subtree):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    tree[i+1] = subtree

# 定义树类

class TreeNode:
    def __init__(self,data,subs=[]):
        self.__data = data # 结点数据
        self._subtrees = list(subs) # 一组子树

    def __str__(self): # 将自动被str(...)标准函数调用，用于显示和输出
        return "[TreeNode {0} {1}]".format(self._data,self.subtrees)

>>> "名字 {1} {0} {1}".format("hello", "world")  # 设置指定位置
'名字 world hello world'