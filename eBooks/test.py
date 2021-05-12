def parity(x):
    result = 0
    while x:
        result ^= 1
        print("result:", bin(result))
        x &= x - 1 # drop the lowest set bit of x
        print("x:", bin(x))
    return result

x = 0b00101100
parity(x)

"""
result 0b1 -- count one 1s
x 0b101000 -- erase lowest 1
result 0b0 -- count two 1s
x 0b100000 -- erase lowest 1
result 0b1 -- count three 1s
x 0b0 -- erase lowest 1
"""