class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ret = [0] * max(nums1[-1][0], nums2[-1][0])
        for idx, val in nums1:
            ret[idx - 1] += val

        for idx, val in nums2:
            ret[idx - 1] += val

        return [[idx + 1, val] for idx, val in enumerate(ret) if val > 0]
        
