#  coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')      # python的str默认是ascii编码，和unicode编码冲突,需要加上这几句


一.顺序表：包括list和tuple


二.链接表


2.单链表


class LNode:
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = next_
# 这个类里只有一个初始化方法，它给对象的两个域赋值，第二个参数用next_是为了避免与标准函数next重名
# 若要变为私有：_next,_head

# 表首端插入元素
q = LNode(13) #创建一个新结点并存入数据13
q.next = head.next #把原链表首节点的链接head.next存入新结点的链接域，将原表的一串结点链接到刚创建的新结点之后
head = q #修改表头变量head，使之指向新结点q。使得q成为了表的首结点
# 一般情况的元素插入，设变量pre已指向要插入元素的前一结点
q = LNode(13)
q.next = pre.next # pre后面的结点跟在q后面
pre.next = q # q跟在pre后面

# 删除表首元素
head = head.next #修改表头指针，使之指向表中的第二个结点，第一个结点被丢弃回收
# 一般情况下的元素删除，设pre为被删结点的前一结点
pre.next = pre.next.next # 将pre.next.next向前提一位

# 链表的扫描
# p = head
# while p is not None and 还需继续的其他条件:
#     对p所指结点里的数据做所需操作
#     p = p.next
# 按下标定位（确定第i个元素所在结点的操作称为按下标定位）
p = head
while p is not None and i > 0:
    i -= 1
    p = p.next
    # 举例：如果现在需要删除第k个结点，可以先将i设置为k-1，循环后检查i是0（此时p向后移动了k-1次，指向第k个结点）且p.next不是0就可以删
# 按元素定位：假设需要在链表里找到满足谓词pred(符合pred条件)的元素
p = head
while p is not None and not pred(p.elem):
    p = p.next
# 完整的扫描称为遍历
p = head
while p is not None:
    print (p.elem) # 这个循环依次输出表中各元素
    p = p.next

# 求链表的长度
def length(head):
    p,n = head,0
    while p is not None:
        n += 1
        p = p.next
    return n
# 很明显，这种求表长度的方法，时间复杂度为O(n)


3.单链表类的实现


llist1 = LNode(1)
p = llist1 # p是扫描指针，这里将其指向第一个结点(值为1)
for i in range(2,11): # 取i为2-10 ，把一个个新结点链接到已有的表结点链的最后
    p.next = LNode(i)
    p = p.next

p = llist1
while p is not None:
    print (p.elem)
    p = p.next

# LList类的定义，初始化函数和简单操作
# 现在基于结点类LNode定义一个单链表对象的类，在这种表对象里只有一个引用链接结点的_head域
# 这里将头指针定义为私有变量，不希望外部使用 _head
class LList:
    def __init__(self):
        self._head = None # 建立一个空表

    def is_empty(self):
        return self._head is None # 判断表空的操作检查_head

    def prepend(self,elem):
        self._head = LNode(elem,self._head) # 在表头插入数据，它把包含新元素的结点链接在最前面，结合LNode的定义来看
    # class LNode:
    #     def __init__(self, elem, next_=None):
    #         self.elem = elem
    #         self.next = next_

    def pop(self):
        if self._head is None: # 无结点，引发异常
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

# 后端操作
# 1.在链表的最后插入元素
def append(self,elem):
    if self._head is None: # 若这是个空链表，那么直接放到第一个结点位置就好，也是最后一个
        self._head = LNode(elem)
        return
    p = self._head
    while p.next is not None: # 一直重复直到取到最后一个元素
        p = p.next
    p.next = LNode(elem) # 在链表的最后插入元素
# 2.删除表中最后元素（即最后的结点）
def pop_last(self):
    if self._head is None: #空表
        raise LinkedListUnderflow("in pop_last")
    p = self._head
    if p.next is None: # 表中只有一个元素
        e = p.elem
        self._head = None
        return e
    while p.next.next is not None: # 直到p.next是最后结点
        p = p.next
    e = p.next.elem
    p.next = None # 删除最后一个结点
    return e

# 其他操作
# 1.找到满足给定条件的表元素（该方法返回第一个满足谓词的表元素）
def find(self,pred):
    p = self._head
    while p is not None:
        if pred(p.elem): # 满足某pred条件
            return p.elem
        p = p.next
# 2.看看被操作的表的当时情况
def printall(self):
    p = self._head
    while p is not None:
        print (p.elem,end='')
        if p.next is not None:
            print (',',end='')
        p = p.next
    print ('')
