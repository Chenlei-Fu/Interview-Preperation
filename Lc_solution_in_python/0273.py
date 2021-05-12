class Solution:
    def numberToWords(self, num: int) -> str:
        """
        method1: recursion
        """
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        
        def word(num):
            if num == 0:
                return []
            if num < 20:
                return [to19[num-1]]
            if num < 100:
                return [tens[num//10-2]] + word(num % 10)
            if num < 1000:
                return [to19[num//100-1]] + ['Hundred'] + word(num % 100)
            
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if num < 1000**(p+1):
                    return word(num//1000**p) + [w] + word(num%1000**p)
        return ' '.join(word(num)) or 'Zero'


        
    # def numberToWords(self, num: int) -> str:
    #     """
    #     method 2
    #     """
    #     if num == 0:
    #         return 'Zero'
    #     res = ''
    #     for i in range(len(self.thousands)):
    #         if num % 1000 != 0:
    #             res = self.helper(num%1000) + self.thousands[i] + " " + res
    #         num //= 1000
    #     return res.strip()

    
    # def helper(self, num):
    #     if num == 0:
    #         return ""
    #     if num < 20:
    #         return self.lessThan20[num] + " "
    #     if num < 100:
    #         return self.tens[num//10] + " " + self.helper(num % 10)
    #     if num < 1000:
    #         return self.lessThan20[num//100] + " Hundred " + self.helper(num%100)

