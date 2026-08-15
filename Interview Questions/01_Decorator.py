def my_decorator(func):

    def wrapper():
        print("successfull")
        func()
    return wrapper

@my_decorator
def hello_func():
    print("hello")

hello_func()


def my_decorator_v2(func):

    def wrapper_v2(x,y):
        print("About adding two numbers")
        return func(x,y)
    return wrapper_v2

@my_decorator_v2
def add(x,y):
    return x + y

result = add(10,20)
print('result:',result)