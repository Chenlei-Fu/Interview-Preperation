from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        """
        The even digits all have a unique letter while the odd digits all don't:

        zero: Only digit with z
        two: Only digit with w
        four: Only digit with u
        six: Only digit with x
        eight: Only digit with g

        The odd ones for easy looking, each one's letters all also appear in other digit words:
        one, three, five, seven, nine
        """
        
        res = ''
        res += '0' * s.count('z')
        res += '1' * (s.count('o') - s.count('z') - s.count('w') - s.count('u'))
        res += '2' * s.count('w')
        res += '3' * (s.count('h') - s.count('g'))
        res += '4' * s.count('u')
        res += '5' * (s.count('f') - s.count('u'))
        res += '6' * s.count('x')
        res += '7' * (s.count('s') - s.count('x'))
        res += '8' * s.count('g')
        res += '9' * (s.count('i') - s.count('f') - s.count('x') - s.count('g') + s.count('u'))
        return res
        
        
        
        """
        method 2
        """
        cnt = Counter(s)
        digits = ["zero","two","four","six","eight","one","three","five","seven","nine"]
        ids = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        Counters = [Counter(d) for d in digits]
        Found = [0] * 10
        for it, C in enumerate(Counters):
            k = min(cnt[x] // C[x] for x in C)
            for i in C.keys(): C[i] *= k
            cnt -= C
            Found[ids[it]] = k
        return ''.join([str(i) * Found[i] for i in range(10)])
        
        
            