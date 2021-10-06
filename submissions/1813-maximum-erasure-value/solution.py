class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        curr = set()
        i, j = 0, 0
        curr_sum = 0
        ret = 0
        for j in nums:
            if j not in curr:
                curr.add(j)
                curr_sum += j
            else:
                ret = max(ret, curr_sum)
                while nums[i] != j:
                    curr.remove(nums[i])
                    curr_sum -= nums[i]
                    i += 1
                i += 1
            
        return max(ret, curr_sum)
