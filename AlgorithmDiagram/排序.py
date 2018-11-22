
#  coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 接下来讨论排序算法时，使用的示例数据结构都是下面定义的record类的对象：

class record:
    def __init__(self,key,datum):
        self.key = key
        self.datum = datum

# 冒泡排序(均按照key的值从小到大排序)
def bubbleSort(lst):
    for i in range(len(lst)):
        found = False
        for j in range(1,len(lst)-i):
            if lst[j-1].key > lst[j].key:
                temp = lst[j]
                lst[j] = lst[j-1]
                lst[j-1] = temp
                # lst[j-1],lst[j] = lst[j],lst[j-1] # 直接调换位置
                found = True
        if not found: # found依然为false，说明一次逆序也没碰到，排序结束
            break


# 插入排序
def insert_sort(lst):
    for i in range(1,len(lst)): # 开始时片段[0:1]已排序
        x = lst[i]
        j = i
        while j > 0 and lst[j-1].key > x.key:
            lst[j] = lst[j-1] # 反序逐个后移元素，确定插入位置
            j -= 1  # 后一个位置向右移了一格，序列号向左移一格
        lst[j] = x # 将本次操作的元素插入j位置

# 选择排序
def select_sort(lst):
    for i in range(len(lst)-1):
        k = i # k是已知最小元素的位置
        for j in range(i,len(lst)):
            if lst[j].key < lst[k].key:
                k = j
        if i != k:
            lst[i],lst[k] = lst[k],lst[i] # 直接调换位置

# 快速排序
def quick_sort(lst):
    if len(lst) < 2: # 基线条件
        return lst
    else:              # 递归条件
        pivot = lst[0] # 作为基准（pivot）
        # print type(pivot),'1',type([pivot]),'2'  # 前为 int，后为 list
        # 分区（partition）操作
        less = [i for i in lst[1:] if i.key <= pivot.key] # 由所有小于基准值的元素组成的子数组
        greater = [i for i in lst[1:] if i.key > pivot.key]
        # 递归（recursive）排序
        return quicksort(less) + [pivot] + quicksort(greater) # 列表的排序

# 归并排序

# 合并两分段
def merge(lfrom,lto,low,mid,high):
    # 需要归并的两个有序分段分别是 lfrom[low:mid] 和 lfrom[mid:high]，归并结果应存入 lto[low:high]，区间左闭右开
    i,j,k = low,m,low
    while i < mid and j < high:  # 反复复制两分段首记录最小的
        if lfrom[i].key <= lfrom[j].key: # 第一段的首记录小于第二段的首记录，存入lto对应位置
            lto[k] = lfrom[i]
            i += 1 # 继续比较第一段的第二个与第二段的第一个大小
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    # 接下来将未比较的部分（有可能只剩一个）复制到lto中，这两个while循环只会执行其中一个
    while i < mid: # 复制第一段剩余记录
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:
        lto[k] = lfrom[j]
        j += 1
        k += 1
#
def merge_pass(lfrom,lto,llen,slen): # 表长度：llen ；分段长度：slen
    i = 0
    while i + 2*slen < llen:
        merge(lfrom,lto,i,i + slen,i + 2*slen)
        i += 2*slen # 处理接下来的两个分段
    if i + slen < llen: # 剩下两段，后段长度小于slen
        merge(lfrom,lto,i,i + slen,llen)
    else:               # 只剩下一段，复制到表lto
        for j in range(i,llen):
            lto[j] = lfrom[j]
# 主函数：先安排另一个同样长度的表，而后在两个表之间往复地做一遍遍归并，直至完成工作
def merge_sort(lst):
    slen,llen = 1,len(lst) # 先进行一对一归并，再做二对二归并...
    templst = [None]*llen # 安排另一个同样长度的表
    while slen < llen:
        merge_pass(lst,templst,llen,slen)
        slen *= 2
        merge_pass(templst,lst,llen,slen) # 结果存回原位
        # (一对一归并完成后，进行二对二归并，并放回lst中，可以把 templst和lst理解为各自的归并备用表）
        slen *= 2



