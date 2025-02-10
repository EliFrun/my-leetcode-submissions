class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return

        n = len(nums)
        for i in range((k + 1)//2):
            tmp = nums[- i - 1]
            nums[- i - 1] = nums[n - k + i]
            nums[n - k + i] = tmp

        for i in range((n - k + 1)//2):
            tmp = nums[n - 1 - k - i]
            nums[n - 1 - k - i] = nums[i]
            nums[i] = tmp


        for i in range(n // 2):
            tmp = nums[len(nums) - 1 - i]
            nums[len(nums) - 1 - i] = nums[i]
            nums[i] = tmp
