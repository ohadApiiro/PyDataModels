from PyDataModels.FooFile import Foo


class Bar(Foo):
    def __init__(self):
        self.bar_var = 2

    def bar_func(self):
        print("bar")
