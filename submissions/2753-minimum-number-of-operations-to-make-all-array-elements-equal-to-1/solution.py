class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if 1 in nums:
            return len(nums) - nums.count(1)
        m = float('inf')
        for i in range(len(nums)):
            g = nums[i]
            for j in range(i, len(nums)):
                g = gcd(g, nums[j])
                if g == 1:
                    m = min(m, j - i + 1)
                    break
        if m == float('inf'):
            return -1
        return m - 2 + len(nums)
            

        
