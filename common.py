import csv

from typing import Protocol


class ItemInterface(Protocol):
    name: str
    days_left: int
    value: int

    def next_day(self) -> None:
        ...


class ItemMaker(Protocol):
    def make(self, name: str, category: str, days_left: int, value: int) -> ItemInterface | None:
        ...


class ItemMakingMapper:
    @classmethod
    def from_csv(cls, path: str, maker: ItemMaker):
        data: dict[str, str] = {}

        with open(path, 'r') as f:
            for row in csv.DictReader(f):
                key = row['name']
                value = row['category']
                data[key] = value

        return ItemMakingMapper(data, maker)

    def __init__(self, mapping: dict[str, str], maker: ItemMaker):
        self._mapping = dict(mapping)
        self._maker = maker

    def make(self, name: str, days_left: int, value: int) -> ItemInterface | None:
        return self._maker.make(name, self._mapping.get(name, ''), days_left, value)
