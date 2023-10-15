from __future__ import annotations

import sys

from dataclasses import dataclass
from typing import ClassVar


def fmt(value):
    if value is None:
        return 'nil'

    match value:
        case DNObj():
            return value.fmt()
        case bool():
            return str(value)[0].lower()
        case str():
            return f"'{value}'"
        case tuple():
            contents = ' '.join(fmt(element) for element in value)
            return 'tuple{ ' + contents + ' }'
        case list():
            contents = ' '.join(fmt(element) for element in value)
            return 'list{ ' + contents + ' }'
        case dict():
            contents = ' '.join(f'{fmt(key)} {fmt(val)}' for key, val in value.items())
            return 'hashtable{ ' + contents + ' }'
        case _:
            return str(value)


def prettyfmt(value):
    pass


def display(value, out=sys.stdout):
    pass


def display_pretty(value, out=sys.stdout):
    pass


class DNObj:
    def fmt(self):
        return repr(self)

    def prettyfmt(self):
        return repr(self)

    def print(self, stream=sys.stdout):
        display(self, out=stream)

    def prettyprint(self, stream=sys.stdout):
        display_pretty(self, out=stream)


@dataclass(frozen=True)
class Symbol(DNObj):
    value: str
    _instances: ClassVar[dict[str, Symbol]] = {}

    def fmt(self):
        return f"#{self.value}"

    def prettyfmt(self):
        return self.fmt()

    @classmethod
    def make(cls, value: str):
        sym = cls._instances.get(value)
        if sym is None:
            sym = cls(value)
            cls._instances[value] = sym
        return sym



Value = str | float | int | bool | None | list | dict | tuple | DNObj
