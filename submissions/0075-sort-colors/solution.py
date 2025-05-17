class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)
        l = 0
        for i in range(3):
            for j in range(l, l + c[i]):
                nums[j] = i
            l = l + c[i]

        
            
            
        
