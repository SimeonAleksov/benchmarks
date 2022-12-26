from tabulate import tabulate

from benchmark import Benchmark
from subjects import marshmallow, pdnt, srp, drf


def benchmark():
    table = []
    _subjects = (marshmallow, pdnt, srp, drf)
    for sub in _subjects:
        bench = Benchmark(
            sub.deserialzation_func,
            sub.serialization_func,
            sub.name,
        )
        row = bench.time_one()
        table.append(row)
        row = bench.time_one_deserialize()
        table.append(row)
        many = bench.time_many()
        table.append(many)
        row = bench.time_many_deserialize()
        table.append(row)

    print(
        tabulate(
            table,
            headers=["Library - Action", "Duration (seconds)"],
        )
    )
    print("#" * 60)
    Benchmark.access_time()


if __name__ == "__main__":
    benchmark()
