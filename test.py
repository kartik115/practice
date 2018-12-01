def func_overload(a, b):
    return a+b


def func_overload(a,b):
    return "{0}{1}".format(a, b)


print(func_overload(2, 3))
print(func_overload("2", "3"))


class Demo:
    def ___new___(self):
        self.__init__(self)
        print("new demo")

    def __init__(self):
        print("init demo")


class DemoDerive(Demo):
    def ___new___(self):
        print("new derived demo")

    def __init__(self):
        print("init demo")


obj1 = DemoDerive()
obj2 = Demo()

s = "string"
s.replace("t", "p").upper()
print(s)


def split_string(input, delimeter):
    length = len(input)
    s = ''
    output = list()
    for x in range(length):
        if input[x] == delimeter:
            output.append(s)
            s = ''
        else:
            s += input[x]
    output.append(s)
    print(output)


split_string("Big boss show is baised", " ")


class Test:
    pass


class DerivedTest(Test):
    pass


print(isinstance(DerivedTest(), Test))
print(isinstance(Test(), Test))
print(type(DerivedTest()) == Test)
print(type(Test()) == Test)

try:
    raise ValueError('1')
except ValueError as error:
    print('2')
    raise ValueError('3')
finally:
    print('4')
