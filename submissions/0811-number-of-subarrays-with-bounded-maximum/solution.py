class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        good_lists = []
        floor = 0
        for i in range(len(nums)):
            if i == len(nums) - 1 and nums[i] <= right:
                good_lists.append(nums[floor:i + 1])
            if nums[i] > right:
                if i != floor:
                    good_lists.append(nums[floor:i])
                floor = i + 1

        ret = 0
        for l in good_lists:
            bad_lists = []
            floor = 0
            for i in range(len(l)):
                if i == len(l) - 1 and l[i] < left:
                    bad_lists.append(l[floor:i + 1])
                if l[i] >= left:
                    if i != floor:
                        bad_lists.append(l[floor:i])
                    floor = i + 1

            count = 0

            for lis in bad_lists:
                ll = len(lis)
                count += ll * (ll + 1) / 2
            n = len(l)
            ret += n * ( n + 1 ) / 2 - count

        return int(ret)
        
