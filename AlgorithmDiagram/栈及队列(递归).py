#  coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')      # python的str默认是ascii编码，和unicode编码冲突,需要加上这几句


# 二、栈：概念和实现

# 基于顺序表实现一个栈(表尾作为栈顶)

class StackUnderflow(ValueError): # 定义一个异常：栈下溢（空栈访问）
    pass

class SStack():
    def __init__(self): # 用list对象 _elems存储栈中元素
        self._elems = [] # 所有栈操作都映射到list操作（[]用于创建list）

    def is_empty(self):
        return self._elems == []

    def top(self): # 返回栈顶
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]

    def push(self,elem): # 入栈
        self._elems.append(elem)

    def pop(self): # 出栈
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()

st1 = SStack()
st1.push(3)
st1.push(5)
while not st1.is_empty():
    print (st1.pop())

# 栈的链接表实现（表头作为栈顶）
class LStack(): # 用LNode作为结点
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow("in LStack.top()")
        return self._top.elem

    def push(self,elem):
        self._top = LNode(elem,self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow("in LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem
# 这个类的使用方式与SStack完全一样，完全可以相互替代。这也是抽象数据类型的功劳。


# 三、栈的应用

# 栈可以用于颠倒一组元素的顺序,但是并不能得到原序列的任意排列
st1 = SStack()
for x in list1:
    st1.push(x)
list2 = []
while not st1.is_empty():
    list2.append(st1.pop())

# 括号匹配问题 P141
# 表达式的表示、计算和变换（前缀中缀后缀表达式）P143


# 三、求解背包问题的递归算法

# 先写出递归最终得到的几种情况

def knap_rec(weight,wlist,n): # 函数的三个参数分别是总重量weight，记录各物品重量的表wlist，物品数目n
    if weight == 0: # 终极状态
        return True
    if weight<0 or (weight > 0 and n < 1): # 重量大于0但已经没有物品可用
        return False
    if knap_rec(weight - wlist[n-1],wlist,n-1): # 减少了物品种类n，总的重量也减去此物品的重量
        # 那么这里减去的 wlist[n-1] 应该是谁呢？程序会按顺序判断，比如5不行之后，程序一层层返回栈，然后执行最后一个if语句
        # 刚好把第五个if语句执行了，把 5 从列表中删除
        print ("Item "+str(n)+":",wlist[n-1]) # 加上此物品，就刚好达到总重量
        return True
    if knap_rec(weight,wlist,n-1): # 能用n-1件物品达到总重量
        return True

weight = 10
wlist = [2,2,6,4,5]
knap_rec(weight,wlist,5)

# 四、队列

# 考虑定义一个可以自动扩充存储的队列类

class QueueUnderflow(ValueError): # 队列可能由于空而无法dequeue（出队）
    pass

class SQueue():
    def __init__(self,init_len = 8):
        self._len = init_len # 存储区长度
        self._elems = [0]*init_len # 元素存储
        self._head = 0 # 表头元素下标
        self._num = 0 # 元素个数

    def is_empty(self):
        return self.__num == 0

    def peek(self): # 查看队列里最早进入的元素
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]

    def dequeue(self): # 出队
        if self._num == 0:
            raise QueueUnderflow
        e = self._elems[self._head]
        self._head = (self._head+1) % self._len
        self._num -= 1
        return e

    def enqueue(self,e): # 元素e入队
        if self._num == self._len: # 若队列满，调用extend方法将存储区长度加倍，把原有元素搬迁到新表里
            self.__extend()
        self._elems[(self._head+self._num) % self._len] = e
        self._num += 1

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(old_len): # 将老的元素搬迁到新表中
            new_elems[i] = self._elems[(self._head+i)%old_len]
        self._elems,self._head = new_elems,0


# 五、迷宫求解和状态空间搜索

dirs = [(0,1),(1,0),(0,-1),(-1,0)] # 对于任何一个位置(i,j)，给它加上dirs[0]等就分别得到了该位置东南西北的四个相邻位置
                                   # pos[0]为i，pos[1]为j

def mark(maze,pos): # 给迷宫maze的位置pos标2表示 “到过了”
    maze[pos[0]][pos[1]] = 2
def passable(maze,pos): # 检查迷宫maze的位置pos是否可行
    return maze[pos[0]][pos[1]] == 0

# 递归实现的核心函数如下：
def find_path(maze,pos,end): # pos表示搜索的当前位置
    mark(maze,pos)
    if pos == end: # 已到达出口
        print (pos,end=" ") # 输出这个位置
        return True # 成功结束
    for i in range(4): # 否则按四个方向顺序探查
        nextp = pos[0]+dirs[i][0],pos[1]+dirs[i][1]
        if passable(maze,nextp):
            if find_path(maze,nextp,end): # 从nextp可达出口
                print (pos,end=" ") # 输出这个点
                return True # 成功结束
    return False

# 利用栈和回溯法解决迷宫问题 P165

# 基于队列的迷宫求解算法 P169






