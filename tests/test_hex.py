import context
import unittest
from hex import Hex
from hex import hex_length, hex_neighbor, hex_distance

class TestHex(unittest.TestCase):

    def test_str(self):
        h = Hex(1,0)
        s = f'{h}'
        self.assertEquals(type(s),str)

    def test_equals(self):
        h1 = Hex(1,0)
        h2 = Hex(1,0)
        self.assertEquals(h1,h2)

    def test_not_equals(self):
        h1 = Hex(1,0)
        h2 = Hex(2,0)
        self.assertNotEquals(h1,h2)

    def test_plus(self):
        h1 = Hex(1,0)
        h2 = Hex(1,0)
        h3 = Hex(2,0)
        self.assertEquals(h1+h2,h3)
    
    def test_minus(self):
        h1 = Hex(1,0)
        h2 = Hex(1,0)
        h3 = Hex(2,0)
        self.assertEquals(h3 - h2, h1)

    def test_multiply(self):
        h1 = Hex(2,0)
        h2 = Hex(2,0)
        h3 = Hex(4,0)

        # case 1
        self.assertEquals(h1 * h2, h3)
        h1 = Hex(0,2)
        h2 = Hex(2,0)
        h3 = Hex(0,0)
        self.assertEquals(h1 * h2, h3)

        # third case
        self.assertEqual(Hex(0,2) * Hex(0,2), Hex(0,4)) 
        self.assertEqual(Hex(-1,-1), Hex(-1,-1), Hex(1,1))

    def test_length(self):
        self.assertEqual(hex_length(Hex(1,0)),1)
        self.assertEqual(hex_length(Hex(0,1)),1)
        self.assertEqual(hex_length(Hex(1,1)),2)
        self.assertEqual(hex_length(Hex(10,1)),11)
        self.assertEqual(hex_length(Hex(10,10)),20)

    def test_distance(self):
        self.assertEqual(hex_distance(Hex(5,0),Hex(0,5)),5)

    def test_neighbors(self):
        # this is pointy vertex up
        # 0 = (1,0)
        # 1 = (1,-1)
        # 2 = (0,-1)
        # 3 = (-1,0)
        # 4 = (-1,1)
        # 5 = (0,1)
        self.assertEqual(hex_neighbor(Hex(0,0),0), Hex(1,0))
        self.assertEqual(hex_neighbor(Hex(0,0),1), Hex(1,-1))
        self.assertEqual(hex_neighbor(Hex(0,0),2), Hex(0,-1))
        self.assertEqual(hex_neighbor(Hex(0,0),3), Hex(-1,0))
        self.assertEqual(hex_neighbor(Hex(0,0),4), Hex(-1,1))
        self.assertEqual(hex_neighbor(Hex(0,0),5), Hex(0,1))

        self.assertEqual(hex_neighbor(Hex(6,6),0), Hex(7,6))
        self.assertEqual(hex_neighbor(Hex(6,6),1), Hex(7,5))
        self.assertEqual(hex_neighbor(Hex(6,6),2), Hex(6,5))
        self.assertEqual(hex_neighbor(Hex(6,6),3), Hex(5,6))
        self.assertEqual(hex_neighbor(Hex(6,6),4), Hex(5,7))
        self.assertEqual(hex_neighbor(Hex(6,6),5), Hex(6,7))