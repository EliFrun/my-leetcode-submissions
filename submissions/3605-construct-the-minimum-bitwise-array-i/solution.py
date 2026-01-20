class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            curr = 0
            if num == 2:
                ans.append(-1)
                continue
            while curr <= num:
                if curr | (curr + 1) == num:
                    ans.append(curr)
                    break
                curr += 1
        return ans
        
