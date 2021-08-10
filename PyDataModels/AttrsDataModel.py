from attr import attrs, attrib

from PyDataModels.BarFile import Bar
from PyDataModels.FooFile import Foo


@attrs
class AttrDataModel:
    product_name = attrib()
    price = attrib()
    def __init__(self):
        bar = Bar
        self.x = bar.bar_func()

bar = Bar()

bar.bar_func()
def global_func(bla):
    pass

class A:
    def __init__(self):
        self.x = self.blabla()

    def blabla(self):
        return 1

foo = Foo()
global_func(foo)
