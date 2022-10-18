class Zuxian():
    pass

class Baba(Zuxian):
    pass

class Mama(Zuxian):
    pass

class Child(Baba,Mama):
    pass

print(Child.__mro__)

'''
(<class '__main__.Child'>, <class '__main__.Baba'>, <class '__main__.Mama'>, <class '__main__.Zuxian'>, <class 'object'>)
'''

class Zuxian():
    pass

class Mama(Zuxian):
    pass

class Baba(Zuxian):
    pass

class Child(Baba,Mama):
    pass

print(Child.__mro__)

'''
(<class '__main__.Child'>, <class '__main__.Baba'>, <class '__main__.Mama'>, <class '__main__.Zuxian'>, <class 'object'>)
'''

class Zuxian():
    pass

class Mama(Zuxian):
    pass

class Baba(Zuxian):
    pass

class Child(Mama,Baba):
    pass

print(Child.__mro__)

'''
(<class '__main__.Child'>, <class '__main__.Mama'>, <class '__main__.Baba'>, <class '__main__.Zuxian'>, <class 'object'>)
'''

