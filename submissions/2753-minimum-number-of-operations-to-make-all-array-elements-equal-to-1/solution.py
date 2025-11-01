class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if 1 in nums:
            return len(nums) - nums.count(1)

        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)

        min_length = float('inf')
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i, len(nums)):
                curr = gcd(curr, nums[j])
                if curr == 1:
                    min_length = min(min_length, j - i + 1)
            if min_length == float('inf'):
                return -1
        return len(nums) + min_length - 2

        
