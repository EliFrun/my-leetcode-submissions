class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        h1 = []
        h2 = []
        for num in nums:
            if num % 3 == 2:
                heappush(h2, -num)
                if len(h2) > 2:
                    heappop(h2)
            elif num % 3 == 1:
                heappush(h1, -num)
                if len(h1) > 2:
                    heappop(h1)

        h1 = [-x for x in h1]
        h2 = [-x for x in h2]
        
        if s % 3 == 1:
            ret = 0
            if h1:
                ret = s - min(h1)
            if len(h2) > 1:
                ret = max(ret, s - sum(h2))
            return ret
        if s % 3 == 2:
            ret = 0
            if len(h1) > 1:
                ret = max(ret, s - sum(h1))
            if h2:
                ret = max(ret, s - min(h2))
            return ret
        return s
         


            
        
        

    
