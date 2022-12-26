import marshmallow

name = "Marshmallow"


class SubM(marshmallow.Schema):
    w = marshmallow.fields.Int()
    x = marshmallow.fields.Int()
    y = marshmallow.fields.Str()
    z = marshmallow.fields.Str()


class ComplexM(marshmallow.Schema):
    foo = marshmallow.fields.Int()
    bar = marshmallow.fields.Str()
    sub = marshmallow.fields.Nested(SubM)
    subs = marshmallow.fields.Nested(SubM, many=True)


def serialization_func(obj, many):
    return ComplexM().dump(obj, many=many)


def deserialzation_func(obj, many):
    return ComplexM().load(obj, many=many)
