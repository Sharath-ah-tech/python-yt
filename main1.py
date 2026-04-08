from module import add,sub,mul,div
def add_all(*data):
    print(data)
def sub_all(*d):
    print(d)
def info(**kwargs):
    print(kwargs)
def all(*data, **kwargs):
    print(data, kwargs)
print(add_all(add(5, 3), add(10, 2)))
print(sub_all(sub(sub(10,5),5)))
print(info(name="sundar", age= 45))
print(all(add(5, 3), sub(10, 5), mul(2, 3), div(10, 2), name = 'Sundar', age=25))