
class Hex:
    """
        https://www.redblobgames.com/grids/hexagons/implementation.html
    """
    def __init__(self, q:int, r:int):
        """ cube storage, axial constructor

        """
        self._q = q
        self._r = r
        self._s = -q - r

        assert(self._q+self._r+self._s == 0)

    @property
    def q(self) -> int:
        return self._q
    
    @q.setter
    def q(self, v:int):
        self._q = v

    @property
    def r(self)->int:
        return self._r
    
    @r.setter
    def r(self, v:int):
        self._r = v

    @property
    def s(self)->int:
        return - self._q - self._r
    
    def __repr__(self) -> str:
        return f'({self.q},{self.r},{self.s})'
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Hex):
            if self.q == other.q and self.r == other.r and self.s == other.s :
                return True
        return False
    
    def __ne__(self, other) -> bool:
        if isinstance(other, Hex):
            if self.q != other.q or self.r != other.r or self.s != other.s:
                return True
            else:
                return False
        else:
            return True

    def __add__(self, other):
        return Hex(self.q + other.q, self.r + other.r)
    
    def __sub__(self, other):
        return Hex(self.q - other.q, self.r - other.r)
        
    def __mul__(self, other):
        return Hex(self.q * other.q, self.r * other.r)
        

def hex_length(h:Hex) -> int:
    return int( (abs(h.q) + abs(h.r) + abs(h.s)) / 2)

def hex_distance(a:Hex, b:Hex) -> int:
    return int(hex_length(a-b))

hex_directions = [
    Hex(1, 0), Hex(1, -1), Hex(0, -1), 
    Hex(-1, 0), Hex(-1, 1), Hex(0, 1)
]

def hex_direction(direction:int) -> Hex:
    # this allows directions outside of the range 0..5
    return hex_directions[(6 + (direction % 6)) % 6]

def hex_neighbor(hex:Hex, direction:int) -> Hex:
    return hex + hex_direction(direction)
