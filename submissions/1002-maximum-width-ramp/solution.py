class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        a = sorted(enumerate(nums), key=lambda x: (x[1], x[0]))

        mindex = a[0][0]
        ret = 0
        for i, num in a[1:]:
            ret = max(ret, i - mindex)
            mindex = min(mindex, i)

        return ret
        
