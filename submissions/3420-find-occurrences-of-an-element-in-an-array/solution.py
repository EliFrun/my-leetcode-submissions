class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        lis = [-1] * (len(nums) + 1)
        count = 0
        for i, num in enumerate(nums):
            if num == x:
                count += 1
            if lis[count] == -1:
                lis[count] = i
            
        return [lis[q] if q < len(lis) else -1 for q in queries]

        
