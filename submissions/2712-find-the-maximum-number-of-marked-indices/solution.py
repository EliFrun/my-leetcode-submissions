class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)//2
        def solve(k):
            for i in range(k):
                if nums[i] * 2 > nums[len(nums) - k + i]:
                    return False
            return True
        ret = 0
        while left <= right:
            middle = (left + right) // 2
            if solve(middle):
                ret = middle
                left = middle + 1
            else:
                right = middle - 1

        return 2 * ret
