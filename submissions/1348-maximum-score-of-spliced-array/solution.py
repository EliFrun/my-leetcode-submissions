class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        d = [y - x for x,y in zip(nums1, nums2)]
        s1 = sum(nums1)
        s2 = sum(nums2)

        ma = 0
        curr = 0
        left = 0
        for v in d:
            curr += v
            while curr < 0:
                curr -= d[left]
                left += 1
            ma = max(curr, ma)

        mi = 0
        curr = 0
        left = 0
        for v in d:
            curr += v
            while curr > 0:
                curr -= d[left]
                left += 1
            mi = min(curr, mi)

        return max(s1 + ma, s2 - mi, s1, s2)

        
        
