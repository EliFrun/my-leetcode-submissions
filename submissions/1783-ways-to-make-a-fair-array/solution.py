class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even_left, odd_left = 0, 0
        even_right, odd_right = 0, 0
        for i, num in enumerate(nums):
            if i & 1:
                odd_right += num
            else:
                even_right += num
        ret = 0
        for i, num in enumerate(nums):
            if i & 1:
                odd_right -= num
            else:
                even_right -= num
            
            if even_right + odd_left == even_left + odd_right:
                ret += 1

            if i & 1:
                odd_left += num
            else:
                even_left += num

        return ret

            

        
