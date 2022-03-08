class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ret = sum(nums)
        nums.sort(reverse=True)
        if ret % 3 == 0:
            return ret
        
        mod0 = [x for x in nums if x % 3 == 0]
        mod1 = [x for x in nums if x % 3 == 1]
        mod2 = [x for x in nums if x % 3 == 2]
        
        mod1.sort()
        mod2.sort()
        
        if ret % 3 == 1:
            if len(mod1) != 0 and len(mod2) >= 2:
                return ret - min(mod1[0], mod2[0] + mod2[1]) 
            elif len(mod1) != 0:
                return ret - mod1[0]
            elif len(mod2) >= 2:
                return ret - mod2[0] -mod2[1]
            else:
                return 0
            
        if ret % 3 == 2:
            if len(mod2) != 0 and len(mod1) >= 2:
                return ret - min(mod2[0], mod1[0] + mod1[1])
            elif len(mod2) != 0:
                return ret - mod2[0]
            elif len(mod1) >= 2:
                return ret - mod1[0] -mod1[1]
            else:
                return 0
            
            
        
        

    
