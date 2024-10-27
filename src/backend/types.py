from dataclasses import dataclass


@dataclass
class Field:
    name: str
    type_: str
    is_primary_key: bool


@dataclass
class Difference:
    current: Field | None
    updated: Field | None
