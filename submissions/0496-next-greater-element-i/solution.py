class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        l = [-1] * len(nums2)
        for i, num in reversed(list(enumerate(nums2))):
            while stk and stk[-1] < num:
                stk.pop()
            if stk:
                l[i] = stk[-1]
            stk.append(num)

        d = {num: idx for num, idx in zip(nums2, l)}

        return [d[num] for num in nums1]
