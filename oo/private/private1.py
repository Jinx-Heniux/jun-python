class Momen():

    def __init__(self,name):
        self.name = name
        self.__age = 18

    def __secret1(self):
        return self.__age

    def secret2(self):
        return self.__age

m1 = Momen("小芳")

# print(f"名字：{m1.name} | 年龄：{m1.__age}")
# 伪私有属性
print(f"名字：{m1.name} | 年龄：{m1._Momen__age}")

# print(f"名字：{m1.name} | 年龄：{m1.__secret1()}")
# 伪私有方法
print(f"名字：{m1.name} | 年龄：{m1._Momen__secret1()}")

print(f"名字：{m1.name} | 年龄：{m1.secret2()}")