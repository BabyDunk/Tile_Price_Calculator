from os import system, name
from math import floor


class CoverCost:
    """
    CoverCost will aid in getting the cost for tiles of any given area

    Can handle metric or imperial measurements
    """
    # Class Attributes
    inch = 8.333
    measurement = ''
    width_int = 0
    width_fact = 0
    height_int = 0
    height_fact = 0
    tile_width = 0
    tile_height = 0
    tile_count = 0
    box_price = 0
    total = 0

    def __init__(self):
        pass

    def __str__(self):
        pass

    def set_metric(self):
        """
        Set measurement type True to indicate is_metric() is set to metric
        :return: none
        """
        self.measurement = True

    def set_imperial(self):
        """
        Set measurement type False to indicate is_metric() is set to imperial
        :return: none
        """
        self.measurement = False

    def is_metric(self):
        """
        Checks if is metric, if False would imply that it's imperial
        :return: boolean
        """
        return self.measurement

    def add_width_int(self, width):
        """
        Sets work area width integer
        :param width: int
        :return: int
        """
        self.width_int = width
        return self.width_int

    def add_width_fact(self, width):
        """
        Sets work area fraction
        :param width: int
        :return: int
        """
        self.width_fact = width
        return self.width_fact

    def add_height_int(self, height):
        """
        Sets work area height integer
        :param height: int
        :return: int
        """
        self.height_int = height
        return self.height_int

    def add_height_fact(self, height):
        """
        Sets work area height fraction
        :param height: int
        :return: int
        """
        self.height_fact = height
        return self.height_fact

    def add_tile_width(self, width):
        """
        Sets title width
        :param width: float
        :return: float
        """
        self.tile_width = width
        return self.tile_width

    def add_tile_height(self, height):
        """
        Set tile height
        :param height: float
        :return: float
        """
        self.tile_height = height
        return self.tile_height

    def box_tile_count(self, count):
        """
        Sets tile count in box
        :param count: int
        :return: int
        """
        self.tile_count = count
        return self.tile_count

    def price_per_box(self, price):
        """
        Set price per box of tiles
        :param price: float
        :return: float
        """
        self.box_price = price
        return self.box_price

    def get_total(self):
        """
        Return price total
        :return: float
        """
        return self.total

    def inch_frac_foot(self, inch_count):
        """
        Converts float to inch ratio
        :param inch_count: float
        :return: float
        """
        return float((self.inch * inch_count) / 100)

    def tiles_needed(self):
        """
        Counts the number of tiles needed
        Calculations are done by getting the work area and the tile area, then dividing the two
        rounded up to the nearest whole number
        :return: int
        """

        if self.is_metric():
            width_fact = self.width_fact / 100
            height_fact = self.height_fact / 100
            tile_width = (self.tile_width / 10) / 100
            tile_height = (self.tile_height / 10) / 100
        else:
            width_fact = self.inch_frac_foot(self.width_fact)
            height_fact = self.inch_frac_foot(self.height_fact)
            tile_width = self.inch_frac_foot(self.tile_width)
            tile_height = self.inch_frac_foot(self.tile_height)

        tile_size = tile_width * tile_height
        work_area = (self.width_int + width_fact) * (self.height_int + height_fact)

        if work_area % tile_size == 0:
            tiles_needed = (work_area / tile_size)
        else:
            tiles_needed = (floor(work_area / tile_size)) + 1

        return tiles_needed

    def boxes_needed(self):
        """
        Calculates the total number of boxes needed for the give work area
        :return:  int
        """

        tiles = self.tiles_needed()

        if tiles % self.tile_count == 0:
            tiles_needed = tiles / self.tile_count
        else:
            tiles_needed = floor(tiles / self.tile_count) + 1

        return tiles_needed

    def cal_total(self):
        """
        Adds the complete price to the total
        :return: float
        """
        self.total = self.boxes_needed() * self.box_price
        return self.total

    @staticmethod
    def clear_console():
        """
        Clears console of previous prints
        :return: none
        """
        if name == 'posix':
            _ = system('clear')
        else:
            _ = system('cls')
