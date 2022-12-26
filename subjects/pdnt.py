import pydantic
import typing

name = "Pydantic"


class SubM(pydantic.BaseModel):
    w: int
    x: int
    y: str
    z: str


class ComplexM(pydantic.BaseModel):
    foo: int
    bar: str
    sub: SubM
    subs: typing.List[SubM]


def serialization_func(obj, many):
    if many:
        return [
            ComplexM(
                foo=o.foo,
                bar=o.bar,
                sub=SubM(**o.sub.__dict__),
                subs=[SubM(**sub.__dict__) for sub in o.subs],
            ).dict()
            for o in obj
        ]
    return ComplexM(
        foo=obj.foo,
        bar=obj.bar,
        sub=SubM(**obj.sub.__dict__),
        subs=[SubM(**sub.__dict__) for sub in obj.subs],
    )


def deserialzation_func(obj, many):
    if many:
        return pydantic.parse_obj_as(typing.List[ComplexM], obj)
    return ComplexM.parse_obj(obj)
