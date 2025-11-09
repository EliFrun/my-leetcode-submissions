class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        #[1,2,0,3]
        indexes = {}
        for i,v in enumerate(nums1):
            indexes[v] = i

        for i in range(len(nums2)):
            nums2[i] = indexes[nums2[i]]

        left = SortedList()
        right = SortedList(nums2)
        ret = 0
        for num in nums2:
            ret += left.bisect_left(num) * (len(right) - right.bisect_left(num) - 1)
            left.add(num)
            right.remove(num)
        return ret
        

        
