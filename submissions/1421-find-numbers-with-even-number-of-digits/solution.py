class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for x in nums if int(log10(x)) & 1)
