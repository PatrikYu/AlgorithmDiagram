#  coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')      # python的str默认是ascii编码，和unicode编码冲突,需要加上这几句

import datetime # 需要处理一些与时间相关的数据，引入datetime标准库包

# 公共人员类的实现
class Person:
    _num = 0 # 用于记录类对象的数目

    #  __init__方法的主要工作是检查参数合法性，设置对象的数据属性。
    def __init__(self,name,sex,birthday,ident):
        if not (isinstance(name,str) and sex in ("女","男")):
            raise PersonValueError(name,sex) # 若输入不符合标准就报错
        try:
            birth = datetime.date(*birthday) # 生成一个日期对象
            # 上面的函数定义利用了date类，其构造函数要求三个参数（分别代表年月日），如果实参不是合法日期值就会引发异常。
        except: # 若上面句子出错就执行以下语句
            raise PersonValueError("Wrong date:",birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1

    def id(self): return self._id
    def name(self): return self._name
    def sex(self): return self._sex
    def birthday(self): return self._birthday
    def age(self): return (datetime.date.today().year - self._birthday.year)

    def set_name(self,name): # 修改名字
        if not isinstance(name,str):
            raise PersonValueError("set_name",name)
        self._name = name

    def __lt__(self,another): # 实现小于运算
        if not isinstance(another,Person):
            raise PersonTypeError(another)
        return self._id < another._id
    # 实现小于运算的方法要求另一个参数也是Person，然后根据两个人员记录的_id域的大小确定记录的大小关系
    # 后面表的sort方法会用到

    # 在这个类里还需要定义一个类方法，以便取得类中的人员计数值。另外还定义了两个与输出有关的方法
    @classmethod
    def num(cls): return Person._num
    # 这里的第一个参数是cls，表示调用当前的类名
    # 调用方法：r = Person.num()
    # 前面用了@classmethod装饰。 它的作用就是有点像静态类，比静态类不一样的就是它可以传进来一个当前类作为第一个参数。

    def __str__(self):
        return " ".join((self._id,self._name,self._sex,str(self._birthday))) # 以" "连接

    def details(self):
        return ", ".join(("编号：" + self._id,"姓名：" + self._name,"性别：" + self._sex,"出生日期："+ str(self._birthday)))
    # 以", "连接

    # 让__str__提供对象的基本信息，details方法提供完整细节。
    # 注意：字符串的join方法要求参数是可迭代对象。所以这里将元素组成一个元祖 （）

# 至此Person类的基本定义就完成了。下面是使用这个类的几个语句：
p1 = Person("徐文婷","女",(1996, 6, 30),"1201510111")
p2 = Person("晏晓利", "女", (1997, 7, 15), "1201510132")
p3 = Person("陈班班", "男", (1998, 8, 23), "1201510104")
p4 = Person("徐浩", "男", (1999, 9, 8), "1201510128")

plist2 = [p1,p2,p3,p4]
for p in plist2:
    print p
print ("\nAfter sorting")
plist2.sort() # 用到了Person类里面的__lt__()方法，按照id进行排序
for p in plist2:
    print (p.details())

print "\n",("People created:" ,Person.num())

# 学生类的实现

# 1.Student对象也是Person对象，应调用Person类的初始化函数
# 2.要用Student类实现一种学号生成方式，为保证学号唯一性，用一个计数变量，每次生成学号时将其加一
#    这个变量应该是Student类内部的数据，但又不属于任何Student实例对象，因此应用类的数据属性表示
# 3.学号生成函数只在Student类的内部使用，但并不依赖Student的具体实例。且此函数依赖于Studennt类中的数据属性，应定义为类方法

class Student(Person): # 继承Person
    _id_num = 0

    @classmethod # 定义为类方法
    def _id_gen(cls): # 用类的数据属性表示，实现学号生成规则
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year,cls._id_num)
    # 使用str的format方法构造学号：规定学号的首位为1，把入学年份以4位十进制的形式编码到学号中，最后是五位的序号

    def __init__(self,name,sex,birthday,department):
        Person.__init__(self,name,sex,birthday,Student._id_gen())
        self._department = department
        self._enroll_date = datetime.date.today()
        self._course = {}
        # 分别记录学生的院系，入学报到日期，课程学习成绩，初始时设为空字典

    def set_course(self,course_name):
        self._courses[course_name] = None

    def set_score(self,course_name,score):
        if course_name not in self._courses:
            raise PersonValueError("No this course selected:",course_name)
        self._courses[course_name] = score
    # 假定了必须先选课，最后才能设定课程成绩

    def scores(self): return [(cname,self._courses[cname]) for cname in self._courses]
    # 给出所有成绩的列表

    # 虽然Person类的details方法依然可用，但Student对象包含的信息更多
    # 需要定义一个同名的新方法，覆盖基类中已有定义的details方法，可以在首先在新方法里调用基类的同名方法
    def details(self):
        return ", ".join((Person.details(self),"入学日期: " + str(self._enroll_date),\
                          "院系： " + self._department,"课程记录： " + str(self.scores())))
    # 并不是每个派生类的覆盖方法都需要重复基类方法的工作，若需要，必须通过基类名或super函数去调用
    # 若从self出发调用details，实际调用的将是本类的details

# 教职工类的实现

class Staff(Person):
    _id_num = 0

    @classmethod  # 定义为类方法
    def _id_gen(cls,birthday):  # 用类的数据属性表示
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return "0{:04}{:05}".format(birth_year,cls._id_num) # 教职工编号首位为0

    def __init__(self,name,sex,birthday,entry_date=None):
        super().__init__(name,sex,birthday,Staff._id_gen(birthday))
     #  Person.__init__(self,name,sex,birthday,Student._id_gen())
     #  使用super()函数时不需要提供self参数，是更好的调用方法

        self._enroll_date = datetime.date.today() # 简单写写
        self._position = "未定"
        self._department = "未定"
        self._salary = 8000

        # 这三个有其默认值（可修改），不需要传入进行初始化

    def set_salary(self,amount): self._salary = amount
    # 同理定义部门和职位

    def details(self):
        return ", ".join((super().details(),"入职日期：" + str(self._entry_date),"工资：" + str(self._salary)))









