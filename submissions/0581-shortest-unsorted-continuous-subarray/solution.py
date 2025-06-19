class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s = sorted(nums)
        mi, ma = -1, -2
        for i in range(len(nums)):
            if nums[i] != s[i]:
                if mi == -1:
                    mi = i
                    break
        if mi >= 0:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] != s[i]:
                    if ma == -2:
                        ma = i
                        break


        return ma - mi + 1

        
