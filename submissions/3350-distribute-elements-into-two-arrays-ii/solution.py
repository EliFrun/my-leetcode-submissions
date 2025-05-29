class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        s1, s2 = SortedList(), SortedList()
        s1.add(nums[0])
        s2.add(nums[1])
        lis1 = [nums[0]]
        lis2 = [nums[1]]
        for i in range(2, len(nums)):
            l1 = len(s1) - s1.bisect_right(nums[i])
            l2 = len(s2) - s2.bisect_right(nums[i])
            if l1 > l2:
                s1.add(nums[i])
                lis1.append(nums[i])
            elif l2 > l1:
                s2.add(nums[i])
                lis2.append(nums[i])
            else:
                if len(s1) <= len(s2):
                    s1.add(nums[i])
                    lis1.append(nums[i])
                else:
                    s2.add(nums[i])
                    lis2.append(nums[i])



        return lis1 + lis2

