class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.s1 = SortedList(Counter(nums1).items())
        self.s2 = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.s2[self.nums2[index]] -= 1
        if self.s2[self.nums2[index]] == 0:
            self.s2.pop(self.nums2[index])
        self.nums2[index] += val
        self.s2[self.nums2[index]] += 1
        

    def count(self, tot: int) -> int:
        ret = 0
        for k,v in self.s1:
            ret += v * self.s2[tot - k]
            if k >= tot:
                break

        return ret



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
