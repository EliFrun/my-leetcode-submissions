class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def solve(i):
            diff_array = [0 for _ in range(len(nums) + 1)]
            for l,u,d in queries[:i]:
                diff_array[l] -= d
                diff_array[u + 1] += d

            curr = 0
            for i in range(len(nums)):
                curr += diff_array[i]
                if nums[i] + curr > 0:
                    return False
            return True

        if not solve(len(queries)):
            return -1

        low, high = 0, len(queries)
        while high - low > 1:
            middle = (high + low) // 2
            if solve(middle):
                high = middle
            else:
                low = middle
        
        if solve(low):
            return low
        return high
        
