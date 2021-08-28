class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        
        xor = 0
        for n in nums:
            xor ^= n
            
        diff = xor & (-xor)
        
        a, b = 0, 0
        for n in nums:
            if diff & n == 0:
                a ^= n
            else:
                b ^= n
                
                
        return [a, b]
