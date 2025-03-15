class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        vals = sorted(list(set(nums)))
        def solve(m):
            memo = [0] * (len(nums) + 2)
            for i in range(len(nums) - 1, -1, -1):
                memo[i] = max((1 if nums[i] <= m else 0) + memo[i + 2], memo[i + 1])
            return memo[0] >= k

        left, right = 0, len(vals) - 1
        while right - left > 1:
            middle = (left + right) // 2
            if solve(vals[middle]):
                right = middle
            else:
                left = middle

        if solve(vals[left]):
            return vals[left]
        return vals[right]
            


