class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = 0
        c1 = 0
        n2 = 0
        c2 = 0
        for num in nums1:
            n1 += num
            c1 += 0 if num else 1

        for num in nums2:
            n2 += num
            c2 += 0 if num else 1

        if n1 + c1 == n2 + c2:
            return n1 + c1
        if n1 + c1 > n2 + c2:
            if c2:
                return n1 + c1
            return -1
        if n1 + c1 < n2 + c2:
            if c1:
                return n2 + c2
            return -1

        
