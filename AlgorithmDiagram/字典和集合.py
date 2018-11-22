#  coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')      # python的str默认是ascii编码，和unicode编码冲突,需要加上这几句

# 二、字典线性表实现(采用链接表实现字典总有操作是O(n)操作，没有任何明显的优势)

# 有序线性表和二分法检索

def bisearch(lst,key):
    low,high = 0,len(lst)-1
    while low <= high:
        mid = low + (high-low)//2
        if key == lst[mid].key:
            return lst[mid].value
        if key < lst[mid].key:
            high = mid -1
        else:
            low = mid + 1



# 六、 二叉排序树（又名 二叉搜索树、二叉查找树）与字典

# 任何用于实现二叉树的技术都能用于实现二叉排序树，为了支持树结构的动态变化，建议采用链接结构，可以基于前面定义的BinTNode类实现

# 二叉排序树的检索

def bt_search(btree,key):
    bt = btree
    while bt is not None:
        entry = bt.data
        if key < entry.key:
            bt = bt.left
        elif key > entry.key:
            bt = bt.right
        else:
            return entry.value
    return None
# 检索过程很清晰，就是根据被检索关键码与当前结点关键码的比较情况，决定是向左走还是向右走，最终返回对应key的value

# 二叉排序树（字典）类
# 现在考虑基于二叉排序树的思想定义一个字典类，并分析和实现类中的各主要算法

class DictBinTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self,key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
            bt = bt.right
        else:
            return entry.value
    return None

# 字典项的插入

    def insert(self,key,value):
        bt = self._root
        if bt is None: # 如果二叉树空，就直接建立一个包括新关键码和关联值得树根结点
            self._root = BinTNode(Assoc(key,value))
            return
        while True:
            entry = bt.data
            if key < entry.key:
                if bt.left is None:
                    bt.left = BinTNode(Assoc(key,value))
                    return
                bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinTNode(Assoc(key, value))
                    return
                bt = bt.right
            else: # 遇到结点里的关键码等于被检索关键码，直接替换关联值并结束
                bt.data.value = value
                return
# 给字典定义一个迭代器方法，生成其中所有值的序列，以便字典的使用者通过for循环或其他方式使用字典里的数据
# 下面实现的是 中序遍历 ，对字典而言，按其他遍历序的价值不大
    def values(self):
        t,s = self._root,SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            t = s.pop
            yield t.data.value  # 备注：yield t.data.key,t.data.value
            t = t.right

# t.data是一个Assoc类对象，不能返回此关联对象，万一无意修改，可能会破坏整个字典，不再是一个二叉排序树了。
# 备注中采取另一种方法：在找到所需的关联后，取出其中的关键码和值，重新做成一个序对返回。
# 这样，只要关键码本身不是可变对象，用户就不能破坏字典的完整性

# 删除具有给定关键码的元素

    def delete(self,key):
        p,q = None,self._root
        while q is not None and q.data.key != key: # 先寻找key对应的结点位置，并维持p为q的父结点
            p = q
            if key < q.data.key:
                q = q.left
            else:
                q = q.right
            if q is None:
                return # 树中没有关键码key

            # 到这里q引用要删除结点，p是其父节点或None（p为None,说明这时q是根结点（这样就没有进入上一个循环））
            if q.left is None: # 如果q没有左子结点
                if p is None:  # 说明q是根结点，则应该修改 _root
                    self._root = q.right
                elif q is p.left: # 根据q和p的关系修改p的子树引用
                    p.left = q.right
                else:
                    p.right = q.right
                return

            # 考虑q有左子结点的情况
            r = q.left # 找q左子树的最右结点
            while r.right is not None:
                r = r.right
            r.right = q.right # 将q的右子树作为r的右子树
            # 接下来，用q的左子树结点代替q原先的位置
            if p is None: # q是根结点，修改 _root
                self._root = q.left
            elif p.left is q:
                p.left = q.left
            else:
                p.right = q.left

# 为了检查二叉树的情况，定义一个输出树中信息的方法
    def print(self):
        for k,v in self.entries():
            print (k,v)
# END class

# 最后定义一个函数，基于一系列数据项（关键码和值得二元组）建立起一组二叉排序树：
def build_dictBinTree(entries):
    dic = DictBinTree()
    for k,v in entries:
        dic.insert(k,v)
    return dic

# 最佳二叉排序树

# 简单情况：检索概率相同
class DictOptBinTree(DictBinTree): # 从DictBinTree中继承
    def __init__(self,seq):
        DictBinTree.__init__(self)
        data = sorted(seq)
        self._root = DictOptBinTree.buildOBT(data,0,len(data)-1)

    # 在这个类里定义了一个静态方法
    @staticmethod
    def buildOBT(data,start,end):
        if start > end:
            return None
        mid = (end+start)//2
        left = DictOptBinTree.buildOBT(data,start,mid-1)
        right = DictOptBinTree.buildOBT(data, mid+1, end)
        return BinTNode(Assoc(*data[mid]),left,right) # 存入此时中间值，并在每一次递归返回时都存入相应的值

# 一般情况下的最佳二叉排序树
# 最佳二叉排序树的重要性质：它的任何子树也是最佳的二叉排序树
# 利用动态规划算法，从最小的最佳二叉树做起，逐步做出所需的最佳二叉树
# 其时间复杂度为 O(n^3),空间复杂度为 O(n^2)


# 平衡二叉树（AVL树） P302
# 插入操作与删除操作算法的时间复杂度都是 O(log n)

# 动态多分支排序树 P311
# 多分支排序树、B树、B+树


