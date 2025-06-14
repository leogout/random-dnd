from enum import Enum
from pydantic import BaseModel


class Race(str, Enum):
    DWARF = "dwarf"
    ELF = "elf"
    HALFLING = "halfling"
    HUMAN = "human"
    GNOME = "gnome"
    HALF_ORC = "half-orc"


class Languages(str, Enum):
    FRENCH = "french"
    ENGLISH = "english"


class Character(BaseModel):
    race: Race