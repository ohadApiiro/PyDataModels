from attr import attrs, attrib


@attrs
class AttrDataModel:
    product_name = attrib()
    price = attrib()
