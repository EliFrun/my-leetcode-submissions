class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums = sorted(
            [(sum([int(x) for x in str(num)]), num) for num in nums]
        )

        m = -1
        curr = [nums[0][1]]
        curr_dig = nums[0][0]
        for i in range(1, len(nums)):
            if nums[i][0] == curr_dig:
                curr.append(nums[i][1])
            else:
                if len(curr) > 1:
                    m = max(curr[-1] + curr[-2], m)
                curr = [nums[i][1]]
                curr_dig = nums[i][0]

        
        if len(curr) > 1:
            m = max(curr[-1] + curr[-2], m)    

        return m
        
