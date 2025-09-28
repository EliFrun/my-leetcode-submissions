class Solution:
    def splitArray(self, nums: List[int]) -> int:
        l = []
        r_first = 0
        while nums and (not l or nums[0] > l[-1]):
            l.append(nums.pop(0))

        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                return -1


        
        s1 = sum(l)
        s2 = sum(nums)
        ret = abs(s1 - s2)
        if not nums or l[-1] > nums[0]:
            s2 += l[-1]
            s1 -= l[-1]
            ret = min(ret, abs(s2 -s1))
        return ret
            

            

        

            
        
