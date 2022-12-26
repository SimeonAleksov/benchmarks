import typing
import time
import timeit
from contextlib import contextmanager

from tabulate import tabulate

from data import nested_obj, ParentTestObject, setup_attrs, setup_slots


@contextmanager
def timer(tracker):
    start = time.time()
    yield
    end = time.time()
    tracker += [end - start]


class Benchmark:
    def __init__(
        self,
        deserialization_func: typing.Callable,
        serialization_func: typing.Callable,
        name: str,
    ):
        self.serialize = serialization_func
        self.deserialize = deserialization_func
        self.name = name
        self.obj = ParentTestObject()

    def time_one(self):
        row = [self.name + " - Serialize - One"]
        with timer(row):
            self.serialize_one()
        return row

    def time_many(self):
        row = [self.name + " - Serialize - Many"]
        with timer(row):
            self.serialize_many()
        return row

    def time_one_deserialize(self):
        row = [self.name + " - Deserialize - One"]
        with timer(row):
            self.deserialize_one()
        return row

    def time_many_deserialize(self):
        row = [self.name + " - Deserialize - Many"]
        with timer(row):
            self.deserialize_many()
        return row

    def serialize_one(self, limit=1000):
        for i in range(0, limit):
            self.serialize(self.obj, False)

    def serialize_many(self, limit=1000):
        for i in range(0, limit):
            self.serialize([self.obj, self.obj, self.obj], True)

    def deserialize_one(self, limit=1000):
        for i in range(0, limit):
            self.deserialize(nested_obj, False)

    def deserialize_many(self, limit=1000):
        for i in range(0, limit):
            self.deserialize([nested_obj, nested_obj, nested_obj], True)

    @classmethod
    def access_time(cls):
        attrs = timeit.Timer(
            "quote.user_id; quote.uuid",
            setup=setup_attrs,
        ).repeat(100)
        slots = timeit.Timer(
            "quote.user_id; quote.uuid",
            setup=setup_slots,
        ).repeat(100)
        table = [
            ["Attrs - access time", sum(attrs) / len(attrs)],
            ["Slots - access time", sum(slots) / len(slots)],
        ]

        print(
            tabulate(
                table,
                headers=["Library", "Duration (seconds)"],
            )
        )
