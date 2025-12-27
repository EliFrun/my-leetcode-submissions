class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        m = 0
        for i, v in enumerate(arr):
            m = min(m + 1, v)
        return m

        
