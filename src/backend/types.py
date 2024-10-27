from dataclasses import dataclass


@dataclass
class Column:
    name: str
    type_: str
    is_primary_key: bool


@dataclass
class Difference:
    current: Column | None
    updated: Column | None
