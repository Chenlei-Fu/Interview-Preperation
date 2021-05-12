class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """
        think reversely
        """
        target = list(target)
        len_stamp, len_target = len(stamp), len(target)
        stars, visited, res = 0, [0] * len_target, []
        while stars < len_target:
            doneReplace = False
            for i in range(len_target - len_stamp + 1):
                if not visited[i] and self.canReplace(stamp, target, i):
                    stars = self.doReplace(len_stamp, target, i, stars)
                    visited[i] = 1
                    doneReplace = True
                    res.append(i)
                    if stars == len_target:
                        break
            if not doneReplace:
                # cannot replace
                return []
        return reversed(res)
    
    def canReplace(self, stamp, target, p):
        for i in range(len(stamp)):
            if target[i + p] != '*' and target[i + p] != stamp[i]:
                return False
        return True
    
    
    def doReplace(self, len_stamp, target, p, stars):
        for i in range(len_stamp):
            if target[i+p] != '*':
                target[i+p] = '*'
                stars += 1
                
        return stars