class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 4 or nums[1] <= nums[0]:
            return False
        inc = 1
        cnt = 1
        prev = nums[0]
        for num in nums[1:]:
            if (num - prev) * inc < 0:
                inc *= -1
                cnt += 1
            elif num - prev == 0:
                return False
            prev = num

        print(cnt)
        return cnt == 3
        
