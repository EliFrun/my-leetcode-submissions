class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:  
        lis = []
        for x in matrix:
            lis += x
            
        lis.sort()
        
        return lis[k - 1]
        
