class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        ret = list(set(nums1) & set(nums2))

        l = []
        for v in ret:
            l += [v] * min(c1[v], c2[v])
        return l


        
