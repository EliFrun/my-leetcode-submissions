class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = [x for x in list(set(nums)) if x > 0]
        return sum(s) if s else max(list(set([x for x in nums if x <= 0])))
