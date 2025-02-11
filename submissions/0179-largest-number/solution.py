class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return str(int(''.join(sorted([str(x) for x in nums], reverse=True, key=lambda x: x * (10//len(x) + 1)))))
        
