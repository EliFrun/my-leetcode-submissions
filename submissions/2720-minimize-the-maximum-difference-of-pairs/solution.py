class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        def solve(diff):
            ret = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= diff:
                    ret += 1
                    i += 1
                if ret >= p:
                    return True
                i += 1
            return False

        res = right
        while left <= right:
            middle = (left + right) // 2
            if solve(middle):
                res = middle
                right = middle - 1
            else:
                left = middle + 1
        return res
        
