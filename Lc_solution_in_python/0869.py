class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        """
        因为reorder的string的共同特征就是他们的counter相同，
        先得到counter
        再看看数字范围内是否有某个2的次方数counter与N相同
        """
        # c = collections.Counter(str(N))
        # for i in range(30):
        #     if c == collections.Counter(str(1 << i)):
        #         return True
        # return False
        
        """
        method2: sorted
        """
        return sorted(str(N)) in [sorted(str(1 << i)) for i in range(30)]