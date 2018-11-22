
#  coding: utf-8
from __future__ import division  # // 表示整数除法，返回不大于结果的一个最大的整数
import sys
reload(sys)
sys.setdefaultencoding('utf8')      # python的str默认是ascii编码，和unicode编码冲突,需要加上这几句


a=5.0
b=3.0
c=a//b
print c