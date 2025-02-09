class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        if len(nums2) == 1:
            return min([nums2[0] - x for x in nums1])
        
        if len(nums2) == 2:
            m = 1_000_000
            for i in range(4):
                for j in range(i + 1, 4):
                    if nums2[0] - nums1[i] == nums2[1] - nums1[j]:
                        m = min(m, nums2[0] - nums1[i])

            return m

        diffs = defaultdict(int)
        for _ in range(3):
            for i, j in zip(nums1, nums2):
                if j == -1:
                    continue
                diffs[j - i] += 1
            nums2 = [-1] + nums2

        return sorted(diffs.items(), key=lambda x: (x[1], -x[0]))[-1][0]
        
