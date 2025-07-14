class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ret = 0
        while nums:
            if len(nums) > 1:
                n2, n1 = nums.pop(), nums.pop(0)
                ret += int(f'{n1}{n2}')
            else:
                ret += nums.pop()
        return ret
        
