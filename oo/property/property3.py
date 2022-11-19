class Money():

    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("错误：不是整数类型！")

m = Money()
m.money = 100
print(m.money)