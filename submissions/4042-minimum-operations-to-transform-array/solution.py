class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def solve(append, idx):
            if idx >= len(nums1):
                return 0 if not append else float('inf')
            ret = abs(nums1[idx] - nums2[idx]) + solve(append, idx + 1)
            if append:
                ret = min(
                    ret, 
                    1 + abs(nums1[idx] - nums2[idx]) +
                    min(
                        abs(nums2[-1] - nums1[idx]),
                        abs(nums2[-1] - nums2[idx]),
                        0 if min(nums1[idx], nums2[idx]) <= nums2[-1] <= max(nums1[idx], nums2[idx]) else float('inf')
                    ) + solve(False, idx + 1)
                )
            return ret
        return solve(True, 0)
        
