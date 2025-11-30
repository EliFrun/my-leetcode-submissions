class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ret = float('inf')

        d = {}
        for i, num in reversed(list(enumerate(nums))):
            if (v := int(str(num)[::-1])) in d:
                ret = min(ret, d[v] - i)
            d[num] = i
        if ret != float('inf'):
            return ret
        return -1
            
            
        
