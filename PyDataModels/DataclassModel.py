from dataclasses import dataclass
from dataclasses import field
from dataclasses import make_dataclass

C = make_dataclass('C',
                   [('x', int),
                     'y',
                    ('z', int, field(default=5))],
                   namespace={'add_one': lambda self: self.x + 1})


@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    mylist: list[int] = field(default_factory=list)