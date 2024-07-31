def mydecoration(fun):
    def wrapper():
        print("i am decorating your function")
        fun()
    return wrapper
def hello() :
    print("hello")
mydecoration(hello)()