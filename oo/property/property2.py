class Foo():

    def __init__(self) -> None:
        self.value = "abc"

    def get_bar(self):
        return self.value

    def set_bar(self, value):
        self.value = value

    def del_bar(self):
        del self.value

    BAR = property(get_bar,set_bar,del_bar,"description...")

f = Foo()

print(Foo.BAR.__doc__)
# print(f.BAR.__doc__)
print(f.BAR)
f.BAR = "test"
print(f.BAR)
del f.BAR
# print(f.BAR)