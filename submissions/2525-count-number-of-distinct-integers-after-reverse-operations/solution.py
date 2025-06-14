class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set()
        nums = set(nums)
        for x in nums:
            s.update([x, int(str(x)[::-1])])
        return len(s)
        
