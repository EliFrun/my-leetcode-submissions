class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(
            sum([int(y) for y in str(x)]) for x in nums
        )
