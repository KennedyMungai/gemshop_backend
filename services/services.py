"""The services file"""
from random import randint
from string import ascii_uppercase

from models.gem_model import Gem, GemProperties

color_grades = ascii_uppercase[3:9]


def create_gem_props():
    """A function that fills in the gem properties

    Returns:
        gemp_-p: A gem instance
    """
    size = randint(3, 70) / 10
    color = color_grades[randint(0, len(color_grades) - 1)]
    clarity = randint(1, 4)
    gemp_p = GemProperties(size=size, clarity=clarity, color=color)

    return gemp_p


def create_gem(gem_p: int):
    """Function to create gem instances

    Args:
        gem_p (int): An int passed

    Returns:
        Gem: A gem instance
    """
    gem = Gem(price=1000, gem_properties_id=gem_p)

    return gem