#看一个例子
mlist1 = LList()
for i in range(10):
    mlist1.prepend(i) # 通过循环在表首端加入9个整数
for i in range(11,20):
    mlist1.append(i) # 通过循环在表尾端加入9个元素
mlist1.printall() # 最后顺序输出表里的所有元素

# 表的遍历
def for_each(self,proc): # 自己写的foreach函数，java里面好像自带此类函数
    p = self._head
    while p is not None:
        proc(p.elem) # proc的实参应该是可以作用于表元素的操作函数，它将被作用于每个表元素
        p = p.next
# 假如list1是以字符串为元素的表，下面语句将一行一个地输出这些字符串.
list1.for_each(print) # 当然，for_each这个函数是写在class里面的，这儿用.来调用
# python为内部汇集类型提供的遍历机制是迭代器，标准使用方式是放在for语句头部，在循环体中逐个处理汇集对象的元素
# 在python中，要想定义迭代器，最简单的方式是定义生成器函数，在类里也能定义具有这种性质的方法
def elements(self):
    p = self._head
    while p is not None:
        yield p.elem
        p = p.next
# 在python中，这种一边循环一边计算的机制，称为生成器 generator,能够节省大量空间
for x in list1.elements():
    print(x)
# generator 保存的是算法，用 print(x) 循环输出

# 筛选生成器filter,表示要基于给定的谓词筛选出表中满足pred的元素
def filter(self,pred):
    p = self._head
    while p is not None:
        if pred(p.elem):
            yield p.elem # 这也是一个生成器方法，使用方式与前面的elements类似，这是需要多提供一个谓词参数。
        p = p.next


4.链表的变形和操作


# 通过继承和扩充定义新链表类
def __init__(self):
    LList.__init__(self) # 对父类LList初始化
    self._rear = None # 初始化尾结点引用域，定义为私有变量_

def prepend(self,elem):
    if self._head is None: # 由于从LList继承的判断表空操作只检查_head,同一个类里的其他操作应该与它一致
        self._head = LNode(elem, self._head)
        self._rear = self._head  # 若是空表，新加入的第一个结点也是最后一个结点
    else:
        self._head = LNode(elem, self._head)

def append(self,elem):
    if self._head is None:
        self._head = LNode(elem, self._head)
        self._rear = self._head
    else:
        self._rear.next = LNode(elem)
        self._rear = self._rear.next

def pop_last(self):
    if self._head is None: #空表
        raise LinkedListUnderflow("in pop_last")
    p = self._head
    if p.next is None: # 表中只有一个元素
        e = p.elem
        self._head = None
        return e
    while p.next.next is not None: # 直到p.next是最后结点
        p = p.next
    e = p.next.elem
    p.next = None # 删除最后一个结点

    self._rear = p # 只加了这么一条，在删除尾结点之后更新_rear

    return e

# 下面是一段使用这个类的代码
mlist1 = LList1()
mlist1.prepend(99)
for i in range(11,20):
    mlist1.append(randint(1,20))

for x in mlist1.filter(lambda y:y%2==0):
    print (x)


# 循环单链表类:只需要一个数据域_rear，它在逻辑上始终引用着表的尾结点

class LCList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self,elem): # 前端加入结点，就是在尾结点和首结点之间加入新的首结点
        p = LNode(elem)
        if self._rear is None:
            p.next = p # 建立一个结点的环
            self._rear = p
        else:
            p.next = self._rear.next # 将尾结点的下一结点作为p的下一结点
            self._rear.next = p # 这样就在尾结点和首结点之间加入新的结点p

    def append(self,elem): # 尾端插入
        self.prepend(elem)
        self._rear = self._rear.next # 尾端向下一个结点移了一位就变成尾端插入了

    def pop(self): # 前端弹出
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p = self._rear.next # p取得此时的首端
        if self._rear is p: # 就一个结点
            self._rear = None
        else:
            self._rear.next = p.next # 第二个结点作为尾结点的下一个，即作为新的首结点

    def printall(self): # 输出表元素
        if self.is_empty():
            return
        p = self._rear.next # 取得首结点
        while True:
            print (p.elem)
            if p is self._rear:
                break
            p = p.next


# 链表反转


