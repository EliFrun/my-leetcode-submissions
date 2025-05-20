class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums) + 1)
        for l, r in queries:
            diff[r + 1] += 1
            diff[l] -= 1

        curr = 0
        for num, d in zip(nums, diff):
            curr += d
            if num + curr > 0:
                return False

        return True
        
