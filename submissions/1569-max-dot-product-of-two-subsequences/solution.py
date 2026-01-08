class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def solve(i, j):
            if i >= len(nums1):
                return 0
            if j >= len(nums2):
                return 0
            return max(max(0, nums1[i] * nums2[j]) + solve(i + 1, j + 1), solve(i + 1, j), solve(i, j + 1))
        if all(x < 0 for x in nums1) and all(x > 0 for x in nums2):
            return max(nums1) * min(nums2)
        if all(x > 0 for x in nums1) and all(x < 0 for x in nums2):
            return min(nums1) * max(nums2)
        
        return solve(0, 0)
