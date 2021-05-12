class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return -1
        row, col = len(mat), len(mat[0])
        pointers, curMax = [0] * row, 0
        
        # get curMax at the first col
        for i in range(row):
            curMax = max(curMax, mat[i][0])
        
        while True:
            haveCommon = True
            for i in range(row):
                while pointers[i] < col and mat[i][pointers[i]] < curMax:
                    pointers[i] += 1
                    haveCommon = False
                if pointers[i] == col:
                    return -1
                
                curMax = max(curMax, mat[i][pointers[i]])
                
            if haveCommon:
                break
        return curMax

# from bisect import bisect_left
# class Solution:
#     def smallestCommonElement(self, mat: List[List[int]]) -> int:
#         """
#         Binary Search
#         """
#         row, col = len(mat), len(mat[0])
#         pos = [0] * row
#         for i in range(col): # for every element at the first row
#             have_common = True
#             for j in range(1, row):
                
#                 res = self.binary_search(mat[j][pos[j]: col], mat[0][i])
                
#                 if res == -1: # not found
#                     have_common = False
#                     break
#                 else:
#                     pos[j] = res
            
#             if have_common:
#                 return mat[0][i]
#         return -1
                          
#     def binary_search(self, a, x):
#         i = bisect_left(a, x) 
#         if i != len(a) and a[i] == x: 
#             return i 
#         else: 
#             return -1
        