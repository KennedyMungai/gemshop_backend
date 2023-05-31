"""The services file"""
from models.gem_model import Gem


def create_gem(gem_p: int):
    gem = Gem(price=1000, gem_properties_id=gem_p)

    return gem
