class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = len(nums1) + len(nums2)
        for i in range(0, a//2 - (1 if a % 2 == 0 else 0)):
            if nums1 and nums2:
                nums1.pop(0) if nums1[0] < nums2[0] else nums2.pop(0)
            elif nums1:
                nums1.pop(0)
            else:
                nums2.pop(0)
                

        if a % 2 == 0:
            l = []
            for i in range(0,2):
                if nums1 and nums2:
                    if nums1[0] < nums2[0]:
                        l.append(nums1[0])
                        nums1.pop(0)
                    else:
                        l.append(nums2[0])
                        nums2.pop(0)
                elif nums1:
                    l.append(nums1[0])
                    nums1.pop(0)
                else:
                    l.append(nums2[0])
                    nums2.pop(0)
                
            return (l[0] + l[1])/2
        
        else:
            if nums1 and nums2:
                return nums1[0] if nums1[0] < nums2[0] else nums2[0]
            return nums1[0] if nums1 else nums2[0]
