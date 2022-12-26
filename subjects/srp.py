from dataclasses import dataclass
import typing

from serpyco import Serializer


name = "Serpyco"


@dataclass
class SubM:
    w: int
    x: int
    y: str
    z: str


@dataclass
class ComplexM:
    foo: int
    bar: str
    sub: SubM
    subs: typing.List[SubM]


serializer = Serializer(ComplexM)


def serialization_func(obj, many):
    return serializer.dump(obj, many=many)


def deserialzation_func(obj, many):
    return serializer.load(obj, many=many)
