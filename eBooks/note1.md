# Notes - Elements of Programming Interviews in Python
## Content
[Chapter 1: Primitive Types](#Primitive Types)
* [a. facts of bitwise calculations](#a. facts of bitwise calculations)
* [b. parity](# b. parity)




### 1. Primitive Types
#### a. facts of bitwise calculations
1. `x & 1` -- calculate number of bits
2. `x ^ 1` -- for calculate parity (number of 1 is odd or even)
3. `x & (x - 1)` -- erase the lowest set bit (lowest 1), also used for parity

#### b. parity
The parity of a binary word
	= 1 if the number of 1s in the word is odd
	= 0 								   even

1. `x & (x-1)`
```python
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
```


2. divide into two parts each time
```python
def parity(x): #64 bits
	x ^= x >> 32
	x ^= x >> 16
	x ^= x >> 8
	x ^= x >> 4
	x ^= x >> 2
	x ^= x >> 1
	return x & 0x1 
```

3. cache: sacrifice the space complexity


#### c. some cool bit manipulation tricks
[code](code/bit_manipulatio.py)





							