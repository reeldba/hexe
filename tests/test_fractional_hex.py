import context
import unittest
from hex import Hex
from hex import hex_length, hex_neighbor, hex_distance
from fractional_hex import Fractional_Hex


class TestFractionalHex(unittest.TestCase):

    def test_str(self):
        h = Fractional_Hex(10.0,10.0)
        s = f'{h}'
        self.assertEquals(type(s),str)