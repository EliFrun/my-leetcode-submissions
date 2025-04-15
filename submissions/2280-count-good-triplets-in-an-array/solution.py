class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        lis = [0] * len(nums1)
        for i, num in enumerate(nums1):
            lis[num] = i

        for i in range(len(nums2)):
            nums2[i] = lis[nums2[i]]

        s = SortedList([])

        l = []
        for v in nums2:
            idx = s.bisect_right(v)
            l.append(idx)
            s.add(v)


        s = SortedList([])
        for i,v in enumerate(list(reversed(nums2))):
            idx = s.bisect_right(-v)
            l[-i - 1] *= idx
            s.add(-v)

        return sum(l)

        

