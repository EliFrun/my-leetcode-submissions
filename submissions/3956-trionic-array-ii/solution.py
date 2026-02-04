class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        decreasing = []


        i = 1
        while i < len(nums) - 1:
            left = i
            while i < len(nums) - 2 and nums[i + 1] < nums[i]:
                i += 1
            if left != i:
                decreasing.append([left, i])
            i += 1

        ret = float('-inf')
        for l, r in decreasing:
            s = 0
            for i in range(l, r + 1):
                s += nums[i]
            
            ls = 0
            lb = float('-inf')
            while l > 0 and nums[l - 1] < nums[l]:
                l -= 1
                ls += nums[l]
                if ls > lb:
                    lb = ls

            rs = 0
            rb = float('-inf')
            while r < len(nums) - 1 and nums[r + 1] > nums[r]:
                r += 1
                rs += nums[r]
                if rs > rb:
                    rb = rs

            if s + lb + rb > ret:
                ret = s + lb + rb
        return ret
        
