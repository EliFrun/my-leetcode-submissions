class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            even = set()
            odd = set()
            for j in range(i, len(nums)):
                if nums[j] & 1:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])
                if len(even) == len(odd):
                    ret = max(ret, j - i + 1)
        return ret
        
