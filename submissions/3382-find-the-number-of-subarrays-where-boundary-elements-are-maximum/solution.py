class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        stk = []
        ret = len(nums)
        for num in nums:
            while stk and stk[-1][0] < num:
                stk.pop()

            if stk and stk[-1][0] == num:
                ret += stk[-1][1]
                stk[-1][1] += 1
            else:
                stk.append([num, 1])
        return ret
        
