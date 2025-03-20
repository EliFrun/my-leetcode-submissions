class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        @cache
        def best_possible_subseq(n, i):
            if len(n) == i:
                return n
            if len(n) < i:
                return ''
            if i == 0:
                return ''
            if i == 1:
                return str(max([int(x) for x in n]))
            return comp(n[0] + best_possible_subseq(n[1:], i - 1), best_possible_subseq(n[1:], i))

        @cache
        def best_combo(s1, s2):
            s1 = [int(x) for x in s1]
            s2 = [int(x) for x in s2]
            ret = []
            while s1 and s2:
                ret.append(max(s1, s2).pop(0))

            if s1:
                ret.extend(s1)
            if s2:
                ret.extend(s2)

            return ret
        
        def comp(s1, s2):
            if len(s1) > len(s2):
                return s1
            if len(s2) > len(s1):
                return s2
            for c1, c2 in zip(s1, s2):
                if int(c1) > int(c2):
                    return s1
                if int(c2) > int(c1):
                    return s2
            return s1
        
        ret = []
        nums1 = ''.join([str(x) for x in nums1])
        nums2 = ''.join([str(x) for x in nums2])
        for i in range(0, k + 1):
            j = k - i
            if len(nums1) < i or len(nums2) < j:
                continue
            n1 = best_possible_subseq(nums1, i)
            n2 = best_possible_subseq(nums2, j)
            num = ''
            
            ret = comp(ret, best_combo(n1,n2))

        return [int(x) for x in ret]

        