def rev(self):
    p = None
    while self._head is not None:
        q = self._head # q取得表头指针所指向的第一个结点！！！！！！！！而self._head依旧是表头指针
        self._head = q.next # 摘下原来的首结点
        q._next = p # 第一次循环时，p为空；第二次循环时，将首结点放到第二个结点的后面
        p = q       # p取得这一次摘下来的结点，第一次循环时即为首结点
    self._head = p  # 反转后的结点序列已经做好，重置表头链接

# 链表排序

# 顺序表(list)排序函数（插入排序）
def list_sort(lst):
    for i in range(1,len(lst)): # 开始时片段[0:1]已排序
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x: # 这里是从小到大排序，要 从大到小 改为 lst[j-1] < x
            lst[j] = lst[j-1] # 反序逐个后移元素至确定插入位置
            j -= 1
        lst[j] = x # 当位置j之前元素不大于x时，将x放入空位

# 单链表的排序算法
# 首先考虑基于移动元素的单链表排序算法
def sort1(self):
    if self._head is None:
        return
    crt = self._head.next # 从第二个结点开始处理
    while crt is not None:
        x = crt.elem
        p = self._head # 取得首结点
        while p is not crt and p.elem <= x: # 跳过小元素（我们要做的是从小到大的排序，要挑出左边元素比较大的做排序）
            p = p.next
        while p is not crt: # 倒换大元素，完成元素插入的工作。p不断向后移，取得的值为y，若y大于x，将p与crt位置对应的值交换
            y = p.elem
            p.elem = x
            x = y
            p = p.next
        crt.elem = x # 回填最后一个元素（实际上在最后一次 x = y ,相当于把手头数据填入）
        crt = crt.next

# 现在考虑通过调整链接的方式实现插入排序。  ？？？没看懂这个算法
# 就是一个个取下链表结点，将其插入一段元素递增的结点链中的正确位置
def sort(self):
    p = self._head
    if p is None or p.next is None: # 空或单个链表就没有必要排序了
        return

    rem = p.next # 用rem记录除第一个元素之外的结点段，然后通过循环把这些结点逐一插入_head关联的排序段
    p.next = None
    while rem is not None:
        p = self._head # 取下首结点
        q = None

        # 此内层循环在排序段查找rem结点的插入位置，用了两个扫描指针p和q，q在前，p在后
        while p is not None and p.elem <= rem.elem: # p,q不断向后推进，直到p为None或出现了比rem结点值大的
            q = p
            p = p.next
        if q is None:  # 实现表头插入
            self._head = rem
        else: # 一般情况插入
            q.next = rem

        # 连接好排序段
        q = rem
        rem = rem.next
        q.next = p


5.表的应用

# josephus问题
# 基于“数组”概念的解法
def josephus_A(n,k,m): # 一共有n个人，从第k个人开始数，报到第m个数的人退出
    people = list(range(1,n+1)) # 建立一个包含n个人的表
    i = k-1 # 用i表示数组下标，其初值取k-1：从第k个人那开始数
    for num in range(n): # 大循环一次迭代出列一人，共计执行n次迭代
        count = 0
        while count < m:
            if people[i] > 0: # 仅统计未出局的人
                count += 1
            if count == m:
                print (people[i],end="")
                people[i] = 0 # 出局者标记为0
            i = (i+1) % n # 无论有没有报到m，都是下一个人开始报，这里%n代表遇到表的末端就转回下一轮开始报
        if num < n-1:
            print (", ",end="")
        else:
            print ("")
    return

# 基于顺序表的解
def josephus_L(n,k,m):
    people = list(range(1,n+1))

    num,i = n,k-1
    for num in range(n,0,-1): # n--1
        i = (i+m-1) % num # 核心代码：直接往后数m个就是要删去的
        print (people.pop(i),end=(", "if num > 1 else "\n")) # 这个条件表达式的格式注意一下
    return

# 基于循环单链表的解
class Josephus(LCList):
    def turn(self,m): # 将循环表对象的rear指针沿next方向移m步（相当于结点环旋转）
        for i in range(m):
            self_rear = self._rear.next

    def __init__(self,n,k,m):
        LCList.__init__(self) # 首先调用基类的初始化函数建立一个空表
        for i in range(n): # 通过一个循环建立包含n个结点和相应数据的初始循环表
            self.append(i+1)
        self.turn(k-1) # 从第k个人那儿开始数
        while not self.is_empty():
            self.turn(m-1) # 找到并逐个弹出结点
            print (self.pop(),end=("\n" if self.is_empty() else ", "))










