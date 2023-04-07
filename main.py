from hex import Hex
from hex import hex_length,hex_distance,hex_neighbor
from fractional_hex import Fractional_Hex, hex_round, hex_linedraw

def main():
    h = Hex(1,1)
    print(h)
    h2 = Hex(2,0)
    print(h2)

    print((h == h2))
    print((h != h2))

    print(h + h2)
    print(h - h2)
    print(h * h2)
    print(hex_length(h))
    print(hex_distance(h,h2))

    for i in range(0,5):
        print(hex_neighbor(h,i))

    fh1 = Fractional_Hex(10.0, 10.0)
    fh2 = Fractional_Hex(20.0, 20.0)

    f1 = Hex(10,20)
    f2 = Hex(10,22)
    for item in hex_linedraw(f1, f2):
        print(item)

if __name__ == "__main__":
    main()