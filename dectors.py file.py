def display(func):
    def inner():
        print("hello-----")
        func()
    return inner
@ display
def show():
    print("narendra")
show()
