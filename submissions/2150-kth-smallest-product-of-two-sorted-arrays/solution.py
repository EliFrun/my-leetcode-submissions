class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        negs1 = nums1[:bisect_right(nums1, 0)]
        pos1 = nums1[bisect_right(nums1, 0):]
        negs2 = nums2[:bisect_right(nums2, 0)]
        pos2 = nums2[bisect_right(nums2, 0):]
        inverted_negs1 = [-x for x in negs1][::-1]
        inverted_negs2 = [-x for x in negs2][::-1]

        def f1(l1, l2, x):
            if not l2:
                return 0
            ret = 0
            for v in l1:
                if v == 0:
                    if x > 0:
                        ret += len(l2)
                    elif x == 0:
                        ret += bisect_right(l2, 0)
                    continue
                ret += bisect_right(l2, x/v)
            return ret



        def counting_function(x):

            return f1(pos1, pos2, x) + f1(pos1, negs2, x) + f1(pos2, negs1, x) + f1(inverted_negs1, inverted_negs2, x)

        
        left = min(nums1[0] * nums2[0], nums1[-1] * nums2[-1], nums1[0] * nums2[-1], nums1[-1] * nums2[0])
        right = max(nums1[0] * nums2[0], nums1[-1] * nums2[-1], nums1[0] * nums2[-1], nums1[-1] * nums2[0])
        while left < right:
            middle = (left + right) // 2
            if counting_function(middle) < k:
                left = middle + 1
            else:
                right = middle

        return left
                
        
