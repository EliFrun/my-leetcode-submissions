class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()

        if len(nums) % 2 == 0:
            return min(
                [
                    (x + y) / 2 for x, y in zip(
                        nums[:len(nums)//2],
                        nums[len(nums):len(nums)//2 - 1:-1]
                    )
                ]
            )
        
        return min(
                [float(len(nums)//2)] + [
                    (x + y) / 2 for x, y in zip(
                        nums[:len(nums)//2],
                        nums[len(nums):len(nums)//2:-1]
                    )
                ]
            )
        
