#  coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')      # python的str默认是ascii编码，和unicode编码冲突,需要加上这几句

from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)    # 设置作图中显示中文字体

from numpy import *      # 导入科学计算包
import operator          # 导入numpy中的运算符模块

print "一段中文哟"
# 一、算法简介


# 1.二分查找 p7

# 仅当列表是有序的时候，二分查找才管用

def binary_search(list,item):
    low = 0
    high = len(list)-1 # low,high用于确定查找范围

    while low<=high: # 确认存在查找的空间
        mid = (low+high)/2 # 如果（low+high）不是偶数，python将自动将mid向下取整
        guess = list[mid] # 猜中间的值是我们所寻找的item
        if guess == item:
            return mid # 返回位置
        if guess>item:
            high = mid-1
        else:
            low = mid+1
    print "Not Found"
    return None

# 对于包含n个元素的列表，用二分查找最多需要log2(n)步，而简单查找最多需要n步。log2(128)=7,最多需要7次

# 二、选择排序

# 对喜欢的乐队进行排序

# 先编写一个用于找出数组中最小元素的函数

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# 排序

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index))
        # 注意 pop()后接的是索引，不是具体元素值
        # arr.pop(smallest)就是此时arr中最小值
        # 将arr中最小值添加到newArr中，并且将arr中此元素删除
    return newArr

# print selectionSort([5,3,6,2,10])


# 四、快速排序

# p47 练习

# 4.1 请编写前述sum函数的代码

def sum(arr):
    if len(arr)<2:
        return arr[0] # 之前提示错误：int不能直接与list相加，因此return为arr[0]，而不是arr；arr.pop(0)是int
    else:             # 由于这里要实现相加，故不能写成[arr.pop(0)]。列表的相加不是对应数值的相加
        return arr.pop(0) + sum(arr)
# print sum([4,5,8,6,3])

# 4.2 编写一个递归函数来计算列表包含的元素数

def calc_num(arr):
    if len(arr)<2:
        return 1
    else:
        arr.pop(0)
        return 1+calc_num(arr)
# print calc_num([4,5,8,6,3])

# 4.3 递归找出列表中最大的数字

# 思路：求n个数的最大值，我们可以先求n-1个数的最大值，然后再与第n个数作比较，返回最大值
# 但是递归要设置终止条件，终止条件即为当n等于1时，我们就不需要再去求n-1个数的最大值和它比较了，直接返回这个数即可

def find_max(arr): # 最终返回n个数的最大值
    if len(arr)<2:
        return arr[0]
    else:
        a = arr.pop(0)
        b = find_max(arr) # 将b记作后n-1个数的最大值
        # 接下来比较 a 与 b 的大小
        if a > b:
            return a
        else:
            return b
# print find_max([4,5,8,6,3])

# 快速排序

def quicksort(array):
    if len(array) < 2: # 基线条件
        return array
    else:              # 递归条件
        pivot = array[0]
        # print type(pivot),'1',type([pivot]),'2'  # 前为 int，后为 list
        less = [i for i in array[1:] if i<= pivot]
        greater = [i for i in array[1:] if i>pivot]
        return quicksort(less) + [pivot] + quicksort(greater) # 列表的排序
# print quicksort([4,5,8,6,3])


# 六、广度优先搜索(breadth-first search,BFS)

# 创建一个图(用字典来存储这个图),从中心出发，按顺时针顺序，依次写出一度关系，二度关系的图（条理清晰，添加的顺序并无影响）

graph={}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["thom"]=[]
graph["jonny"]=[]
graph["peggy"]=[]

# 首先，创建一个队列。在python中，可使用函数deque来创建一个双端队列

from collections import deque
# search_queue = deque() # 创建一个队列
# search_queue += graph("you") # 将你的邻居都加入到这个搜索队列中，注意graph("you")是一个数组

# 编写函数 person_is_seller，判断一个人是不是芒果商

def person_is_seller(name):
    return name[-1] == 'm' # 返回值为True或False
# 这里仅仅是举个例子，检查人的姓名是否以m结尾，如果是，他就是芒果经销商

# peggy即是alice的朋友又是bob的朋友，因此她将被加入队列两次，但你只需检查peggy一次，否则就做了无用功
# 因此，检查完一个人后，应将其标记为已检查，且不再检查他，否则可能会导致死循环，例如你和另一个节点构成了邻居关系
# 循环将不断在你们之间进行，所谓无限循环。因此，可以使用一个列表来记录检查过的人

# 主程序

def search(name):
    search_queue = deque()  # 创建一个队列
    search_queue += graph[name]  # 将你的邻居都加入到这个搜索队列中，注意graph("you")是一个数组
    searched = [] # 这个数组用于记录检查过的人
    while search_queue:  # 只要队列不为空
        person = search_queue.popleft() # 就取出其中的第一个人
        if person not in searched: # 仅当这个人没检查过时才检查
            if person_is_seller(person):  # 检查这个人是否是芒果销售商
                print person + " is a mango seller!"
                return True
            else:
                search_queue += graph[person]  # 不是芒果销售商，将这个人的朋友都加入搜索队列
                searched.append(person) # 将此人标记为检查过
    return False

# search("you")


# 七、迪克斯特拉算法


# 先实现权重图,同时存储邻居和前往邻居的开销

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
# print graph["start"].keys(),"获取起点的所有邻居" # 注意是keys()
# print graph["start"]["a"],"获得从起点到A的边的权重"
# 添加其他节点集邻居
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {} # 终点没有任何邻居

# 接下来，需要用一个散列表来存储每个节点的开销，节点的开销指的是从起点出发前往该节点需要多长时间
# 对于未知的开销，将其设置为无穷大

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 还需要一个存储父节点的散列表

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 最后，你需要一个数组，用于记录处理过的节点，因为对于同一个节点，你不用处理多次
processed = []

# 具体算法如下

# 函数 find_lowest_cost_node 找出开销最低的节点，注意：被调用的函数要放在主函数前面，否则会报错

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # 遍历所有的节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # 确保已在列表中1
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# 主程序

node = find_lowest_cost_node(costs) # 在未处理的节点中找出开销最小的节点
while node is not None: # 当前节点是否为空，这个while循环在所有节点都被处理过后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # 如果经当前节点前往该邻居更近，就更新该邻居的开销
            costs[n] = new_cost
            parents[n] = node # 同时将该邻居的父节点设置为当前节点
    processed.append(node) # 将当前节点标记为处理过
    node = find_lowest_cost_node(costs)
# print costs,"开销"
# print parents,"对应的父节点"


# 八、贪婪算法


# 首先，创建一个列表，其中包含要覆盖的州
states_needed = set(["mt","wa","or","id","nv","ut","ca","az"]) # 集合不能包含重复的元素
# 可供选择的广播台清单
stations = {}
stations["kone"] = set(["id","nv","ut"])
stations["ktwo"] = set(["wa","id","mt"])
stations["kthree"] = set(["or","nv","ca"])
stations["kfour"] = set(["nv","ut"])
stations["kfive"] = set(["ca","az"])
# 最后，需要使用一个集合来存储最终选择的广播台
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station,states in stations.items(): # station为kone,ktwo等等；states为取到的station所包含的车站set
        covered = states_needed & states # 目前选中的station与需要覆盖的州的重合的州
        if len(covered) > len(states_covered): # 选出此时覆盖州最多的广播台
            best_station = station
            states_covered = covered
    states_needed -= states_covered # 将已覆盖的州从需要的州列表中删除
    final_stations.add(best_station) # 将此时最优的广播台添加到final_stations中

# print final_stations


# 九、动态规划
















