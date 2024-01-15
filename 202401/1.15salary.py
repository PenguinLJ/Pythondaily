"""
假设有个公司有三类员工，分别是产品经理、程序员以及测试工程师。
三类员工的薪资计算方法如下。
>产品经理：按照固定工资分配。

程序员：有基础工资，加班有加班费，当加班时长不超过20小时，加班费为100元/小时；
当加班时长超过20小时，就按20小时加班计算，超出部分不计入薪资。

测试工程师：有基础工资，存在绩效薪资，每发现一个错误(Bug）即可以获得5元绩效薪资。
"""


class Employee:  # 员工类，作为父类
    def __init__(self, name):
        self.name = name  # 定义属性name

    def get_salary(self):  # 定义获取薪资的方法
        pass


class Manager(Employee):  # 定义产品经理类继承Employee类，

    def __int__(self, name, salary=15000):
        super().__init__(name)  # 继承父类属性
        self.salary = salary  # 定义薪资salary

    def get_salary(self):  # 重写父类方法
        return self.salary

    def __str__(self):
        return f"{self.name}的薪资是{self.get_salary()}"


class Programmer(Employee):

    def __init__(self, name, base_salary=12000, over_time=0):
        super().__init__(name)
        self.base_salary = base_salary
        self.over_time = over_time

    def get_salary(self):
        if self.over_time < 0:
            raise ValueError("工作时长有误")
        elif self.over_time > 20:
            self.over_time = 20
        return self.base_salary + 100 * self.over_time

    def __str__(self):
        return f"{self.name}的薪资是{self.get_salary()}"


class SoftTest(Employee):

    def __init__(self, name, base_salary=8000, bug_num=0):
        super().__init__(name)
        self.base_salary = base_salary
        self.bug_num = bug_num

    def get_salary(self):
        return self.base_salary + 5 * self.bug_num

    def __str__(self):
        return f"{self.name}的薪资是{self.get_salary()}"


