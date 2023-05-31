"""The model file for the gem"""
from enum import Enum
from typing import Optional

from pydantic import Field

# from sqlmodel import SQLModel
from database.db import Base


class GemClarity(Enum, int):
    """An enum for the gem's clarity"""
    SI = 1
    VS = 2
    VVS = 3
    FL = 4


class GemColor(Enum, str):
    """The GemColor Enum

    Args:
        Enum (_type_): Enumerator
    """
    D = "D"
    E = "E"
    G = "G"
    F = "F"
    H = "H"
    I = "I"


class GemType(Enum, str):
    """The enum for the gem types

    Args:
        Enum (_type_): The enum for the gems
    """
    DIAMOND = "DIAMOND"
    RUBY = "RUBY"
    SAPPHIRE = "SAPPHIRE"
    EMERALD = "EMERALD"
    TOPAZ = "TOPAZ"
    AMETHYST = "AMETHYST"
    PEARL = "PEARL"
    OBSIDIAN = "OBSIDIAN"
    SQUID = "SQUID"
    CYAN = "CYAN"
    MAGENTA = "MAGENTA"
    YELLOW = "YELLOW"
    BLUE = "BLUE"
    RED = "RED"
    GREEN = "GREEN"
    ORANGE = "ORANGE"
    WHITE = "WHITE"
    BLACK = "BLACK"
    PINK = "PINK"
    PURPLE = "PURPLE"
    GRAY = "GRAY"
    BROWN = "BROWN"
    LIME = "LIME"
    CRIMSON = "CRIMSON"


class Gem(Base):
    """The model for the gem

    Args:
        BaseModel (Pydantic): A pydantic model
    """
    __tablename__ = "gems"

    id: int = Field(primary_key=True)
    price: float
    available: bool = True
    get_type: GemType = GemType.RUBY

    gem_properties_id: Optional[int] = Field(
        default=None, foreign_key="gem_properties.id")


class GemProperties(Base):
    """The model for the gem's properties

    Args:
        BaseModel (Pydantic): A pydantic model
    """
    __tablename__ = "gem_properties"

    id: int = Field(primary_key=True)
    size: float = 1
    clarity: Optional[GemClarity] = None
    color: Optional[GemColor] = None
