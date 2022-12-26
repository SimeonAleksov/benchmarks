obj = {
    "w": 1,
    "x": 2,
    "y": "foo",
    "z": "bar",
}

nested_obj = {
    "foo": 1,
    "bar": "foo",
    "sub": obj,
    "subs": [obj, obj],
}


class ChildTestObject:
    def __init__(self, multiplier=None):
        self.w = 1000 * multiplier if multiplier else 100
        self.x = 20 * multiplier if multiplier else 20
        self.y = "hello" * multiplier if multiplier else "hello"
        self.z = "bar" * multiplier if multiplier else "bar"


class ParentTestObject:
    def __init__(self):
        self.foo = 1
        self.bar = "foo"
        self.sub = ChildTestObject()
        self.subs = [ChildTestObject(i) for i in range(10)]


setup_slots = """
import uuid

class SlotsDTO(object):
    __slots__ = ["uuid", "user_id"]

    def __init__(self, uuid, user_id):
        self.uuid = uuid
        self.user_id = user_id


quote = SlotsDTO(uuid=uuid.uuid4(), user_id=1)
"""

setup_attrs = """
import attr
import uuid

@attr.s(slots=True)
class AttrsDTO:
    uuid = attr.ib()
    user_id = attr.ib()


quote = AttrsDTO(uuid=uuid.uuid4(), user_id=1)
"""
