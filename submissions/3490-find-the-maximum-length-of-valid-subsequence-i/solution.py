class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        dp = [[0] * 4 for _ in range(len(nums))]
        best = [0] * 4
        # 0 0 -> even mod, prev number even
        # 0 1 -> even mod, prev number odd
        # 1 0 -> odd mod, prev number even
        # 1 1 -> odd mod, prev number odd

        for num in nums:
            if num & 1:
                best[3] = max(best[3], best[2] + 1)
                best[1] += 1
            else:
                best[0] += 1
                best[2] = max(best[2], best[3] + 1)


        return max(best)




        
