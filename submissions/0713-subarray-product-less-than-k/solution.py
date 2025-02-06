class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        def solve(lis):
            curr = lis[0]
            left, right = 0, 1
            ret = 0
            while right < len(lis):
                if left >= right:
                    curr *= lis[right]
                    right += 1
                if curr < k:
                    ret += right - left
                    curr *= lis[right]
                    right += 1
                else:
                    curr //= lis[left]
                    left += 1

            while left < len(lis):
                if curr < k:
                    break
                curr //= lis[left]
                left += 1
            if curr < k:
                ret += right - left

            return ret

        return solve(nums)
        
