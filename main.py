from hex import Hex
from hex import hex_length,hex_distance,hex_neighbor

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
if __name__ == "__main__":
    main()