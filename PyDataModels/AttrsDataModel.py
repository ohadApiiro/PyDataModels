from attr import attrs, attrib

from PyDataModels.BarFile import Bar
from PyDataModels.FooFile import Foo


@attrs
class AttrDataModel:
    product_name = attrib()
    price = attrib()

bar = Bar()

bar.bar_func()
def global_func(bla):
    pass


foo = Foo()
global_func(foo)
