class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res1 = [0] * 32
        for num in nums1:
            for i in range(32):
                res1[i] += len(nums2) * (num & 1)
                num >>= 1

        res2 = [0] * 32
        for num in nums2:
            for i in range(32):
                res2[i] += len(nums1) * (num & 1)
                num >>= 1
        
        res = 0
        i = 0
        for a,b in zip(res1, res2):
            if a & 1 != b & 1:
                res += int(2 ** i)
            i += 1

        return res

