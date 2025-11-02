class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: abs(x))
        return abs(nums[-1] * nums[-2] * 100_000)
