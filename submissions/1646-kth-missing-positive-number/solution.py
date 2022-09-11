class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        return sorted(list(set(range(1, 2002)).difference(set(arr))))[k -1]
        
