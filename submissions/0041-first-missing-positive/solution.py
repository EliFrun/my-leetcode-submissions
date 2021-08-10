class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a = set()
        for num in nums:
            a.add(num)
            
        for i in range(1, 500002):
            if not i in a:
                return i
