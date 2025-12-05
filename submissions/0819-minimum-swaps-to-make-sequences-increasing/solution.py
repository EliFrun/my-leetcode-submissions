class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def solve(prev_swapped, i):
            if i >= len(nums1):
                return 0
            v1, v2 = -1, -1
            if i > 0:
                v1 = nums2[i - 1] if prev_swapped else nums1[i - 1]
                v2 = nums1[i - 1] if prev_swapped else nums2[i - 1]
            
            ret = float('inf')
            if nums1[i] > v1 and nums2[i] > v2:
                ret = min(ret, solve(False, i + 1))
            if nums1[i] > v2 and nums2[i] > v1:
                ret = min(ret, 1 + solve(True, i + 1))
            return ret
        return solve(False, 0)
