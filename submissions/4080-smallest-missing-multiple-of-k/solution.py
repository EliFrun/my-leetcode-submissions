class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        v = k
        while True:
            if v not in s:
                return v
            v += k
        return -1
