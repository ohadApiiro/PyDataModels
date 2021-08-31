from attr import attrs, attrib

from PyDataModels.BarFile import Bar
from PyDataModels.FooFile import Foo


@attrs
class AttrDataModel:
    product_name = attrib()
    price = attrib()
    def __init__(self):
        bar = Bar()
        self.x = bar.bar_func()
        global_func(bar)


def global_func(bar):
    bar.bar_func()
    return 'abc'

class A:
    def __init__(self):
        self.x = self.blabla()

    def blabla(self):
        return 1

foo = Foo()
global_func(foo)
