"""The services file"""
from models.gem_model import Gem


def create_gem(gem_p: int):
    """Function to create gem instances

    Args:
        gem_p (int): An int passed

    Returns:
        Gem: A gem instance
    """
    gem = Gem(price=1000, gem_properties_id=gem_p)

    return gem
