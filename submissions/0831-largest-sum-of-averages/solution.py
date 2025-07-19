class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        @cache
        def solve(i, left):
            if left == 0:
                if i < len(nums):
                    return sum(nums[i:])/ (len(nums) - i)
                return float('-inf')
            if i >= len(nums):
                return float('-inf')
            
            ret = 0
            for j in range(i, len(nums) + 1):
                ret = max(ret, sum(nums[i:j + 1])/ (j - i + 1) + solve(j + 1, left - 1))
            return ret

        return solve(0, k - 1)

        
