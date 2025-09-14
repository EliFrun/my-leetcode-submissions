class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        nums.sort()
        s = set([0])
        ret = []
        i = 0
        for x in range(1, len(nums) + 1):
            while i < len(nums) and nums[i] <= x:
                for v in list(s):
                    if v + nums[i] <= k:
                        s.add(v + nums[i])
                i += 1


            if k in s:
                ret.extend([True] * (len(nums) - x + 1))
                break

            curr = False
            for v in s:
                if (k - v) % x == 0 and (k - v) // x <= len(nums) - i:
                    curr = True
            ret.append(curr)

        return ret
            
            
                
        
        
