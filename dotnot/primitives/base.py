from __future__ import annotations

import sys

from dataclasses import dataclass
from typing import ClassVar


def fmt(value):
    pass


def prettyfmt(value):
    pass


def display(value, out=sys.stdout):
    pass


def display_pretty(value, out=sys.stdout):
    pass


class DNObj:
    def fmt(self):
        return fmt(self)

    def prettyfmt(self):
        return prettyfmt(self)

    def print(self, stream=sys.stdout):
        display(self, out=stream)

    def prettyprint(self, stream=sys.stdout):
        display_pretty(self, out=stream)


@dataclass(frozen=True)
class Symbol(DNObj):
    value: str
    _instances: ClassVar[dict[str, Symbol]] = {}

    @classmethod
    def make(cls, value: str): 
        sym = cls._instances.get(value)
        if sym is None:
            sym = cls(value)
            cls._instances[value] = sym
        return sym



Value = str | float | int | bool | None | DNObj


