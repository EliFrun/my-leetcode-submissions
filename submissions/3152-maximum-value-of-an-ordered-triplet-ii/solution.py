class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        mi, ma, ret = 0,0,0
        for num in nums:
            ret = max((mi * num), ret)
            ma = max(ma, num)
            mi = max(ma - num, mi)

        return ret
        
