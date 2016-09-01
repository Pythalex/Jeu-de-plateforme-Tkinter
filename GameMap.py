"""
Maps script
use for display the game levels

Alexandre BONIN - Python 3.5 - 2016
"""


class Map(object):

    def __init__(self, geometry : tuple, base_level = 5):

        self.width = geometry[0]
        self.height = geometry[1]

        self.base_level = base_level



