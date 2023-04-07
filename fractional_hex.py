from hex import Hex
from hex import hex_length, hex_neighbor, hex_distance
from typing import List



class Fractional_Hex():

    def __init__(self, q:float, r:float):
        self._q = q
        self._r = r
        self._s = -self._q - self._r

        assert(self._q+self._r+self._s == 0)


    def __str__(self):
        return f'{self._q}, {self._r}, {self._s}'

    @property
    def q(self)->float:
        return self._q
    
    @q.setter
    def q(self, v:float):
        self._q = v

    @property
    def r(self)->float:
        return self._r
    
    @r.setter
    def r(self, v:float):
        self._r = v

    @property
    def s(self) -> float:
        return self._s

def hex_round(h:Fractional_Hex) -> Hex:
    q:int = int(round(h.q))
    r:int = int(round(h.r))
    s:int = int(round(h.s))

    q_diff:float = abs(q - h.q)
    r_diff:float = abs(r - h.r)
    s_diff:float = abs(s - h.s)

    if (q_diff > r_diff and q_diff > s_diff):
        q = -r -s 
    elif ( r_diff > s_diff ):
        r = -q -s 
    else:
        s = -q -r
    
    return Hex(q,r)

def lerp(a:float, b:float, t:float) -> float:
    return a * (1-t) + b * t
    # alternatively a + (b-a) * t

def hex_lerp(a:Hex, b:Hex, t:float) -> Fractional_Hex:
    return Fractional_Hex(lerp(a.q, b.q, t),
                          lerp(a.r, b.r, t))
#                          lerp(a.s, b.s, t))

def hex_linedraw(a:Hex,  b:Hex) -> List[Hex]:
    n:int = hex_distance(a, b)

    results:List[Hex] = []
    step:float = 1.0 / max(n, 1)
    i:int = 0
    while i < n:
        results.append(hex_round(hex_lerp(a,b,step * i)))
        i = i + step
    return results


