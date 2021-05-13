# Notes - Elements of Programming Interviews in Python
## Content
[Chapter 1: Primitive Types](#Primitive Types)
* [a. facts of bitwise calculations](#a. facts of bitwise calculations)
* [b. parity](# b. parity)
* [c. some cool bit manipulation tricks](#c. some cool bit manipulation tricks)




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
1. Set n<sup>th</sup> bit

```
x | (1<<n)
```

2. Unset n<sup>th</sup> bit

 ```
x & ~(1<<n)
 ```

3. Toggle n<sup>th</sup> bit

```
x ^ (1<<n)
```

4. Round up to the next power of two

```
unsigned int v; //only works if v is 32 bit
v--;
v |= v >> 1;
v |= v >> 2;
v |= v >> 4;
v |= v >> 8;
v |= v >> 16;
v++;
```

5. Round down / floor a number**

```
n >> 0

5.7812 >> 0 // 5

```

6. Get the maximum integer**

```
int maxInt = ~(1 << 31);
int maxInt = (1 << 31) - 1;
int maxInt = (1 << -1) - 1;
int maxInt = -1u >> 1;
```

7. Get the minimum integer

```
int minInt = 1 << 31;
int minInt = 1 << -1;
```

8. Get the maximum long

```
long maxLong = ((long)1 << 127) - 1;
```

9. Multiply by 2

```
n << 1; // n*2
```

10. Divide by 2

```
n >> 1; // n/2
```

11. Multiply by the m<sup>th</sup> power of 2

```
n << m;
```

12. Divide by the m<sup>th</sup> power of 2

```
n >> m;
```

13. Check Equality

<sub>*This is 35% faster in Javascript*</sub>

```
(a^b) == 0; // a == b
!(a^b) // use in an if
```

14. Check if a number is odd

```
(n & 1) == 1;
```

15. Exchange (swap) two values

```
//version 1
a ^= b;
b ^= a;
a ^= b;

//version 2
a = a ^ b ^ (b = a)
```

16. Get the absolute value

```
//version 1
x < 0 ? -x : x;

//version 2
(x ^ (x >> 31)) - (x >> 31);
```

17. Get the max of two values

```
b & ((a-b) >> 31) | a & (~(a-b) >> 31);
```

18. Get the min of two values

```
a & ((a-b) >> 31) | b & (~(a-b) >> 31);
```

19. Check whether both numbers have the same sign

```
(x ^ y) >= 0;
```

20. Flip the sign

```
i = ~i + 1; // or
i = (i ^ -1) + 1; // i = -i
```

21. Calculate 2<sup>n</sup>

```
1 << n;
```

22. Whether a number is power of 2

```
n > 0 && (n & (n - 1)) == 0;
```

23. Modulo 2<sup>n</sup> against m

```
m & ((1 << n) - 1);
```

24. Get the average

```
(x + y) >> 1;
((x ^ y) >> 1) + (x & y);
```

25. Get the m<sup>th</sup> bit of n (from low to high)

```
(n >> (m-1)) & 1;
```

26. Set the m<sup>th</sup> bit of n to 0 (from low to high)

```
n & ~(1 << (m-1));
```

27. Check if n<sup>th</sup> bit is set

```
if (x & (1<<n)) {
  n-th bit is set
} else {
  n-th bit is not set
}
```

28. Isolate (extract) the right-most 1 bit

```
x & (-x)
```

29. Isolate (extract) the right-most 0 bit

```
~x & (x+1)
```

30. Set the right-most 0 bit to 1

```
x | (x+1)
```

31. Set the right-most 1 bit to 0

```
x & (x-1)
```

32. n + 1

```
-~n
```

33. n - 1

```
~-n
```

34. Get the negative value of a number

```
~n + 1;
(n ^ -1) + 1;
```

35. `if (x == a) x = b; if (x == b) x = a;`

```
x = a ^ b ^ x;
```

36. Swap Adjacent bits

```
((n & 10101010) >> 1) | ((n & 01010101) << 1)
```

37. Different rightmost bit of numbers m & n

```
(n^m)&-(n^m) // returns 2^x where x is the position of the different bit (0 based)
```

38. Common rightmost bit of numbers m & n

```
~(n^m)&(n^m)+1 // returns 2^x where x is the position of the common bit (0 based)
```



### 2. LinkedList

Tips:

* Algorithms operating on singly linked lists often beneﬁt from using two iterators, one ahead of the other, or one advancing quicker than the other.
* It’s easy to forget to update next (and previous for double linked list) for the head and tail.

* List problems often have a simple brute-force solution that uses O(n) space, but a subtler solution that uses the existing list nodes to reduce space complexity to O(1).

