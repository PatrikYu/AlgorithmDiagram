#  coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')      # python的str默认是ascii编码，和unicode编码冲突,需要加上这几句

# 三、 字符串匹配（子串查找）

# 朴素的串匹配算法

def naive_matching(t,p):
    m,n = len(p),len(t) # p是模式串，t是目标串
    i,j = 0,0
    while i < m and j < n:
        if p[i] == t[j]: # 字符相同，考虑下一对字符
            i,j = i+1,j+1
        else:
            i,j = 0,j-i+1 # 字符不同，考虑t中下一位置（将模式串右移一位，相当于从目标串的j-i+1处重新开始对比）
    if i == m: # 找到匹配，返回其下标
        return j-i # 举个例子一看就知道了
    return -1
# 最坏情况下的时间复杂度为 O(m*n)

# 无回溯串匹配算法（KMP算法）

# 假设已经根据模式串做出了pnext表，考虑KMP算法的实现
def matching_KMP(t,p,pnext):
    "KMP串匹配，主函数"
    m, n = len(p), len(t)  # p是模式串，t是目标串
    i, j = 0, 0
    while i < m and j < n:
        if i == -1 or t[j] == p[i]: # 遇到-1(当Pi匹配之前做过的比较没有利用价值)，比较下一对字符串
                                    # 字符相等，比较下一对字符串： 大家都往后移一位
            j,i = j+1,i+1
        else: # 字符不相等
            i = pnext[i] # 从pnext取得p的下一字符位置。pnext表的构造见 P117
    if i == m: # 找到匹配，返回其下标
        return j-i
    return -1
# 主函数复杂度为O(n),注：分支的复杂度是取大值
# 一次KMP算法的完整执行包括构造pnext表和实际匹配，总时间复杂性为O(m+n)，由于m<<n，可认为其复杂度为O(n)