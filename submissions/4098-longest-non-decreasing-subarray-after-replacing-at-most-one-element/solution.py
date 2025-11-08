class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = []
        curr = [nums[0]]
        for num in nums[1:]:
            if num >= curr[-1]:
                curr.append(num)
            else:
                l.append(curr)
                curr = [num]
        if curr:
            l.append(curr)

        #print(l)

        ret = max([len(x) for x in l])
        for i in range(len(l) - 1):
            left, right = l[i], l[i + 1]
            ret = max(ret, 1 + max(len(left), len(right)))
            if len(left) == 1 or len(right) == 1:
                ret = max(ret, len(left) + len(right))
            if len(left) > 1:
                if left[-2] <= right[0]:
                    ret = max(ret, len(left) + len(right))
            if len(right) > 1:
                if right[1] >= left[-1]:
                    ret = max(ret, len(left) + len(right))
        return ret
            

