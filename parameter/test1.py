def print_test(title, msg="world"):
    print(title, msg)

print_test("hello") # hello world
print_test("hello", "demon") # hello demon
print_test("hello", msg="demon") # hello demon

# 错误调用示例
# print_test( msg="demon","hello") # 这样是不对的
# Positional argument cannot appear after keyword arguments

print("##################################################")

def print_numbers(*args):            
    print(type(args))  # tuple
    for n in args:
      print(type(n))   # int

print_numbers(1, 2, 3, 4)
print("#####")

l = [1, 2, 3, 4]
print_numbers(*l)  # *l，等价于 print_numbers(1, 2, 3, 4)
print("#####")
print_numbers(l)   # 将 l 作为一个整体传入，这样函数接受到的其实只有一个参数，且参数类型为 list

print("##################################################")

def register(name, email, **kwargs):
    print(f'name:{name}, age:{email}, others:{kwargs}')

register("demon", "1@1.com") 
register("demon", "1@1.com", addr="shanghai") 
register("demon", "1@1.com", addr="shanghai", test="test") 
print("#####")

d = {"addr":"shanghai","test":"test"}
register("demon", "1@1.com", **d)
print("#####")

d = {"name":"yrr", "email":"1@1.com", "addr":"shanghai"}
register(**d)
print("#####")

d = {"email":"yrr", "name":"1@1.com", "addr":"shanghai"}
register(**d)
print("#####")

d = {"addr":"shanghai", "email":"yrr", "name":"1@1.com"}
register(**d)

print("##################################################")

def test1(a, b, c=0, *args, **kwargs):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kwargs)

def test2(a, b, c=0, *args, d, **kwargs):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'args=', args, 'kw =', kwargs)

# 定义一个元组和字典用作参数传入
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}

test1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
test2(*args, **kw)
# a = 1 b = 2 c = 3 d = 99 args= (4,) kw = {'x': '#'}
print("#####")

args = (1, 2, 3, )
kw = {'d': 99, 'x': '#'}
test1(*args, **kw)
test2(*args, **kw)
print("#####")

args = (1, 2, )
kw = {'d': 99, 'x': '#'}
test1(*args, **kw)
test2(*args, **kw)
print("#####")

# args = (1, 2, )
# kw = {'e': 99, 'x': '#'}
# test1(*args, **kw)
# test2(*args, **kw)

