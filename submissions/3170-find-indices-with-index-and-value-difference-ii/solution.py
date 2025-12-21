class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        s = SortedList([(x, i) for i, x in enumerate(nums) if i >= indexDifference])
        
        for i, num in enumerate(nums):
            if i >= len(nums) - indexDifference:
                break
            if abs(num - s[0][0]) >= valueDifference:
                return [i, s[0][1]]
            elif abs(num - s[-1][0]) >= valueDifference:
                return [i, s[-1][1]]
            s.remove((nums[i + indexDifference], i + indexDifference))
        
        return [-1, -1]
